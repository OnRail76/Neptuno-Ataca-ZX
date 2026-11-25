from pathlib import Path
p=Path('build.py');s=p.read_text()
s=s.replace("world=Image.open(A/('mapa_legible.png' if LEVEL==1 else 'grecia_legible.png')).convert('1')", "world=Image.open(A/({1:'mapa_legible.png',2:'grecia_legible.png'}.get(LEVEL,f'map{LEVEL}.png'))).convert('1')")
s=s.replace("else:\n boss=Image.open(A/'rodas_PNG.png')", "elif LEVEL==2:\n boss=Image.open(A/'rodas_PNG.png')")
s=s.replace(' # Align the bottom', "else:\n boss=Image.open(A/f'boss{LEVEL}_PNG.png').convert('1');mk=Image.open(A/f'boss{LEVEL}_MASK.png').convert('1').point(lambda v:255-v)\n # Align the bottom")
s=s.replace("level=Image.new('1',(192,960));level.paste(world,(0,192));level.paste(boss,(24,144-boss.height),mk);level.save(ROOT/f'terrain{LEVEL}.png')", "level=Image.new('1',(192,960));level.paste(world,(0,192));level.paste(boss,(24,144-boss.height),mk);level.save(ROOT/f'terrain{LEVEL}.png')")
s=s.replace('CLEAR=0xfbe0','CLEAR=0xfbe0; BALL=0xfd80; SOLDIER=0xfde0; TANK=0xfe40; TURRET_L=0xfea0; TURRET_R=0xfed0')
s=s.replace("assert CLEAR+len(screens['clear_scr'])<=0x10000", "assert CLEAR+len(screens['clear_scr'])<=BALL")
s=s.replace("('expl_ptr',EXP,24)","('expl_ptr',EXP,24),('ball_ptr',BALL,12),('soldier_ptr',SOLDIER,0),('tank_ptr',TANK,0),('turret_l_ptr',TURRET_L,0),('turret_r_ptr',TURRET_R,0)")
s=s.replace("data('phase_color',[69 if LEVEL==1 else 71]);data('initial_hp',[20 if LEVEL==1 else 28]);", "data('phase_color',[[69,71,70,66,68][LEVEL-1]]);data('initial_hp',[[20,28,32,38,44][LEVEL-1]]);data('boss_thresholds',[[16,23,26,31,36][LEVEL-1],[11,16,18,21,25][LEVEL-1],[6,8,9,10,12][LEVEL-1]]);")
# change bullet movement vertical as signed speed and use ball sprite
s=s.replace("add(2);cp(189);J(n+'_off','nc');sa(n+'_y');la(n+'_dx')", "R('ld b,a');la(n+'_dy');R('add a,b');cp(189);J(n+'_off','nc');sa(n+'_y');la(n+'_dx')")
s=s.replace("[('b0','bullet_ptr',4),('b1','bullet_ptr',4)]", "[('b0','ball_ptr',4),('b1','ball_ptr',4)]")
# visual turret angle chosen using player x; call uses BC coords; leave boat as type2 in level 1.
# clip visible sprites below bottom instead of wrapping to top, also restore matching area.
s=s.replace("L('sprite_setup');R('ld a,b');cp(192);ret('nc') if False else None\nJ('sprite_inactive','nc');", "L('sprite_setup');R('ld a,b');cp(192);J('sprite_inactive','nc');C('clip_height');")
s=s.replace("cp(192);ret('nc');C('ring_addr');R('ld e,l'", "cp(192);ret('nc');C('clip_height');C('ring_addr');R('ld e,l'")
# add local graphics at end, using fixed byte aligned positions for ground columns
needle="# Two 8x8 native explosion frames"
pos=s.index(needle)
s=s[:pos]+'''# Rounded hostile projectile: 4x4 diamond-like ball, distinct from player laser.
shifted(bytes([0x60,0xf0,0xf0,0x60]),None,4,BALL)
def aligned(im,base):
 a=np.packbits(np.pad(np.array(im.convert('1'),dtype=np.uint8),((0,0),(0,8))),axis=1).tobytes();assert len(a)==48;emit_phase(base,a)
for name,base in [('soldier',SOLDIER),('tank',TANK)]:
 im=Image.open(A/f'{name}.png').convert('1');aligned(im,base)
 # second animation frame, moving legs or tracks only, selected by tick below
 im2=im.copy();arr=np.array(im2);arr[12:16]=np.roll(arr[12:16],1,axis=1);aligned(Image.fromarray(arr),base+48)
# Directional turret silhouettes with a clear rotating barrel; fixed aligned x.
turret=Image.open(A/'torreta16.png').convert('1')
for direction,base in [(-1,TURRET_L),(1,TURRET_R)]:
 im=turret.copy();d=ImageDraw.Draw(im);d.rectangle((5,7,10,15),fill=0);d.line((8,7,1 if direction<0 else 14,14),fill=1,width=2);aligned(im,base)
''' + s[pos:]
p.write_text(s)
