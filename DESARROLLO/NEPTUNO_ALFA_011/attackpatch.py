from pathlib import Path
p=Path('attack.py');s=p.read_text();a=s.index("L('enemy_attack')");z=s.index('# Low cost destruction sound',a)
s=s[:a]+'''# Fire selection every 16 ticks: rotate fairly over slots. Ground targets get aimed fire.
L('enemy_attack');la('boss');cp(2);J('boss_attack','z');R('or a');ret('nz');la('tick');andi(15);ret('nz');la('tick');R('rrca','rrca','rrca','rrca');andi(3);R('ld c,a','ld b,0');lh('e0_wait');R('add hl,bc','ld a,(hl)','or a');ret('nz');R('ld a,c','add a,a','ld c,a');lh('e0');R('add hl,bc','ld c,(hl)','inc hl','ld a,(hl)');cp(172);ret('nc');add(8);R('ld b,a','ld a,c');add(7);R('ld c,a');J('fire_aim')
# Boss pattern thresholds are loaded with each phase. Distinct batteries and progressively faster cadence.
L('boss_attack');la('boss_hp');R('ld b,a');lh('boss_thresholds');R('ld a,b');X('cp (hl)',0xbe);J('boss_front','nc');R('inc hl');X('cp (hl)',0xbe);J('boss_fan','nc');R('inc hl');X('cp (hl)',0xbe);J('boss_medium','nc');J('boss_fast')
L('boss_front');la('tick');andi(31);ret('nz');la('phase_id');cp(1);J('boss_front_pair','z');la('tick');andi(32);J('boss_front_right','nz');R('ld c,52');J('boss_front_launch');L('boss_front_right');R('ld c,132');L('boss_front_launch');R('ld b,136','xor a');J('fire_enemy');L('boss_front_pair');R('ld b,140','ld c,48','xor a');C('fire_enemy');R('ld b,140','ld c,136','xor a');J('fire_enemy')
L('boss_fan');la('tick');andi(31);ret('nz');R('ld b,136','ld c,48');imm(1);C('fire_enemy');R('ld b,136','ld c,136');imm(255);J('fire_enemy')
L('boss_medium');la('tick');andi(15);ret('nz');la('phase_id');cp(3);J('boss_sweep','c');la('tick');andi(32);J('boss_sweep_right','nz');R('ld b,132','ld c,48');J('fire_aim');L('boss_sweep_right');R('ld b,132','ld c,136');J('fire_aim');L('boss_sweep');la('tick');andi(112);add(32);R('ld c,a','ld b,136','xor a');J('fire_enemy')
L('boss_fast');la('tick');andi(7);ret('nz');la('tick');andi(16);J('boss_fast_right','nz');R('ld c,52');J('boss_fast_launch');L('boss_fast_right');R('ld c,132');L('boss_fast_launch');R('ld b,136');J('fire_aim')
# Aimed projectiles sample player position once, never home after firing.
# Quantized slope, horizontal and vertical, including upward fire from ground troops.
data('launch_dy',[2]);data('aim_dx',[0]);data('aim_abs_y',[0]);data('aim_abs_x',[0]);data('aim_sx',[0]);data('aim_sy',[0]);data('attack_phase',[0])
L('fire_aim');la('player_y');add(6);R('sub b');J('aim_y_up','c');sa('aim_abs_y');setv('aim_sy',1);J('aim_x');L('aim_y_up');X('cpl',0x2f);R('inc a');sa('aim_abs_y');setv('aim_sy',255)
L('aim_x');la('player');add(6);X('sub c',0x91);J('aim_x_left','c');sa('aim_abs_x');setv('aim_sx',1);J('aim_ratio');L('aim_x_left');X('cpl',0x2f);R('inc a');sa('aim_abs_x');setv('aim_sx',255)
L('aim_ratio');la('aim_abs_y');R('ld d,a');la('aim_abs_x');X('cp d',0xba);J('aim_horizontal','nc');la('aim_sy');R('add a,a');sa('launch_dy');la('aim_abs_x');R('add a,a');J('aim_vertical_diag','c');X('cp d',0xba);J('aim_zero_x','c');L('aim_vertical_diag');la('aim_sx');J('fire_ready');L('aim_zero_x');R('xor a');J('fire_ready')
L('aim_horizontal');R('ld d,a');la('aim_sx');R('add a,a');sa('aim_dx');la('aim_abs_y');R('add a,a');J('aim_horizontal_diag','c');X('cp d',0xba);J('aim_zero_y','c');L('aim_horizontal_diag');la('aim_sy');J('aim_store_y');L('aim_zero_y');R('xor a');L('aim_store_y');sa('launch_dy');la('aim_dx');J('fire_ready')
L('fire_enemy');R('push af');setv('launch_dy',2);R('pop af');L('fire_ready');R('push af');la('b0_y');cp(255);J('fire_b0','z');la('b1_y');cp(255);J('fire_b1','z');R('pop af');ret()
for j in range(2):
 n=f'b{j}';L(f'fire_b{j}');R('ld a,b');sa(n+'_y');R('ld a,c');sa(n);R('pop af');sa(n+'_dx');copyv('launch_dy',n+'_dy');ret()
''' + s[z:];s=s[:s.index('# Rodas II:')];p.write_text(s)
# fix ground draw orientation based unsigned compare rather than signed wrap, and avoid draw clipping on inactive.
p=Path('enemy_draw.py');s=p.read_text().replace("la('player');R('sub c');add(8);cp(17);J('draw_enemy_go','c');bit(7);lh('turret_r_ptr');J('draw_enemy_go','z');lh('turret_l_ptr')", "la('player');R('sub c');J('turret_left','c');cp(9);J('draw_enemy_go','c');lh('turret_r_ptr');J('draw_enemy_go');L('turret_left');cp(248);J('draw_enemy_go','nc');lh('turret_l_ptr')");p.write_text(s)
p=Path('wave_motion.py');s=p.read_text().replace("cp(96);J('enemy_exit'","cp(89);J('enemy_exit'");p.write_text(s)
p=Path('waves.py');s=p.read_text().replace('delays=(0,8,16,24)','delays=(0,6,12,18)');p.write_text(s)
# support extra opcodes in native simulator
p=Path('test_cpu.py');s=p.read_text().replace("if o in (7,15):", "if o==0x2f:self.r[7]^=255;return\n  if o in (7,15):").replace('0xd9,0x37,0x00','0xd9,0x37,0x2f,0x00');p.write_text(s)
# Flow: final screen loaded on tape (after stage5), generic intermediate, phase digit all five.
p=Path('flow.py');s=p.read_text();a=s.index("L('end_game')");z=s.index("L('wait_press')",a)
s=s[:a]+'''L('end_game');la('game_state');cp(1);J('end_win','nz');lh('over_scr');J('show_end');L('end_win');la('phase_id');cp(5);J('end_final','z');lh('clear_scr');L('show_end');C('unpack');C('hold_three');C('wait_press');la('game_state');cp(2);J('title','nz');setv('carrying',1);C('load_level');J('load_failed','nc');C('init_level');J('main')
# Final artwork is a separate normal CODE block on tape. Do not enter ROM with SPACE held.
L('end_final');lh('clear_scr');C('unpack');C('hold_three');C('wait_press');ixload('title_header');ld(17);R('xor a');C('load_raw');J('load_failed','nc');X('ld ix,$4000',0xdd,0x21,0,0x40);ld(6912);imm(255);C('load_raw');J('load_failed','nc');R('xor a');X('out ($fe),a',0xd3,0xfe);C('hold_three');C('wait_press');J('title')
L('hold_three');R('ld b,150');L('end_wait');R('halt','dec b');J('end_wait','nz');ret()
''' + s[z:];# final requested FASE5 only final, not intermediate: wait release then load artwork directly (no generic display) after destruction.
s=s.replace("L('end_final');lh('clear_scr');C('unpack');C('hold_three');C('wait_press');", "L('end_final');C('wait_release_final');")
s=s.replace("L('hold_three');", "L('wait_release_final');R('ld d,8');L('final_release_loop');R('halt');C('keys');la('fire');R('or a');J('wait_release_final','nz');X('dec d',0x15);J('final_release_loop','nz');ret()\nL('hold_three');")
a=s.index("L('hud_init_phase')");z=s.index("L('title_header')",a)
s=s[:a]+'''L('hud_init_phase');la('phase_id');cp(1);ret('z');R('dec a','dec a','ld l,a','ld h,0','add hl,hl','add hl,hl','add hl,hl');ld('phase_digits');R('add hl,de');ld('phase_digit_dest');R('ld b,7');L('phase_digit_loop');R('push bc','ld a,(de)','ld c,a','inc de','ld a,(de)','ld b,a','inc de','ld a,(hl)','inc hl');X('ld (bc),a',0x02);R('pop bc','dec b');J('phase_digit_loop','nz');ret()
data('phase_digits',[14,2,2,14,8,8,14,0,14,2,2,14,2,2,14,0,10,10,10,14,2,2,2,0,14,8,8,14,2,2,14,0]);tabwords('phase_digit_dest',[attr(y)+24+5 for y in range(168,175)])
''' + s[z:];p.write_text(s)
# Pack campaign and direct test TAPs for all phases; retain common code layout.
p=Path('pack.py');s=p.read_text().replace('for i in (1,2):','for i in range(1,6):');a=s.index("s1=json.loads");z=s.index('def block',a)
s=s[:a]+'''s1=json.loads((P/'symbols1.json').read_text());ks=[(P/f'kernel{i}.bin').read_bytes() for i in range(1,6)];k1=ks[0];x,y=[s1[s]-0x6000 for s in ('overlay_start','overlay_end')]
for i,k in enumerate(ks,1):
 assert s1==json.loads((P/f'symbols{i}.json').read_text()),i
 assert k1[:x]==k[:x] and k1[y:]==k[y:],i
k=k1[:x]+bytes(y-x)+k1[y:];k,asm,guard_labels=guard(k,s1);(P/'kernel.bin').write_bytes(k);(P/'tape_guard.asm').write_text(asm);(P/'symbols.json').write_text(json.dumps({**s1,**guard_labels},indent=2))
for i,ki in enumerate(ks,1):(P/f'overlay{i}.bin').write_bytes(ki[x:y])
''' + s[z:];a=s.index('for name,data in ');z=s.index(' (P/name)',a)
s=s[:a]+'''for i,name in enumerate(['NEPTUNO_ATACA_008.tap','NEPTUNO_ATACA_GRECIA_008.tap','NEPTUNO_ATACA_SIRIA_008.tap','NEPTUNO_ATACA_FRANCIA_008.tap','NEPTUNO_ATACA_BARCELONA_008.tap'],1):
 data=prefix+header(3,'INICIO',y-x,s1['overlay_start'],0)+phase(i)+screen('TITULO','TITULO.scr')+b''.join(phase(j) for j in range(i+1,6))+screen('FINAL','FINAL_FASE5.scr')
''' + s[z:];p.write_text(s)
p=Path('test_cpu.py');s=p.read_text().replace("('NEPTUNO_ATACA_007.tap' if level==1 else 'NEPTUNO_ATACA_GRECIA_007.tap')", "(['NEPTUNO_ATACA_008.tap','NEPTUNO_ATACA_GRECIA_008.tap','NEPTUNO_ATACA_SIRIA_008.tap','NEPTUNO_ATACA_FRANCIA_008.tap','NEPTUNO_ATACA_BARCELONA_008.tap'][level-1])");p.write_text(s)
