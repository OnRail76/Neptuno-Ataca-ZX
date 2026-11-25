# Four aim directions, selected from player position; retain native aligned graphics.
# x/y at BC. All ground lanes are byte-aligned, so an 8-entry shift table is unnecessary.
for name,addr in [('soldier_down',0xfde0),('soldier_left',0xf940),('soldier_right',0xf9a0),('soldier_up',0xfa00),('tank_down',0xfe40),('tank_left',0xff00),('tank_right',0xff30),('tank_up',0xfe70),('turret_down',0xf8e0),('turret_left_frame',0xfea0),('turret_right_frame',0xfed0),('turret_up',0xf910)]:
 tabwords(name,[addr]*8)
# Use compact pointer tables to select an existing shift table; soldier animation uses alternate table.
for n,frames in [('soldier_dirs',['soldier_down','soldier_left','soldier_right','soldier_up']),('tank_dirs',['tank_down','tank_left','tank_right','tank_up']),('turret_dirs',['turret_down','turret_left_frame','turret_right_frame','turret_up'])]:
 L(n)
 for frame in frames:DW(frame)
for n,addr in [('soldier_down_anim',0xfe10),('soldier_left_anim',0xf970),('soldier_right_anim',0xf9d0),('soldier_up_anim',0xfa30)]:tabwords(n,[addr]*8)
L('soldier_anim_dirs')
for n in ['soldier_down_anim','soldier_left_anim','soldier_right_anim','soldier_up_anim']:DW(n)
L('draw_enemy_type');R('ld d,a','ld a,b');cp(192);ret('nc');R('ld a,d');lh('drone_ptr');R('or a');J('draw_enemy_go','z');lh('fighter_ptr');cp(1);J('draw_enemy_go','z');lh('turret_dirs');cp(2);J('ground_direction','z');lh('tank_dirs');cp(4);J('ground_direction','z');lh('soldier_dirs');la('tick');andi(8);J('ground_direction','z');lh('soldier_anim_dirs')
# Choose horizontal when |dx| >= |dy|; else aim up/down. Preserve BC and direction table.
L('ground_direction');R('push bc','push hl');la('player');R('sub c','ld d,2');J('aim_draw_dx','nc');X('cpl',0x2f);R('inc a','ld d,1');L('aim_draw_dx');R('ld e,a');la('player_y');R('sub b','ld h,0');J('aim_draw_dy','nc');X('cpl',0x2f);R('inc a','ld h,3');L('aim_draw_dy');X('cp e',0xbb);R('ld a,d');J('aim_draw_index','c');R('ld a,h');L('aim_draw_index');R('add a,a','ld e,a','ld d,0','pop hl','add hl,de','ld e,(hl)','inc hl','ld d,(hl)','ex de,hl','pop bc');L('draw_enemy_go');imm(16);J('draw_or')
# Ground movement and HP initialization in spare resident low memory.
L('spawn_ground_hp');ixget(0);cp(3);ret('c');imm(2);J('spawn_hp_set','z');imm(3);L('spawn_hp_set');ixput(3);ret()
L('enemy_ground_advance');R('inc hl','ld a,(hl)','inc a','ld b,a');ixget(0);cp(3);J('ground_store','nz');la('tick');andi(3);J('ground_store','nz');R('inc b');L('ground_store');R('ld a,b');cp(192);J('enemy_y_store','c');imm(255);J('enemy_y_store')
