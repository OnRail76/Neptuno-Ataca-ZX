# Additional game routines, same emitter / CPU as BENCH01.
# Fast box test: signed modular distance, compare top-left coordinates.
def near(a,bv,offset,limit,fail):
 la(bv);R('ld b,a');la(a);R('sub b');add(offset);cp(limit);J(fail,'nc')
L('power_collision');near('powerup','player',12,25,'power_miss');near('powerup_y','player_y',12,25,'power_miss');setv('powerup_y',255);lh(500);shm('spread_lo');C('sfx_power');L('power_miss');ret()
L('collisions');la('death');R('or a');ret('nz');la('cheat_on');R('or a');J('skip_player_hits','nz');la('invul');R('or a');J('skip_player_hits','nz')
# air and boat collision loop, then enemy bullets
bc_m('player');lh('e0');W('ld ix,e0_wait',0x00,0) if False else None;X('ld ix,e0_wait',0xdd,0x21,0,0);fix.append((len(b)-2,'e0_wait'));R('ld d,4');L('player_hit_loop');R('ld a,(ix+0)','or a');J('player_hit_dead','nz');R('inc hl','ld a,(hl)');cp(255);J('player_hit_next','z');R('sub b');add(12);cp(25);J('player_hit_next','nc');R('dec hl','ld a,(hl)','inc hl');X('sub c',0x91);add(12);cp(25);J('player_hit_next','nc');C('lose_life');ret();L('player_hit_dead');R('inc hl');L('player_hit_next');R('inc hl','inc ix');X('dec d',0x15);J('player_hit_loop','nz')
for n in ['b0','b1']:
 fail='phmiss_'+n;la(n+'_y');cp(255);J(fail,'z');near(n+'_y','player_y',3,18,fail);near(n,'player',3,18,fail);C('lose_life');ret();L(fail)
L('skip_player_hits')
# 6 bullets vs four enemies, subroutines per enemy avoid huge unrolled code. Coordinates in temp BC, save shot index via pointer.
for j in range(6):
 n=f's{j}';la(n+'_y');cp(255);J('shmiss'+str(j),'z');bc_m(n);lh(n);shm('shot_ptr');C('shot_hit');L('shmiss'+str(j))
ret()
L('shot_hit');la('game_state');R('or a');ret('nz');la('boss');cp(2);J('normal_hits','nz');R('ld a,b');cp(144);ret('nc');R('ld a,b','push bc');la('phase_id');cp(2);J('boss_hit_height','nz');R('ld a,b');cp(40);J('boss_hit_miss','c');L('boss_hit_height');R('pop bc');J('boss_hit_x');L('boss_hit_miss');R('pop bc');ret();L('boss_hit_x');R('ld a,c');cp(24);ret('c');cp(168);ret('nc');C('consume_shot');decv('boss_hp');C('sfx_hit');C('score_add');la('boss_hp');R('or a');ret('nz');setv('boss',3);C('sfx_boss');setv('boss_hp',144);setv('b0_y',255);setv('b1_y',255);setv('powerup_y',255)
for j in range(6):setv(f's{j}_y',255)
ret()
L('normal_hits');la('boss');R('or a');ret('nz')
# loop over four contiguous enemy records, keep shot BC
lh('e0');X('ld ix,e0_wait',0xdd,0x21,0,0);fix.append((len(b)-2,'e0_wait'));R('ld d,4');L('enemy_hit_loop');R('ld a,(ix+0)','or a');J('enemy_hit_dead','nz');R('inc hl','ld a,(hl)');cp(255);J('enemy_hit_next','z');R('sub b');add(15);cp(19);J('enemy_hit_next','nc');R('dec hl','ld a,(hl)','inc hl');X('sub c',0x91);add(15);cp(17);J('enemy_hit_next','nc');R('ld a,(hl)');sa('hit_y');R('dec hl','ld a,(hl)');sa('hit_x')
imm(4);X('sub d',0x92);R('add a,a','add a,a','ld l,a','ld h,0');ld('e0_state');R('add hl,de','ld a,(hl)');cp(3);J('enemy_kill_light','c');R('inc hl','inc hl','inc hl','ld a,(hl)');cp(2);J('enemy_kill_heavy','c');R('dec a','ld (hl),a');C('consume_shot');C('sfx_hit');ret();L('enemy_kill_light');C('boom');J('enemy_kill');L('enemy_kill_heavy');C('sfx_heavy');L('enemy_kill');X('ld (ix+0),12',0xdd,0x36,0,12);C('consume_shot');C('score_add');incv('kills');la('kills');cp(3);ret('c');zero('kills');la('powerup_y');cp(255);ret('nz');copyv('hit_x','powerup');copyv('hit_y','powerup_y');ret()
L('enemy_hit_dead');R('inc hl');L('enemy_hit_next');R('inc hl','inc ix');X('dec d',0x15);J('enemy_hit_loop','nz');ret()
L('consume_shot');lhm('shot_ptr');R('inc hl');X('ld (hl),255',0x36,255);ret()
L('lose_life');C('sfx_death');decv('lives');setv('death',1);setv('death_timer',40);lh(0);shm('spread_lo');setv('powerup_y',255);setv('b0_y',255);setv('b1_y',255);setv('life_dirty',1)
for j in range(6):setv(f's{j}_y',255)
ret()
L('score_add');setv('dirty',4)
for j in (3,2,1,0):
 incv(f'score{j}');la(f'score{j}');cp(10);ret('c');zero(f'score{j}')
ret()
# update score and lives only when changed. Bitmap only. Digits 5x7 doubled vertically.
L('hud_update');la('life_dirty');R('or a');J('hud_score','z');zero('life_dirty');J('hud_lives')
L('hud_score');la('dirty');R('or a');ret('z');R('dec a');sa('dirty');R('ld l,a','ld h,0');ld('score0');R('add hl,de','ld a,(hl)','ld l,a','ld h,0','add hl,hl','add hl,hl','add hl,hl','add hl,hl');ld('digits');R('add hl,de','push hl');la('dirty');R('ld l,a','ld h,0','add hl,hl','add hl,hl','add hl,hl','add hl,hl','add hl,hl');ld('hud_score_dest0');R('add hl,de','ex de,hl','pop hl');J('hud_digit')
L('hud_lives');
# Only clear the lost icon, once, using a compact table of addresses and masks.
la('lives');cp(3);ret('nc');R('ld l,a','ld h,0','add hl,hl');ld('life_tables');R('add hl,de','ld e,(hl)','inc hl','ld d,(hl)','ex de,hl','ld e,16');L('life_wipe');R('ld c,(hl)','inc hl','ld b,(hl)','inc hl');X('ld a,(bc)',0x0a);X('and (hl)',0xa6);X('ld (bc),a',0x02);R('inc hl');X('dec e',0x1d);J('life_wipe','nz');ret()
labels['life_tables']=0xc612
extra_phase[0xc612]=b''.join(struct.pack('<H',0xc618+j*48) for j in range(3))
for j,x in enumerate((13,28,43)):
 vals=[]
 for y in range(140,148):
  for col in range(x//8,(x+6)//8+1):
   mask=255
   for xx in range(x,x+7):
    if xx//8==col:mask &= ~(128>>(xx&7))
   vals.extend(struct.pack('<H',attr(y)+24+col));vals.append(mask)
 assert len(vals)==48;labels['life_table'+str(j)]=0xc618+j*48;extra_phase[0xc618+j*48]=bytes(vals)
# DE pointer to list of destination words, HL digit source. 16 lines.
L('hud_digit');R('ld b,16')
# store table pointer, simple source -> target addressing
L('hud_digit_loop')
# table in DE, source HL: save source on stack, get destination in BC, then write using A and BC
R('push bc');R('ld a,(de)','ld c,a','inc de','ld a,(de)','ld b,a','inc de','ld a,(hl)','inc hl');X('ld (bc),a',0x02);R('pop bc','dec b');J('hud_digit_loop','nz');ret()
L('unpack');ld(0x4000);L('unpack_to');L('unpack_next');R('ld a,(hl)','inc hl','or a');ret('z');bit(7);J('unpack_run','nz');R('ld b,0','ld c,a','ldir');J('unpack_next')
L('unpack_run');bit(6);J('unpack_lz','nz');andi(63);add(3);R('ld b,a','ld a,(hl)','inc hl');L('unpack_repeat');R('ld (de),a','inc de','dec b');J('unpack_repeat','nz');J('unpack_next')
L('unpack_lz');andi(63);add(3);R('push af','ld c,(hl)','inc hl','ld b,(hl)','inc hl','push hl','push de','pop hl','or a');X('sbc hl,bc',0xed,0x42);R('pop bc','pop af','push bc','ld c,a','ld b,0','ldir','pop hl');J('unpack_next')
# Small tables and state. Keep the format native.
data('shot_ptr',[0,0]);data('hit_x',[0]);data('hit_y',[0])
font=['01110/11011/11011/11011/11011/11011/01110','00100/01100/00100/00100/00100/00100/01110','01110/11011/00011/00110/01100/11000/11111','11110/00011/00011/01110/00011/00011/11110','11011/11011/11011/11111/00011/00011/00011','11111/11000/11000/11110/00011/00011/11110','01110/11000/11000/11110/11011/11011/01110','11111/00011/00110/00110/01100/01100/01100','01110/11011/11011/01110/11011/11011/01110','01110/11011/11011/01111/00011/00011/01110']
data('digits',bytes(v for glyph in font for v in ([int(row,2)<<2 for row in glyph.split('/') for _ in range(2)]+[0,0])))
for j in range(4):labels['hud_score_dest'+str(j)]=0x7e70+j*32
