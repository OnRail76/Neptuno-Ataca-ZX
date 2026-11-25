from pathlib import Path
p=Path('build.py');s=p.read_text();a=s.index('rows=[level.tobytes()');z=s.index('screens=',a)
s=s[:a]+'''# 512 native 8x8 tiles, arranged in eight 512-byte scanline planes.
# Keep every boss tile, preserve common scenery exactly, merge rare terrain tiles
# by minimum Hamming distance only where needed. No change to map geometry.
from collections import Counter
raw=np.frombuffer(level.tobytes(),np.uint8).reshape(960,24)
rows=[[raw[y:y+8,x].tobytes() for x in range(24)] for y in range(0,960,8)]
counts=Counter(v for row in rows for v in row); protected=list(dict.fromkeys(v for row in rows[:24] for v in row)); assert len(protected)<=512
bank=protected+[v for v,_ in counts.most_common() if v not in protected];bank=bank[:512];ids={v:i for i,v in enumerate(bank)};changes=0
for row in rows:
 for x,v in enumerate(row):
  if v not in ids:
   n=int.from_bytes(v,'little');idx=min(range(len(bank)),key=lambda k:(n^int.from_bytes(bank[k],'little')).bit_count());ids[v]=idx
  if bank[ids[v]]!=v:changes+=1
  row[x]=ids[v]
recon=np.zeros((960,24),np.uint8)
for y,row in enumerate(rows):
 for x,i in enumerate(row):recon[y*8:y*8+8,x]=np.frombuffer(bank[i],np.uint8)
Image.frombytes('1',(192,960),recon.tobytes()).save(ROOT/f'terrain{LEVEL}.png')
planes=bytes(v[j] for j in range(8) for v in (bank+[bytes(8)]*(512-len(bank))))
encoded=[]
for row in rows[::-1]:
 r=bytearray()
 for g in range(0,24,8):
  group=row[g:g+8];r.append(sum((128>>i) for i,v in enumerate(group) if v>=256));r.extend(v&255 for v in group)
 encoded.append(bytes(r))
world_first=planes+b''.join(encoded[:75]);world_tail=b''.join(encoded[75:]);print('map tiles',len(counts),len(bank),'merged placements',changes,'map',len(world_first),len(world_tail))
''' + s[z:]
s=s.replace('assert len(world_tail)<=2700;data(\'world_tail\',world_tail.ljust(2700', 'assert len(world_tail)<=1300;data(\'world_tail\',world_tail.ljust(1300')
s=s.replace("zero('head');lh(WORLD);shm('world_ptr')", "zero('head');lh(WORLD+4096);shm('world_ptr')")
a=s.index("R('ld b,3');L('decode_group')");z=s.index("# Additional game routines",a)
s=s[:a]+'''# Decode one tile scanline; map pointer advances only after eight lines.
la('remaining');andi(7);R('add a,a');add(WORLD>>8);X('exx',0xd9);R('ld b,a');X('exx',0xd9)
R('ld b,3');L('decode_group');R('push bc','ld c,(hl)','inc hl','ld b,8');L('decode_byte');R('ld a,c','rlca','ld c,a','ld a,(hl)','inc hl');X('exx',0xd9);R('ld l,a','ld h,b');J('decode_low','nc');R('inc h');L('decode_low');R('ld a,(hl)');X('exx',0xd9);R('ld (de),a','inc de','dec b');J('decode_byte','nz');R('pop bc','dec b');J('decode_group','nz')
la('remaining');andi(7);J('world_continue','nz');shm('world_ptr');de_m('world_limit');R('or a','sbc hl,de');J('world_continue','nz');lh('world_tail');shm('world_ptr');L('world_continue');lhm('src_start');R('ld e,l','ld a,h');add((CLEAN-BUF)>>8);R('ld d,a');lc(24);R('ldir');ret()
''' + s[z:]
p.write_text(s)
