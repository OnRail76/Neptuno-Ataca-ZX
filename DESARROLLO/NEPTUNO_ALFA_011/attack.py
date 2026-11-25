# Two enemy bullets: bounded cost, normal fire from alternating active enemies.
# Fire selection every 16 ticks: rotate fairly over slots. Ground targets get aimed fire.
L('enemy_attack');la('boss');cp(2);J('boss_attack','z');R('or a');ret('nz');la('phase_id');cp(1);J('fire_regular','nz');la('tick');andi(31);ret('nz');la('tick');R('rrca','rrca','rrca','rrca','rrca');J('fire_slot');L('fire_regular');cp(4);J('fire_late','nc');la('tick');andi(15);ret('nz');la('tick');R('rrca','rrca','rrca','rrca');J('fire_slot');L('fire_late');la('tick');andi(7);ret('nz');la('tick');R('rrca','rrca','rrca');L('fire_slot');R('push af');C('priority_fire');J('no_priority_fire','nc');R('pop af');ret();L('no_priority_fire');R('pop af');andi(3);R('ld c,a','ld b,0');lh('e0_wait');R('add hl,bc','ld a,(hl)','or a');ret('nz');R('ld a,c','add a,a','ld c,a');lh('e0');R('add hl,bc','ld c,(hl)','inc hl','ld a,(hl)');cp(172);ret('nc');add(8);R('ld b,a','ld a,c');add(7);R('ld c,a');J('fire_aim')
# Prioritize a ground unit that has not yet fired, only when a ball slot is free.
L('priority_fire');la('b0_y');cp(255);J('priority_scan','z');la('b1_y');cp(255);J('priority_none','nz');L('priority_scan')
for j in range(4):
 n=f'e{j}';nextn=f'priority_next{j}';la(n+'_type');cp(2);J(nextn,'c');la(n+'_age');R('or a');J(nextn,'nz');la(n+'_wait');R('or a');J(nextn,'nz');la(n+'_y');cp(172);J(nextn,'nc');add(8);R('ld b,a');la(n);add(7);R('ld c,a');setv(n+'_age',1);C('fire_aim');X('scf',0x37);ret();L(nextn)
L('priority_none');R('or a');ret()
# Boss pattern thresholds are loaded with each phase. Distinct batteries and progressively faster cadence.
L('boss_attack');la('boss_hp');R('ld b,a');lh('boss_thresholds');R('ld a,b');X('cp (hl)',0xbe);J('boss_front','nc');R('inc hl');X('cp (hl)',0xbe);J('boss_fan','nc');R('inc hl');X('cp (hl)',0xbe);J('boss_medium','nc');J('boss_fast')
L('boss_front');la('phase_id');cp(1);J('boss_front_other','nz');la('tick');andi(63);ret('nz');J('boss_front_pair');L('boss_front_other');la('tick');andi(31);ret('nz');la('phase_id');cp(4);J('boss_front_eiffel','z');cp(5);J('boss_front_throne','z');la('tick');andi(32);J('boss_front_right','nz');R('ld c,52');J('boss_front_launch');L('boss_front_right');R('ld c,132');L('boss_front_launch');R('ld b,136','xor a');J('fire_enemy');L('boss_front_pair');R('ld b,140','ld c,48','xor a');C('fire_enemy');R('ld b,140','ld c,136','xor a');J('fire_enemy')
L('boss_front_eiffel');R('ld b,134','ld c,72');imm(255);C('fire_enemy');R('ld b,134','ld c,112');imm(1);J('fire_enemy');L('boss_front_throne');R('ld b,132','ld c,92');J('fire_aim')
L('boss_fan');la('tick');andi(31);ret('nz');la('phase_id');cp(5);J('boss_fan_aim','z');R('ld b,136','ld c,48');imm(1);C('fire_enemy');R('ld b,136','ld c,136');imm(255);J('fire_enemy')
L('boss_fan_aim');R('ld b,136','ld c,48');C('fire_aim');R('ld b,136','ld c,136');J('fire_aim')
L('boss_medium');la('tick');andi(15);ret('nz');la('phase_id');cp(3);J('boss_sweep','c');cp(4);J('boss_sweep','z');la('tick');andi(32);J('boss_sweep_right','nz');R('ld b,132','ld c,48');J('fire_aim');L('boss_sweep_right');R('ld b,132','ld c,136');J('fire_aim');L('boss_sweep');la('tick');andi(112);add(32);R('ld c,a','ld b,136','xor a');J('fire_enemy')
L('boss_fast');la('tick');andi(7);ret('nz');la('phase_id');cp(5);J('boss_fast_sides','nz');la('tick');andi(24);add(56);R('ld c,a','ld b,136');J('fire_aim');L('boss_fast_sides');la('tick');andi(16);J('boss_fast_right','nz');R('ld c,52');J('boss_fast_launch');L('boss_fast_right');R('ld c,132');L('boss_fast_launch');R('ld b,136');J('fire_aim')
# Aimed projectiles sample player position once, never home after firing.
# Quantized slope, horizontal and vertical, including upward fire from ground troops.
data('launch_dy',[2]);data('launch_major',[0]);data('launch_minor',[0]);data('launch_sign',[0]);data('launch_axis',[0]);data('aim_abs_y',[0]);data('aim_abs_x',[0]);data('aim_sx',[0]);data('aim_sy',[0])
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
# During boss destruction the background is modified only AFTER restore_snapshot.
# Erode two native scanlines each presentation. No erase of visible VRAM.
L('boss_decay');la('boss_hp');R('or a');J('boss_done','z');andi(7);J('boss_decay_quiet','nz');C('sfx_boss');L('boss_decay_quiet');C('boss_clear_row');C('boss_clear_row');la('boss_hp');sa('powerup_y');andi(112);add(32);sa('powerup');ret()
L('boss_clear_row');decv('boss_hp');la('boss_hp');R('ld b,a','ld c,0');C('ring_addr');R('ld e,l','ld a,h');add((CLEAN-BUF)>>8);R('ld d,a','ld b,24','xor a');L('boss_clear_loop');R('ld (hl),a','ld (de),a','inc hl','inc de','dec b');J('boss_clear_loop','nz');ret()
L('boss_done');setv('game_state',2);ret()

