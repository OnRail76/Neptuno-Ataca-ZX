# HL points to x, DE scheduled entry, IX four private movement bytes.
L('step_enemy');R('inc hl','ld a,(hl)','dec hl');cp(255);J('enemy_active','nz');la('wave');cp(10);ret('nc');R('ld a,(de)','ld b,a','inc de','ld a,(de)','ld c,a');la('wave_clock');R('cp c');ret('nz');R('ld a,b','ld (hl),a');ixput(3);R('inc hl');X('ld (hl),0',0x36,0);R('inc de','ld a,(de)');ixput(1);R('inc de','ld a,(de)');ixput(0);R('xor a');ixput(2);J('spawn_ground_hp')
L('enemy_active');ixget(1);cp(8);J('enemy_ground_advance','z');cp(6);J('enemy_air','nz');la('tick');andi(1);ret('nz');R('inc hl','ld a,(hl)','inc a');cp(192);J('enemy_y_store','c');imm(255);J('enemy_y_store')
L('enemy_air');ixget(2);R('inc a');ixput(2);R('ld b,a');ixget(1);cp(4);J('enemy_incursion','z');R('ld a,b');cp(89);J('enemy_exit','nc');R('add a,a','inc hl','ld (hl),a','dec hl');ixget(1);R('or a');ret('z');cp(1);J('enemy_sine','z');cp(5);J('enemy_swarm','z');cp(7);J('enemy_diagonal','z');# pincer
R('ld a,b');cp(48);ret('nc');ixget(1);cp(2);J('enemy_right','z');J('enemy_left')
L('enemy_diagonal');R('ld a,b');cp(80);ret('nc');J('enemy_right')
L('enemy_sine');R('ld a,b');andi(63);R('push hl','ld l,a','ld h,0');ld('sine_table');R('add hl,de','ld b,(hl)');ixget(3);R('add a,b','pop hl','ld (hl),a');ret()
L('enemy_swarm');la('player');R('cp (hl)') if False else X('cp (hl)',0xbe);ret('z');J('enemy_left','c');L('enemy_right');R('ld a,(hl)');cp(168);ret('nc');R('inc a','ld (hl),a');ret();L('enemy_left');R('ld a,(hl)','or a');ret('z');R('dec a','ld (hl),a');ret()
# Descend to y=64, hold for 16 ticks, then reverse smoothly.
L('enemy_incursion');R('ld a,b');cp(33);J('inc_down','c');cp(49);J('inc_hold','c');cp(81);J('enemy_exit','nc');R('ld b,a');imm(80);R('sub b');J('inc_down');L('inc_hold');cp(36);ret('nz');R('ld a,(hl)');add(7);R('ld c,a','ld b,80');J('fire_aim');L('inc_down');R('add a,a','inc hl');L('enemy_y_store');R('ld (hl),a');ret();L('enemy_exit');R('inc hl');X('ld (hl),255',0x36,255);ret()
# Native draw selection. Sprite renderer itself is unchanged.
L('draw_burst');R('push af','ld a,b');cp(177);J('burst_skip','nc');add(4);R('ld b,a','ld a,c');add(4);R('ld c,a','pop af');andi(8);lh('expl_ptr');J('burst_go','nz');lh('expl2_ptr');L('burst_go');imm(8);J('draw_or');L('burst_skip');R('pop af');ret()
