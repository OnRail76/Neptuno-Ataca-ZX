# Common flow. Only level parameters and wave data are replaced by tape.
data('cheat_on',[0]);data('cheat_steps',[0]);data('down_latch',[0]);data('fire_latch',[0]);data('carrying',[0])
L('boot');R('di');W('ld sp,$9000',0x31,STACK);R('im 1');X('ld iy,$5c3a',0xfd,0x21,0x3a,0x5c);R('ei');J('title')
# Flag in A, destination IX, byte count DE. ROM carry is preserved across IM2 restore.
L('load_raw');R('di','im 1');X('ld iy,$5c3a',0xfd,0x21,0x3a,0x5c);R('ei');X('scf',0x37);W('call $0556',0xcd,0x0556);R('di','push af');imm(0x7f);X('ld i,a',0xed,0x47);X('im 2',0xed,0x5e);R('pop af','ei');ret()
# Named INICIO header allows rewinding to start of tape (or directly to INICIO).
# Load the full initial phase before showing the interactive title.
L('title');zero('cheat_on');zero('cheat_steps');zero('down_latch');setv('fire_latch',1);zero('carrying')
L('start_seek');ixload('title_header');ld(17);R('xor a');C('load_raw');J('start_seek','nc');la('title_header');cp(3);J('start_seek','nz');la('title_header_name');cp(ord('I'));J('start_seek','nz');la('title_header_name2');cp(ord('N'));J('start_seek','nz');C('load_level');J('load_failed','nc')
L('title_seek');ixload('title_header');ld(17);R('xor a');C('load_raw');J('title_seek','nc');la('title_header');cp(3);J('title_seek','nz');la('title_header_name');cp(ord('T'));J('title_seek','nz');la('title_header_name2');cp(ord('I'));J('title_seek','nz');X('ld ix,$4000',0xdd,0x21,0,0x40);ld(6912);imm(255);C('load_raw');J('title_seek','nc');R('xor a');X('out ($fe),a',0xd3,0xfe)
lh('title_music');C('music_start');L('title_loop');R('halt');C('keys');C('title_input');J('title_begin','c');C('music_tick');J('title_loop');L('title_begin');C('music_stop');setv('lives',3)
for j in range(6):zero(f'score{j}')
C('init_level');J('main')
# Down must be pressed and released twice; holding down cannot count twice.
L('title_input');la('dy');cp(1);J('title_down','z');lc(31);R('in a,(c)');andi(228);cp(4);J('title_down','z');zero('down_latch');J('title_fire')
L('title_down');la('down_latch');R('or a');J('title_fire','nz');setv('down_latch',1);la('cheat_steps');cp(2);J('title_fire','nc');incv('cheat_steps')
L('title_fire');la('fire');R('or a');J('title_fire_down','nz');zero('fire_latch');R('or a');ret()
L('title_fire_down');la('fire_latch');R('or a');ret('nz');setv('fire_latch',1);la('cheat_steps');cp(2);J('title_start','nz');zero('cheat_steps');setv('cheat_on',1);C('music_stop');C('cheat_beep');R('or a');ret()
L('title_start');X('scf',0x37);ret()
# Audible confirmation (approx. 0.13 sec), only in title, never in play.
L('cheat_beep');R('ld b,90');L('cheat_period');imm(16);X('out ($fe),a',0xd3,0xfe);R('ld c,100');L('cheat_hi');R('dec c');J('cheat_hi','nz');R('xor a');X('out ($fe),a',0xd3,0xfe);R('ld c,100');L('cheat_lo');R('dec c');J('cheat_lo','nz');R('dec b');J('cheat_period','nz');ret()
# Two raw tape blocks per stage, resident code and title state do not change.
L('load_level');ixload('overlay_start');ld(labels['overlay_end']-labels['overlay_start']);imm(255);C('load_raw');ret('nc');X('ld ix,$a200',0xdd,0x21,0,0xa2);ld(0x10000-PHASE);imm(255);J('load_raw')
L('load_failed');imm(2);X('out ($fe),a',0xd3,0xfe);lh('over_scr');C('unpack');C('wait_press');J('title')
L('end_game');la('game_state');cp(1);J('end_win','nz');lh('over_scr');J('show_end');L('end_win');la('phase_id');cp(5);J('end_final','z');lh('clear_scr');L('show_end');C('unpack');C('hold_three');C('wait_press');la('game_state');cp(2);J('title','nz');setv('carrying',1);C('load_level');J('load_failed','nc');C('init_level');J('main')
# Final artwork is a separate normal CODE block on tape. Do not enter ROM with SPACE held.
L('end_final');C('wait_release_final');ixload('title_header');ld(17);R('xor a');C('load_raw');J('load_failed','nc');X('ld ix,$4000',0xdd,0x21,0,0x40);ld(6912);imm(255);C('load_raw');J('load_failed','nc');R('xor a');X('out ($fe),a',0xd3,0xfe);C('hold_three');C('wait_press');J('title')
L('wait_release_final');R('ld d,8');L('final_release_loop');R('halt');C('keys');la('fire');R('or a');J('wait_release_final','nz');X('dec d',0x15);J('final_release_loop','nz');ret()
L('hold_three');C('music_stop');la('game_state');cp(2);J('end_hold','nz');lh('victory_music');C('music_start');L('end_hold');R('ld b,150');L('end_wait');R('halt','push bc');C('music_tick');R('pop bc','dec b');J('end_wait','nz');ret()
L('wait_press');L('release_loop');R('halt');C('keys');la('fire');R('or a');J('release_loop','nz');L('press_loop');R('halt');C('keys');la('fire');R('or a');J('press_loop','z');ret()
L('reset_game')
for n in records:setv(n+'_y',255)
setv('player',88);setv('player_y',160);zero('invul');copyv('initial_hp','boss_hp')
for n in ['death','death_timer','spread_lo','spread_hi','kills','dirty','life_dirty','boss','game_state','cool','tick']:zero(n)
for j in range(4):zero(f'e{j}_wait')
C('wave_reset');ret()
L('hud_initial');setv('dirty',4)
for j in range(4):C('hud_update')
# On phase transition remove icons of lives lost, without modifying the saved life count.
la('lives');cp(3);J('hud_init_phase','nc');R('push af');setv('lives',2);C('hud_lives');R('pop af','push af');cp(2);J('hud_init_restore','nc');setv('lives',1);C('hud_lives');L('hud_init_restore');R('pop af');sa('lives')
# Draw only during initialization: name occupies six interior HUD character cells.
L('hud_init_phase');lh('phase_name');ld('phase_name_dest');R('ld b,7');L('phase_name_loop');R('push bc','ld a,(de)','ld c,a','inc de','ld a,(de)','ld b,a','inc de','push de','ld d,b','ld e,c');lc(6);R('ldir','pop de','pop bc','dec b');J('phase_name_loop','nz')
lh(0x5800+21*32+25);la('phase_color');R('ld b,6');L('phase_name_color');R('ld (hl),a','inc hl','dec b');J('phase_name_color','nz');ret()
tabwords('phase_name_dest',[attr(y)+25 for y in range(168,175)])
L('title_header');data('header_buf',[0]*17);labels['title_header_name']=labels['header_buf']+1;labels['title_header_name2']=labels['header_buf']+2
