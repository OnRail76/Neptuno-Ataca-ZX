from pathlib import Path
p=Path('attack.py');s=p.read_text();a=s.index("data('launch_dy'");z=s.index('# Low cost destruction sound',a)
s=s[:a]+'''data('launch_dy',[2]);data('launch_major',[0]);data('launch_minor',[0]);data('launch_sign',[0]);data('launch_axis',[0]);data('aim_abs_y',[0]);data('aim_abs_x',[0]);data('aim_sx',[0]);data('aim_sy',[0])
L('fire_aim');la('player_y');add(6);R('sub b');J('aim_y_up','c');sa('aim_abs_y');setv('aim_sy',1);J('aim_x');L('aim_y_up');X('cpl',0x2f);R('inc a');sa('aim_abs_y');setv('aim_sy',255)
L('aim_x');la('player');add(6);X('sub c',0x91);J('aim_x_left','c');sa('aim_abs_x');setv('aim_sx',1);J('aim_ratio');L('aim_x_left');X('cpl',0x2f);R('inc a');sa('aim_abs_x');setv('aim_sx',255)
# Bresenham/DDA: capture a true vector, then integrate at two major-axis pixels per tick.
L('aim_ratio');la('aim_abs_y');R('ld d,a');la('aim_abs_x');X('cp d',0xba);J('aim_horizontal','nc');sa('launch_minor');R('ld a,d');sa('launch_major');la('aim_sy');R('add a,a');sa('launch_dy');la('aim_sx');sa('launch_sign');zero('launch_axis');R('xor a');J('fire_ready')
L('aim_horizontal');sa('launch_major');R('ld a,d');sa('launch_minor');zero('launch_dy');la('aim_sy');sa('launch_sign');setv('launch_axis',1);la('aim_sx');R('add a,a');J('fire_ready')
L('fire_enemy');R('push af');setv('launch_dy',2);zero('launch_major');R('pop af');L('fire_ready');R('push af');la('b0_y');cp(255);J('fire_b0','z');la('b1_y');cp(255);J('fire_b1','z');R('pop af');ret()
for j in range(2):
 n=f'b{j}';L(f'fire_b{j}');R('ld a,b');sa(n+'_y');R('ld a,c');sa(n);R('pop af');sa(n+'_dx');lh('launch_dy');ld(n+'_dy');lc(5);R('ldir');zero(n+'_err');ret()
# Signed movement with a 2-substep error accumulator; no homing after launch.
for j in range(2):
 n=f'b{j}';L('move_'+n);la(n+'_y');cp(255);ret('z');la(n+'_dx');R('ld h,a');la(n+'_dy');R('ld l,a');la(n+'_major');R('or a');J(n+'_move_fixed','z');R('ld c,a');la(n+'_minor');R('ld b,a');la(n+'_err');R('ld d,0')
 for k in range(2):
  R('add a,b');J(n+f'_take{k}','c');R('cp c');J(n+f'_no{k}','c');L(n+f'_take{k}');X('sub c',0x91);X('inc d',0x14);L(n+f'_no{k}')
 sa(n+'_err');R('ld a,d','or a');J(n+'_move_fixed','z');la(n+'_sign');cp(255);R('ld a,d');J(n+'_positive','nz');X('cpl',0x2f);R('inc a');L(n+'_positive');R('ld d,a');la(n+'_axis');R('or a','ld a,d');J(n+'_minor_y','nz');R('ld h,a');J(n+'_move_fixed');L(n+'_minor_y');R('ld l,a');L(n+'_move_fixed');la(n+'_y');X('add a,l',0x85);cp(189);J(n+'_off','nc');sa(n+'_y');la(n);X('add a,h',0x84);cp(176);J(n+'_off','nc');sa(n);ret();L(n+'_off');setv(n+'_y',255);ret()
''' + s[z:]
# progressive fire cadence; preserve stage 1 rhythm, stages 4-5 aim more often
s=s.replace("la('tick');andi(15);ret('nz');la('tick');R('rrca','rrca','rrca','rrca');andi(3);", "la('phase_id');cp(1);J('fire_regular','nz');la('tick');andi(31);ret('nz');la('tick');R('rrca','rrca','rrca','rrca','rrca');J('fire_slot');L('fire_regular');cp(4);J('fire_late','nc');la('tick');andi(15);ret('nz');la('tick');R('rrca','rrca','rrca','rrca');J('fire_slot');L('fire_late');la('tick');andi(7);ret('nz');la('tick');R('rrca','rrca','rrca');L('fire_slot');andi(3);")
# vary boss patterns by phase
s=s.replace("L('boss_front');la('tick');andi(31);ret('nz');la('phase_id');cp(1);J('boss_front_pair','z');", "L('boss_front');la('phase_id');cp(1);J('boss_front_other','nz');la('tick');andi(63);ret('nz');J('boss_front_pair');L('boss_front_other');la('tick');andi(31);ret('nz');la('phase_id');cp(4);J('boss_front_eiffel','z');cp(5);J('boss_front_throne','z');")
s=s.replace("L('boss_fan');la('tick');andi(31);ret('nz');", "L('boss_front_eiffel');R('ld b,134','ld c,72');imm(255);C('fire_enemy');R('ld b,134','ld c,112');imm(1);J('fire_enemy');L('boss_front_throne');R('ld b,132','ld c,92');J('fire_aim')\nL('boss_fan');la('tick');andi(31);ret('nz');la('phase_id');cp(5);J('boss_fan_aim','z');")
s=s.replace("L('boss_medium');", "L('boss_fan_aim');R('ld b,136','ld c,48');C('fire_aim');R('ld b,136','ld c,136');J('fire_aim')\nL('boss_medium');")
s=s.replace("la('phase_id');cp(3);J('boss_sweep','c');", "la('phase_id');cp(3);J('boss_sweep','c');cp(4);J('boss_sweep','z');")
s=s.replace("L('boss_fast');la('tick');andi(7);ret('nz');la('tick');andi(16);", "L('boss_fast');la('tick');andi(7);ret('nz');la('phase_id');cp(5);J('boss_fast_sides','nz');la('tick');andi(24);add(56);R('ld c,a','ld b,136');J('fire_aim');L('boss_fast_sides');la('tick');andi(16);")
p.write_text(s)
p=Path('waves.py');s=p.read_text().replace("for i in range(2):data(f'b{i}_dx',[0]);data(f'b{i}_dy',[2])", "for i in range(2):\n for name,val in [('dx',0),('dy',2),('major',0),('minor',0),('sign',0),('axis',0),('err',0)]:data(f'b{i}_{name}',[val])");p.write_text(s)
p=Path('build.py');s=p.read_text();a=s.index('# Enemy bullets with horizontal movement');z=s.index("C('enemy_attack')",a);s=s[:a]+"# DDA motion for two aimed enemy projectile slots.\nfor j in range(2):C(f'move_b{j}')\n"+s[z:];p.write_text(s)
# tanks in stages 4-5 survive one hit, then are marked damaged (type 5, same sprite family)
p=Path('game_logic.py');s=p.read_text();needle="X('ld (ix+0),12',0xdd,0x36,0,12);C('boom');";s=s.replace(needle,"la('phase_id');cp(4);J('enemy_kill','c');imm(4);X('sub d',0x92);R('add a,a','add a,a','ld l,a','ld h,0');ld('e0_state');R('add hl,de','ld a,(hl)');cp(4);J('enemy_kill','nz');X('ld (hl),5',0x36,5);C('consume_shot');C('beep');ret();L('enemy_kill');"+needle);p.write_text(s)
