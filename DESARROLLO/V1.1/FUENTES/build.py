from pathlib import Path
import struct, functools, json, zipfile, io, os
LEVEL=int(os.environ.get("NEPTUNO_LEVEL","1"))
from PIL import Image,ImageDraw
import numpy as np
P=Path(__file__).parent; A=P/'assets'; A.mkdir(exist_ok=True)
ORG=0x6000
b=bytearray(); labels={}; fix=[]; listing=[]
def L(n):
 assert n not in labels,n; labels[n]=ORG+len(b);listing.append(n+':')
def E(s,*v):listing.append('    '+s);b.extend(v)
def W(s,op,n):
 listing.append('    '+s); b.append(op); pos=len(b);b.extend(b'\0\0');
 if isinstance(n,str):fix.append((pos,n))
 else:b[pos:pos+2]=struct.pack('<H',n)
def DW(n):
 pos=len(b);b.extend(b'\0\0');fix.append((pos,n));listing.append('    dw '+n)
def data(n,d):
 L(n);d=bytes(d);b.extend(d)
 for i in range(0,len(d),24):listing.append('    db '+','.join(map(str,d[i:i+24])))
def J(n,c=''):W('jp '+(c+',' if c else '')+n,{'':0xc3,'nz':0xc2,'z':0xca,'nc':0xd2,'c':0xda,'p':0xf2,'m':0xfa}[c],n)
def C(n):W('call '+n,0xcd,n)
def ret(c=''):E('ret '+c,{'':0xc9,'z':0xc8,'nz':0xc0,'c':0xd8,'nc':0xd0,'m':0xf8,'p':0xf0}[c])
def la(n):W('ld a,('+str(n)+')',0x3a,n)
def sa(n):W('ld ('+str(n)+'),a',0x32,n)
def lh(n):W('ld hl,'+str(n),0x21,n)
def ld(n):W('ld de,'+str(n),0x11,n)
def lc(n):W('ld bc,'+str(n),0x01,n)
def lhm(n):W('ld hl,('+str(n)+')',0x2a,n)
def shm(n):W('ld ('+str(n)+'),hl',0x22,n)
def imm(v):E('ld a,'+str(v),0x3e,v&255)
def cp(v):E('cp '+str(v),0xfe,v&255)
def andi(v):E('and '+str(v),0xe6,v)
def add(v):E('add a,'+str(v),0xc6,v&255)
def sub(v):E('sub '+str(v),0xd6,v&255)
def reg(s):
 # fixed register transfers and simple ALU instructions
 if s.startswith('ld ') and ',' in s:
  x,y=s[3:].split(',');rr={'b':0,'c':1,'d':2,'e':3,'h':4,'l':5,'(hl)':6,'a':7}
  if x in rr and y in rr:E(s,0x40+rr[x]*8+rr[y]);return
  if x in rr and y.isdigit():E(s,0x06+rr[x]*8,int(y));return
 d={'xor a':[0xaf],'or a':[0xb7],'or b':[0xb0],'or c':[0xb1],'add a,a':[0x87],'and b':[0xa0],'add a,b':[0x80],'sub b':[0x90],'sub c':[0x91],'cp b':[0xb8],'cp c':[0xb9],'inc a':[0x3c],'dec a':[0x3d],'inc b':[0x04],'dec b':[0x05],'inc c':[0x0c],'dec c':[0x0d],'inc hl':[0x23],'dec hl':[0x2b],'inc de':[0x13],'dec de':[0x1b],'inc h':[0x24],'inc l':[0x2c],'inc d':[0x14],'dec h':[0x25],'add hl,hl':[0x29],'add hl,de':[0x19],'add hl,bc':[0x09],'ex de,hl':[0xeb],'push hl':[0xe5],'pop hl':[0xe1],'push de':[0xd5],'pop de':[0xd1],'push bc':[0xc5],'pop bc':[0xc1],'push af':[0xf5],'pop af':[0xf1],'pop ix':[0xdd,0xe1],'inc ix':[0xdd,0x23],'ld a,(de)':[0x1a],'ld (de),a':[0x12],'rrca':[0x0f],'rlca':[0x07],'ldir':[0xed,0xb0],'ldi':[0xed,0xa0],'halt':[0x76],'di':[0xf3],'ei':[0xfb],'im 1':[0xed,0x56],'in a,(c)':[0xed,0x78],'sbc hl,de':[0xed,0x52],'and (ix+0)':[0xdd,0xa6,0],'or (ix+1)':[0xdd,0xb6,1],'ld a,(ix+0)':[0xdd,0x7e,0]}
 E(s,*d[s])
def R(*ss):
 for s in ss:reg(s)
def setv(n,v):imm(v);sa(n)
def zero(n):R('xor a');sa(n)
def bit(i):E('bit '+str(i)+',a',0xcb,0x47+8*i)
def lookup(table): # A index -> HL word
 R('ld l,a','ld h,0','add hl,hl');ld(table);R('add hl,de','ld e,(hl)','inc hl','ld d,(hl)','ex de,hl')
def incv(n):la(n);R('inc a');sa(n)
def decv(n):la(n);R('dec a');sa(n)
def copyv(src,dst):la(src);sa(dst)
# Neptuno Engine: native Z80 machine-code emitter. All addresses resolved below.
import math
ROOT=P
BUF=0x9000; END=0xA200; PHASE=0xA200; CLEAN=0xC700; WORLD=0xD900; SPR=0xF100
STACK=0x9000; IM2TAB=0x7F00; ISR=0x8E8E
# Additional instructions.
def X(s,*v):E(s,*v)
def edword(s,k,n):
 E(s,0xed,k); pos=len(b); b.extend(b'\0\0'); fix.append((pos,n)) if isinstance(n,str) else b.__setitem__(slice(pos,pos+2),struct.pack('<H',n))
def bc_m(n):edword('ld bc,('+str(n)+')',0x4b,n)
def de_m(n):edword('ld de,('+str(n)+')',0x5b,n)
def save_sp(n):edword('ld ('+str(n)+'),sp',0x73,n)
def load_sp(n):edword('ld sp,('+str(n)+')',0x7b,n)
def pad(addr):
 assert ORG+len(b)<=addr,(hex(ORG+len(b)),hex(addr));n=addr-ORG-len(b)
 if n: b.extend(bytes(n));listing.append('    defs '+str(n)+',0')
def jr(n,c=''): # use absolute jp to keep source generator simple
 J(n,c)
def attr(y):return 0x4000+((y&0xc0)<<5)+((y&7)<<8)+((y&0x38)<<2)
def tabwords(n,vals):data(n,b''.join(struct.pack('<H',v) for v in vals))

def packbits(raw):
 # Greedy LZ/RLE, independent streams. 1..127 literal, 128..191 repeat 3..66,
 # 192..255 backward copy 3..66, little endian distance. 0 end.
 out=bytearray();i=0;lit=bytearray();raw=bytes(raw)
 def flush():
  if lit:out.append(len(lit));out.extend(lit);lit.clear()
 while i<len(raw):
  run=1
  while i+run<len(raw) and raw[i+run]==raw[i] and run<66:run+=1
  best=0;dist=0
  if i+3<=len(raw):
   key=raw[i:i+3];pos=raw.rfind(key,max(0,i-65535),i)
   tries=0
   while pos>=0 and tries<128:
    k=3
    while k<66 and i+k<len(raw) and raw[pos+k]==raw[i+k]:k+=1
    if k>best:best=k;dist=i-pos
    if best==66:break
    pos=raw.rfind(key,max(0,i-65535),pos);tries+=1
  if run>=3 and run>=best-1:
   flush();out.extend([128+run-3,raw[i]]);i+=run
  elif best>=5:
   flush();out.append(192+best-3);out.extend(struct.pack('<H',dist));i+=best
  else:
   lit.append(raw[i]);i+=1
   if len(lit)==127:flush()
 flush();out.append(0);return bytes(out)
def packtest(p):
 i=0;out=bytearray()
 while p[i]:
  n=p[i];i+=1
  if n>=192:
   dist=int.from_bytes(p[i:i+2],'little');i+=2
   for _ in range((n&63)+3):out.append(out[-dist])
  elif n>=128:out.extend([p[i]]*((n&63)+3));i+=1
  else:out.extend(p[i:i+n]);i+=n
 return out

world=Image.open(A/({1:'mapa_legible.png',2:'grecia_legible.png'}.get(LEVEL,f'map{LEVEL}.png'))).convert('1'); assert world.size==(192,768)
if LEVEL==1:
 boss=Image.frombytes('1',(144,144),(A/'boss.bin').read_bytes()); mk=Image.frombytes('1',(144,144),(A/'boss_mask.bin').read_bytes()).point(lambda v:255-v)
elif LEVEL==2:
 boss=Image.open(A/'rodas_PNG.png').convert('1');mk=Image.open(A/'rodas_MASK.png').convert('1').point(lambda v:255-v)
else:
 boss=Image.open(A/f'boss{LEVEL}_PNG.png').convert('1');mk=Image.open(A/f'boss{LEVEL}_MASK.png').convert('1').point(lambda v:255-v)
 # Align the bottom of the 104-pixel native asset with the shared 144-line boss arena.
level=Image.new('1',(192,960));level.paste(world,(0,192));level.paste(boss,(24,144-boss.height),mk);level.save(ROOT/f'terrain{LEVEL}.png')
# Lossless 512 native 8x8 tile bank; forbid any substitution.
from collections import Counter
raw=np.frombuffer(level.tobytes(),np.uint8).reshape(960,24)
rows=[[raw[y:y+8,x].tobytes() for x in range(24)] for y in range(0,960,8)]
counts=Counter(v for row in rows for v in row); protected=list(dict.fromkeys(v for row in rows[:24] for v in row)); assert len(counts)<=512,(LEVEL,len(counts))
bank=protected+[v for v,_ in counts.most_common() if v not in protected];ids={v:i for i,v in enumerate(bank)};changes=0
rows=[[ids[v] for v in row] for row in rows]
recon=np.zeros((960,24),np.uint8)
for y,row in enumerate(rows):
 for x,i in enumerate(row):recon[y*8:y*8+8,x]=np.frombuffer(bank[i],np.uint8)
assert recon.tobytes()==level.tobytes(), 'lossy map forbidden'
Image.frombytes('1',(192,960),recon.tobytes()).save(ROOT/f'terrain{LEVEL}.png')
planes=bytes(v[j] for j in range(8) for v in (bank+[bytes(8)]*(512-len(bank))))
encoded=[]
for row in rows[::-1]:
 r=bytearray()
 for g in range(0,24,8):
  group=row[g:g+8];r.append(sum((128>>i) for i,v in enumerate(group) if v>=256));r.extend(v&255 for v in group)
 encoded.append(bytes(r))
world_first=planes+b''.join(encoded[:75]);world_tail=b''.join(encoded[75:]);print('map tiles',len(counts),len(bank),'merged placements',changes,'map',len(world_first),len(world_tail))
screens={n:packbits((A/f).read_bytes()) for n,f in [('over_scr','GAME_OVER.scr'),('clear_scr','FASE_SUPERADA.scr' if LEVEL==1 else 'FASE_SUPERADA_2.scr')]}
assert all(packtest(screens[n])==(A/f).read_bytes() for n,f in [('over_scr','GAME_OVER.scr'),('clear_scr','FASE_SUPERADA.scr' if LEVEL==1 else 'FASE_SUPERADA_2.scr')])
# dynamic extra phase assets; reserve original pre-shift locations
POWER=0xf760; BOAT=0xf8e0; EXP=0xfa60; CLEAR=0xfbe0; BALL=0xfd80; SOLDIER=0xfde0; TANK=0xfe40; TURRET_L=0xfea0; TURRET_R=0xfed0
# clear screen compressed stored in phase, not overwritten during play
assert CLEAR+len(screens['clear_scr'])<=BALL, len(screens['clear_scr'])

# Resident low section: entry, fixed HUD, tables and state.
L('entry');J('boot')
# HUD is fixed native pixel bitmap/attributes; copy at level initialization only.
hud=bytearray((ROOT/'HUD.scr').read_bytes());zero_rows=[int(r,2)<<2 for r in '01110/11011/11011/11011/11011/11011/01110'.split('/') for _ in range(2)]+[0,0]
for yy,v in enumerate(zero_rows,96):hud[attr(yy)-0x4000+25:attr(yy)-0x4000+31]=bytes([v])*6
for yy in range(168,176):hud[attr(yy)-0x4000+25:attr(yy)-0x4000+31]=bytes(6)
data('hud_bitmap',packbits(b''.join(hud[attr(y)-0x4000+24:attr(y)-0x4000+32] for y in range(192))))
data('hud_attrs',b''.join(hud[6144+y*32+24:6144+y*32+32] for y in range(24)))
tabwords('rowptr',[BUF+i*24 for i in range(192)])
tabwords('screen_lut',[attr(y) for y in range(192)])
# Phase-local stack chain address table, fixed 48 bytes/scanline + 9 bytes per band wrapper.
# Each band begins with LD (saved_sp),SP (4), then 96 rows, then LD SP,(saved_sp) + RET (5).
TOP=PHASE; BOTTOM=TOP+4+96*48+5
for name,base in [('top_links',TOP),('bottom_links',BOTTOM)]:tabwords(name,[base+4+i*48+1 for i in range(96)])
# lookup tables for native sprite shift variants, phase layout fixed.
shipbase=SPR; dronebase=shipbase+8*96; fighterbase=dronebase+8*48; bulletbase=fighterbase+8*48; blankbase=bulletbase+8*12
for name,base,step in [('ship_ptr',shipbase,96),('drone_ptr',dronebase,48),('fighter_ptr',fighterbase,48),('bullet_ptr',bulletbase,12),('power_ptr',POWER,48),('boat_ptr',BOAT,48),('expl_ptr',EXP,24),('ball_ptr',BALL,12),('soldier_ptr',SOLDIER,0),('tank_ptr',TANK,0),('turret_l_ptr',TURRET_L,0),('turret_r_ptr',TURRET_R,0)]:tabwords(name,[base+(48 if name in ('soldier_ptr','tank_ptr') and i==1 else i*step) for i in range(8)])
# 4 pre-shifts (0,2,4,6), shared by adjacent x positions. Two drone and three bird poses.
for name,base in [('drone_ptr',dronebase),('fighter_ptr',fighterbase)]:
 pos=labels[name]-ORG; b[pos:pos+16]=b''.join(struct.pack('<H',base+(i//2)*48) for i in range(8))
 # Keep generated listing faithful to the emitted bytes.
 for j,ln in enumerate(listing):
  if ln==name+':':listing[j+1]='    db '+','.join(map(str,b[pos:pos+16]));break
tabwords('drone_anim_ptr',[dronebase+192+(i//2)*48 for i in range(8)])
tabwords('bird_mid_ptr',[fighterbase+192+(i//2)*48 for i in range(8)])
tabwords('bird_fold_ptr',[[0xff60,0xff90,0xffc0,0xc6a8][i//2] for i in range(8)])
# State: coordinate records x,y. y=255 means inactive for bullets.
for n,v in [('head',0),('world_y',0),('tick',0),('dx',0),('dy',0),('fire',0),('joymode',0),('joyraw',0),('cool',0),('sound',0),('bandrow',0),('patch_on',0),('draw_h',0),('phase_error',0)]:data(n,[v])
for n in ['saved_sp','patch_addr','patch_value','band_table','src_start','sprite_table','sprite_data','tmp_ptr']:data(n,[0,0])
records=['player']+[f'e{i}' for i in range(4)]+[f's{i}' for i in range(6)]+['b0','b1','powerup']
for n in records:data(n,[88,152] if n=='player' else [0,255]);labels[n+'_y']=labels[n]+1
for n in records:data('old_'+n,[0,255]);labels['old_'+n+'_y']=labels['old_'+n]+1
for n,v in [('lives',3),('invul',0),('death',0),('death_timer',0),('spread_lo',0),('spread_hi',0),('kills',0),('dirty',0),('life_dirty',0),('boss',0),('boss_hp',20),('game_state',0),('wave',0),('enemy_fire',0),('score0',0),('score1',0),('score2',0),('score3',0),('score4',0),('score5',0),('snapshot_kind',0)]+[(f'e{i}_wait',0) for i in range(4)]+[(f's{i}_dx',0) for i in range(6)]:data(n,[v])
for n in ['world_ptr','remaining']:data(n,[0,0])
# resident data in spare low RAM
L('overlay_start');data('world_limit',struct.pack('<H',WORLD+len(world_first)));data('phase_id',[LEVEL]);data('phase_color',[[69,71,70,66,68][LEVEL-1]]);data('initial_hp',[[20,28,32,38,44][LEVEL-1]]);data('boss_thresholds',[[16,23,26,31,36][LEVEL-1],[11,16,18,21,25][LEVEL-1],[6,8,9,10,12][LEVEL-1]]);assert len(world_tail)<=1300;data('world_tail',world_tail);from hud_names import bitmap as phase_name_bitmap;data('phase_name',phase_name_bitmap(LEVEL));data('tail_pad',bytes(1300-len(world_tail)-42));labels['clear_scr']=CLEAR
exec((ROOT/'waves.py').read_text())
data('over_scr',screens['over_scr']);exec((ROOT/'flow.py').read_text());exec((ROOT/'audio.py').read_text())
print('low end',hex(ORG+len(b)));pad(0x7e70)
for j in range(4):data('hud_dest_data'+str(j),b''.join(struct.pack('<H',attr(y)+25+j) for y in range(96,112)))
# Place IM2 vector in resident memory. Every possible interrupt vector resolves to 8E8E.
pad(IM2TAB);data('im2_vectors',[0x8e]*257);pad(0x8001)
# Copy approved HUD to screen (setup only). Bitmap addresses from LUT, attributes fixed.
L('init_level');R('di','xor a');C('reset_game');X('out ($fe),a',0xd3,0xfe);lh('hud_bitmap');ld(BUF);C('unpack_to');lh(BUF);shm('tmp_ptr');lh('screen_lut');shm('sprite_table');R('ld b,192');L('hud_loop');R('push bc');lhm('sprite_table');R('ld e,(hl)','inc hl','ld d,(hl)','inc hl');shm('sprite_table');R('ex de,hl');ld(24);R('add hl,de','ex de,hl');lhm('tmp_ptr');lc(8);R('ldir');shm('tmp_ptr');R('pop bc','dec b');J('hud_loop','nz')
lh(0x5800);ld('hud_attrs');R('ld b,24');L('attrrow');R('push bc','ld b,24');L('attrleft');la('phase_color');R('ld (hl),a');R('inc hl','dec b');J('attrleft','nz');R('ld b,8');L('attrright');R('ld a,(de)','ld (hl),a','inc de','inc hl','dec b');J('attrright','nz');R('pop bc','dec b');J('attrrow','nz')
# Fill ring with bottom 192 rows in reverse order, exactly the approved scroll direction.
zero('head');lh(WORLD+4096);shm('world_ptr');lh(960);shm('remaining');setv('world_y',0)
R('ld b,192');L('init_rows');R('push bc');C('scroll_one');R('pop bc','dec b');J('init_rows','nz')
C('draw_snapshot');C('blit_top');C('blit_bottom');C('restore_snapshot');C('hud_initial');R('ei');ret()
# Maintain the validated two-band presentation; collision / HUD work divided across ticks.
L('main');C('audio_wait');L('frame_a_ready');C('keys');C('logic');C('draw_snapshot');C('top_delay');C('blit_top');L('frame_b_wait');C('audio_wait');L('frame_b_ready');C('blit_bottom');C('restore_snapshot');C('keys');C('logic');C('scroll_one');C('hud_update');la('game_state');R('or a');J('main','z');J('end_game')
# Init presents one snapshot and restores the buffer before the first scheduled frame.
L('top_delay');lc(55);L('delay_loop');X('dec bc',0x0b);R('ld a,b','or c');J('delay_loop','nz');ret()
# Phase chain setup. Source row = logical head (+96 for bottom), patch only one wrap link if needed.
L('blit_top');la('head');lh('top_links');ld(TOP);J('blit_setup')
L('blit_bottom');la('head');add(96);J('bottom_carry','c');cp(192);J('bottom_ok','c');sub(192);J('bottom_ok');L('bottom_carry');add(64);L('bottom_ok');lh('bottom_links');ld(BOTTOM)
L('blit_setup');sa('bandrow');shm('band_table');R('ex de,hl');shm('band_entry');R('ld l,a','ld h,0','add hl,hl');ld('rowptr');R('add hl,de','ld e,(hl)','inc hl','ld d,(hl)');lhm('band_table');R('ld a,(hl)','inc hl','ld h,(hl)','ld l,a','ld (hl),e','inc hl','ld (hl),d');zero('patch_on');la('bandrow');cp(97);J('blit_go','c');R('ld c,a');imm(192);X('sub c',0x91);R('ld l,a','ld h,0','add hl,hl');de_m('band_table');R('add hl,de','ld e,(hl)','inc hl','ld d,(hl)','ex de,hl');shm('patch_value');X('ld (hl),0',0x36,0);R('inc hl');X('ld (hl),144',0x36,144);R('dec hl');ld(0xfff3);R('add hl,de');shm('patch_addr');ld('saved_sp_sink');R('ld (hl),e','inc hl','ld (hl),d');setv('patch_on',1)
L('blit_go');R('di');L('band_call');W('call band_entry',0xcd,TOP);R('ei');la('patch_on');R('or a');ret('z');lhm('patch_addr');de_m('patch_value');R('ld (hl),e','inc hl','ld (hl),d');ret()
# `band_entry` aliases the CALL's writable immediate, not another state variable.
labels['band_entry']=labels['band_call']+1
# Input copied from GRIT-style port polling, with Kempston fire auto-selection.
L('keys');R('xor a');sa('dx');sa('dy');sa('fire');lc(0xfbfe);R('in a,(c)');bit(0);J('kq','nz');setv('dy',255)
L('kq');lc(0xfdfe);R('in a,(c)');bit(0);J('ka','nz');setv('dy',1)
L('ka');lc(0xdffe);R('in a,(c)');bit(1);J('ko','nz');setv('dx',255)
L('ko');R('in a,(c)');bit(0);J('kp','nz');setv('dx',1)
L('kp');lc(0x7ffe);R('in a,(c)');bit(0);J('ks','nz');setv('fire',1)
L('ks');lc(31);R('in a,(c)','ld b,a');andi(224);ret('nz');R('ld a,b');sa('joyraw');bit(4);J('kj','z');setv('joymode',1)
L('kj');la('joymode');R('or a');ret('z');la('joyraw');bit(0);J('kj1','z');setv('dx',1)
L('kj1');la('joyraw');bit(1);J('kj2','z');setv('dx',255)
L('kj2');la('joyraw');bit(2);J('kj3','z');setv('dy',1)
L('kj3');la('joyraw');bit(3);J('kj4','z');setv('dy',255)
L('kj4');la('joyraw');bit(4);ret('z');setv('fire',1);ret()
# Input/game logic, called twice per complete snapshot. 1 pixel per interrupt.
L('logic');incv('tick');la('game_state');R('or a');ret('nz');la('boss');cp(3);ret('z')
# 16-bit countdown for spread (500 ticks)
la('spread_hi');R('ld b,a');la('spread_lo');R('or b');J('spread_done','z');lhm('spread_lo');R('dec hl');shm('spread_lo');L('spread_done')
la('invul');R('or a');J('no_inv','z');decv('invul');L('no_inv')
la('death');R('or a');J('alive','z');decv('death_timer');la('death_timer');R('or a');J('move_enemies','nz');la('death');cp(1);J('respawn','nz');la('lives');R('or a');J('dead_final','z');setv('death',2);setv('death_timer',35);J('move_enemies');L('dead_final');setv('game_state',1);ret();L('respawn');zero('death');setv('player',88);setv('player_y',160);setv('invul',150);setv('b0_y',255);setv('b1_y',255);J('move_enemies')
L('alive');la('dx');R('ld b,a');la('player');R('add a,b');cp(169);J('mx','nc');sa('player');L('mx');la('dy');R('ld b,a');la('player_y');R('add a,b');cp(177);J('my','nc');R('ld b,a');la('boss');R('or a');J('my_ok','z');R('ld a,b');cp(144);J('my','c');L('my_ok');R('ld a,b');sa('player_y');L('my')
L('move_enemies');la('boss');R('or a');J('move_shots','nz')
C('waves_step')
L('move_shots')
for j in range(6):
 n=f's{j}';la(n+'_y');cp(255);J(n+'_skip','z');cp(6);J(n+'_off','c');sub(6);sa(n+'_y');la(n+'_dx');R('ld b,a');la(n);R('add a,b');cp(176);J(n+'_off','nc');sa(n);J(n+'_skip');L(n+'_off');setv(n+'_y',255);L(n+'_skip')
# DDA motion for two aimed enemy projectile slots.
for j in range(2):C(f'move_b{j}')
C('enemy_attack')
L('no_enemy_fire')
# Falling power-up and pickup. Overlap checks are cheap bounding boxes.
la('powerup_y');cp(255);J('power_done','z');la('tick');andi(1);J('power_check','nz');incv('powerup_y');la('powerup_y');cp(177);J('power_check','c');setv('powerup_y',255);J('power_done')
L('power_check');la('death');R('or a');J('power_done','nz');C('power_collision');L('power_done')
# On alternate ticks check collisions. Fire still 50Hz.
la('tick');andi(1);J('after_hits','nz');C('collisions');L('after_hits')
la('death');R('or a');ret('nz');la('cool');R('or a');J('tryfire','z');decv('cool');ret()
L('tryfire');la('fire');R('or a');ret('z');la('player_y');cp(4);ret('c')
# two triple groups: each group has 3 independently moving bullets; normal uses central slot only.
for j in (0,3):
 la(f's{j}_y');cp(255);J(f'spawn{j}','z')
ret()
for j in (0,3):
 L(f'spawn{j}');la('player');add(7);sa(f's{j}');la('player_y');sub(4);sa(f's{j}_y');zero(f's{j}_dx');setv('cool',15);C('beep');la('spread_hi');R('ld b,a');la('spread_lo');R('or b');ret('z');C('sfx_spread')
 for k,delta in ((j+1,255),(j+2,1)):
  la(f's{k}_y');cp(255);J(f'no_side{k}','nz');la('player');add(7);sa(f's{k}');la('player_y');sub(4);sa(f's{k}_y');setv(f's{k}_dx',delta);L(f'no_side{k}')
 ret()
# Pixel ring address: BC = y,x (B=y C=x); HL points to physical row + x/8.
L('ring_addr');R('ld a,b','ld hl,0') if False else None
la('head');R('add a,b'); # sum can exceed 255: need carry-aware mod 192
J('ring_carry','c');cp(192);J('ring_ok','c');sub(192);J('ring_ok');L('ring_carry');add(64);L('ring_ok');R('ld l,a','ld h,0','add hl,hl');ld('rowptr');R('add hl,de','ld e,(hl)','inc hl','ld d,(hl)','ex de,hl','ld a,c','rrca','rrca','rrca');andi(31);R('ld e,a','ld d,0','add hl,de');ret()
# draw_snapshot called only on restored buffer. Save coordinates used for later restoration.
L('draw_snapshot')
# player explosion uses same sized OR sprite. Blink on reappearance by omitting player on alternating snapshots.
la('death');cp(2);J('hide_player','z');cp(1);J('draw_explosion','z');la('invul');R('or a');J('draw_player','z');la('tick');andi(4);J('hide_player','nz');L('draw_player');bc_m('player');lh('ship_ptr');imm(16);C('draw_mask');J('player_drawn');L('draw_explosion');bc_m('player');la('death_timer');andi(8);C('draw_burst');J('player_drawn');L('hide_player');setv('snapshot_kind',1);J('draw_others');L('player_drawn');zero('snapshot_kind');L('draw_others')
for i in range(4):
 bc_m(f'e{i}');la(f'e{i}_wait');R('or a');J(f'edraw_normal{i}','z');C('draw_burst');J(f'edraw_done{i}');L(f'edraw_normal{i}');la(f'e{i}_type');C('draw_enemy_type');L(f'edraw_done{i}')
for n,table,h in [(f's{i}','bullet_ptr',4) for i in range(6)]+[('b0','ball_ptr',4),('b1','ball_ptr',4)]:
 bc_m(n);lh(table);imm(h);C('draw_or')
bc_m('powerup');la('boss');cp(3);J('power_normal_draw','nz');la('boss_hp');C('draw_burst');J('power_draw_done');L('power_normal_draw');lh('power_ptr');imm(16);C('draw_or');L('power_draw_done');lh('player');ld('old_player');lc(len(records)*2);R('ldir');la('snapshot_kind');R('or a');ret('z');setv('old_player_y',255);ret()
# BC coordinate, HL shift table, A height; DE sprite bytes, HL destination.
L('draw_mask');sa('draw_h');C('sprite_setup');ret('c');la('draw_h');R('ld b,a');L('maskrow')
for i in range(3):
 R('ld a,(de)');X('and (hl)',0xa6);R('inc de','ld c,a','ld a,(de)','or c','ld (hl),a','inc de');
 if i!=2:R('inc hl')
R('ld a,l');add(22);R('ld l,a');J('maskrow_nowrap','nc');R('inc h','ld a,h');cp(0xa2);J('maskrow_nowrap','c');R('ld h,144');L('maskrow_nowrap');R('dec b');J('maskrow','nz');ret()
L('draw_or');sa('draw_h');C('sprite_setup');ret('c');la('draw_h');R('ld b,a');L('orrow')
for i in range(3):
 R('ld a,(de)');X('or (hl)',0xb6);R('ld (hl),a','inc de');
 if i!=2:R('inc hl')
R('ld a,l');add(22);R('ld l,a');J('orrow_nowrap','nc');R('inc h','ld a,h');cp(0xa2);J('orrow_nowrap','c');R('ld h,144');L('orrow_nowrap');R('dec b');J('orrow','nz');ret()
L('sprite_setup');R('ld a,b');cp(192);J('sprite_inactive','nc');C('clip_height');R('ld a,c');andi(7);R('add a,a','ld e,a','ld d,0','add hl,de','ld e,(hl)','inc hl','ld d,(hl)','push de');C('ring_addr');R('pop de','or a');ret()
L('sprite_inactive');X('scf',0x37);ret()
L('next_row');R('ld a,l');add(21);R('ld l,a');J('next_noc','nc');R('inc h');L('next_noc');R('ld a,h');cp(0xa2);ret('c');R('ld h,144');ret()
# Restore all old regions using clean ring. No VRAM access and no order dependency.
L('restore_snapshot')
for n in records:bc_m('old_'+n);imm(16 if n=='player' or n.startswith('e') or n=='powerup' else 4);C('restore_rect')
ret()
L('restore_rect');sa('draw_h');R('ld a,b');cp(192);ret('nc');C('clip_height');C('ring_addr');R('ld e,l','ld a,h');add((CLEAN-BUF)>>8);R('ld d,a');la('draw_h');R('ld b,a','ld c,255');L('restore_row')
# LDI copies HL->DE, so swap pointers for the three bytes. C never wraps (max 48 copies), B retains row count.
R('ex de,hl','ldi','ldi','ex de,hl','ld a,(de)','ld (hl),a')
R('ld a,l');add(22);R('ld l,a','ld e,a');J('restore_row_nowrap','nc');R('inc h','inc d','ld a,h');cp(0xa2);J('restore_row_nowrap','c');R('ld h,144','ld d,199');L('restore_row_nowrap');R('dec b');J('restore_row','nz');ret()
# One-pixel downward scroll: replace only the new ring head, clean + compositing copy.
# Scroll: consume one compact 24-byte scanline. Three masks, MSB first.
L('scroll_one');la('boss');cp(3);J('boss_decay','z');lhm('remaining');R('ld a,h','or l') if False else None
R('ld a,h');X('or l',0xb5);ret('z');R('dec hl');shm('remaining');R('ld a,h');X('or l',0xb5);J('not_at_boss','nz');setv('boss',2);copyv('initial_hp','boss_hp');L('not_at_boss')
# Boss starts entering 144 lines before the end. Remove normal enemies then.
lhm('remaining');R('ld a,h','or a');J('not_boss_entry','nz');R('ld a,l');cp(144);J('not_boss_entry','nz');setv('boss',1);setv('b0_y',255);setv('b1_y',255);la('player_y');cp(144);J('boss_player_safe','nc');setv('player_y',144);L('boss_player_safe')
for j in range(4):setv(f'e{j}_y',255);zero(f'e{j}_wait')
L('not_boss_entry');la('head');R('or a');J('scroll_nz','nz');imm(192);L('scroll_nz');R('dec a');sa('head');R('ld l,a','ld h,0','add hl,hl');ld('rowptr');R('add hl,de','ld e,(hl)','inc hl','ld d,(hl)');X('ld (src_start),de',0xed,0x53,0,0);fix.append((len(b)-2,'src_start'));lhm('world_ptr')
# Decode one tile scanline; map pointer advances only after eight lines.
la('remaining');andi(7);R('add a,a');add(WORLD>>8);X('exx',0xd9);R('ld b,a');X('exx',0xd9)
R('ld b,3');L('decode_group');R('push bc','ld c,(hl)','inc hl','ld b,8');L('decode_byte');R('ld a,c','rlca','ld c,a','ld a,(hl)','inc hl');X('exx',0xd9);R('ld l,a','ld h,b');J('decode_low','nc');R('inc h');L('decode_low');R('ld a,(hl)');X('exx',0xd9);R('ld (de),a','inc de','dec b');J('decode_byte','nz');R('pop bc','dec b');J('decode_group','nz')
la('remaining');andi(7);J('world_continue','nz');shm('world_ptr');de_m('world_limit');R('or a','sbc hl,de');J('world_continue','nz');lh('world_tail');shm('world_ptr');L('world_continue');lhm('src_start');R('ld e,l','ld a,h');add((CLEAN-BUF)>>8);R('ld d,a');lc(24);R('ldir');ret()
# Additional game routines go in reserved resident memory below ISR.
extra_phase={}
exec((ROOT/'game_logic.py').read_text())
exec((ROOT/'wave_motion.py').read_text())
# Resident interrupt handler and reserved stack.
# IM2 handler preserves registers, no ROM or contended stack accesses during SP transfer.
print('high code ends',hex(ORG+len(b)))
exec((ROOT/'audio_wait.py').read_text());pad(ISR);L('isr');J('isr_audio');pad(0x8f00);L('saved_sp_sink');data('sink',[0,0]);pad(0x9000)
# End of resident kernel.
for pos,n in fix:b[pos:pos+2]=struct.pack('<H',labels[n])
kernel=bytes(b);assert len(kernel)==0x3000
# Phase pack: two unrolled stack chains; group saves source SP into next LD SP operand.
phase=bytearray(0x10000-PHASE)
phase_asm=[]
def emit_phase(addr,s):phase[addr-PHASE:addr-PHASE+len(s)]=s
for band,base in enumerate([TOP,BOTTOM]):
 emit_phase(base,bytes([0xed,0x73])+struct.pack('<H',labels['saved_sp']));phase_asm.append(f'ORG ${base:04X}\n    ld (saved_sp),sp')
 for row in range(96):
  y=band*96+row; dst=attr(y)
  for group in range(2):
   here=base+4+row*48+group*24
   target=here+25 if not(row==95 and group==1) else labels['saved_sp_sink']
   code=bytes([0x31,0,0,0xc1,0xd1,0xe1,0xd9,0xc1,0xd1,0xe1,0xed,0x73])+struct.pack('<H',target)+bytes([0x31])+struct.pack('<H',dst+(group+1)*12)+bytes([0xe5,0xd5,0xc5,0xd9,0xe5,0xd5,0xc5]);assert len(code)==24
   emit_phase(here,code)
   phase_asm.append(f'row_{y}_{group}:\n    ld sp,0\n    pop bc\n    pop de\n    pop hl\n    exx\n    pop bc\n    pop de\n    pop hl\n    ld (${target:04X}),sp\n    ld sp,${dst+(group+1)*12:04X}\n    push hl\n    push de\n    push bc\n    exx\n    push hl\n    push de\n    push bc')
 end=base+4+96*48;emit_phase(end,bytes([0xed,0x7b])+struct.pack('<H',labels['saved_sp'])+bytes([0xc9]));phase_asm.append('    ld sp,(saved_sp)\n    ret')
assert BOTTOM+4617<=CLEAN
emit_phase(WORLD,world_first);emit_phase(CLEAR,screens['clear_scr'])
for a,d in extra_phase.items():emit_phase(a,d)
# Exact 8 shift variants, 3 bytes/line, player's original 16x24 adapted to 16x16 for this benchmark.
def shifted(raw,mask,h,base):
 a=np.unpackbits(np.frombuffer(raw,dtype=np.uint8)).reshape(h,-1);m=np.unpackbits(np.frombuffer(mask,dtype=np.uint8)).reshape(h,-1) if mask is not None else None
 for shift in range(8):
  x=np.zeros((h,24),np.uint8);x[:,shift:shift+a.shape[1]]=a;packed=np.packbits(x,axis=1)
  if m is not None:
   mm=np.ones((h,24),np.uint8);mm[:,shift:shift+a.shape[1]]=m;mp=np.packbits(mm,axis=1);assert not (mp&packed).any();z=np.empty((h,6),np.uint8);z[:,::2]=mp;z[:,1::2]=packed;packed=z
  emit_phase(base+shift*packed.size,packed.tobytes())
ship=Image.frombytes('1',(16,24),(ROOT/'cielo_rojo_0.bitmap.bin').read_bytes()).resize((16,16),Image.Resampling.NEAREST);mk=Image.frombytes('1',(16,24),(ROOT/'cielo_rojo_0.mask.bin').read_bytes()).resize((16,16),Image.Resampling.NEAREST);shifted(ship.tobytes(),mk.tobytes(),16,shipbase)
def airframes(raw,addresses):
 a=np.unpackbits(np.frombuffer(raw,np.uint8)).reshape(16,16)
 for shift,base in zip((0,2,4,6),addresses):
  x=np.zeros((16,24),np.uint8);x[:,shift:shift+16]=a;emit_phase(base,np.packbits(x,axis=1).tobytes())
drone=(ROOT/'DRON_bitmap.bin').read_bytes();bird=(ROOT/'NAVE_VERTICAL_bitmap.bin').read_bytes()
for f,start in [(2,dronebase),(1,dronebase+192)]:airframes(drone[f*32:(f+1)*32],[start+k*48 for k in range(4)])
for f,start in [(4,fighterbase),(5,fighterbase+192)]:airframes(bird[f*32:(f+1)*32],[start+k*48 for k in range(4)])
airframes(bird[6*32:7*32],[0xff60,0xff90,0xffc0,0xc6a8]);shifted(bytes([0xc0]*4),None,4,bulletbase)
shifted((A/'power_spread_0.bitmap.bin').read_bytes(),None,16,POWER)
# Surface graphics: no boats in any phase. The former boat bank stores aimed frames.
shifted(bytes([0x60,0xf0,0xf0,0x60]),None,4,BALL)
def aligned(im,base):
 a=np.packbits(np.pad(np.array(im.convert('1'),dtype=np.uint8),((0,0),(0,8))),axis=1).tobytes();assert len(a)==48;emit_phase(base,a)
# Native soldier sprites from approved bank, two walking poses per cardinal orientation.
for direction,base in [('S',0xfde0),('W',0xf940),('E',0xf9a0),('N',0xfa00)]:
 im=Image.open(A/f'soldier_{direction}.png').convert('1');aligned(im,base)
 im2=im.copy();arr=np.array(im2);arr[12:16]=np.roll(arr[12:16],1,axis=1);aligned(Image.fromarray(arr),base+48)
# Tanks retain original body and chassis orientation; cannon aims independently.
for direction,base in [('S',0xfe40),('N',0xfe70),('W',0xff00),('E',0xff30)]:
 im=Image.open(A/f'tank_{direction}.png').convert('1');aligned(im,base)
for direction,base in [('S',0xf8e0),('N',0xf910),('W',0xfea0),('E',0xfed0)]:
 aligned(Image.open(A/f'torreta_{direction}.png'),base)
# Two 8x8 native explosion frames occupy the previous single 16x16 allocation.
for i,frame in enumerate(['10000001/00100100/00011000/01111110/01111110/00011000/00100100/10000001','00100100/10000001/00011000/01000010/01000010/00011000/10000001/00100100']):
 shifted(bytes(int(row,2) for row in frame.split('/')),None,8,EXP+i*192)
# TAP BASIC loader then CODE block then raw phase data (LD-BYTES).
def block(flag,p):q=bytes([flag])+p;return struct.pack('<H',len(q)+1)+q+bytes([functools.reduce(int.__xor__,q,0)])
def header(t,n,l,p1,p2):return block(0,bytes([t])+n.encode().ljust(10,b' ')[:10]+struct.pack('<HHH',l,p1,p2))
def num(n):return str(n).encode()+bytes([14,0,0,n&255,n>>8,0])
(ROOT/f'kernel{LEVEL}.bin').write_bytes(kernel);(ROOT/f'phase{LEVEL}.bin').write_bytes(phase);(ROOT/f'symbols{LEVEL}.json').write_text(json.dumps(labels,indent=2));(ROOT/f'kernel{LEVEL}.asm').write_text('ORG $6000\n'+'\n'.join(listing));(ROOT/f'stack_blaster{LEVEL}.asm').write_text(f'saved_sp equ ${labels["saved_sp"]:04X}\n'+'\n'.join(phase_asm));print('kernel',len(kernel),'phase',len(phase),'overlay',hex(labels['overlay_start']),hex(labels['overlay_end']))
