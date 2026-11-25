# Coreography data and state. All trajectories expressed in pixels and 50 Hz ticks.
# Records x, delay, pattern, sprite type. 255 delay denotes an empty slot.
# Modes: 0 straight, 1 sine, 2/3 pincer, 4 incursion, 5 swarm, 6 boat, 7 diagonal.
import math
empty=(0,255,0,0)
def e(x,d,m,t=0):return (x,d,m,t)
surface0=np.frombuffer((A/'spawn.bin').read_bytes(),dtype=np.uint8).reshape(96,24)
def water(w,delay,prefer):
 y=(768-(w*120+delay)//2-192)//8
 xs=[x*8 for x in range(2,21) if 0<=y and y+3<96 and np.all(surface0[y:y+4,x:x+2]==1)]
 return e(min(xs,key=lambda x:abs(x-prefer)),delay,6,2) if xs else empty
waves=[
 [e(44,12,0),e(88,0,0,1),e(132,12,0),e(88,24,0,1)], # V
 [e(86,0,1),e(86,12,1),e(86,24,1),empty], # sine
 [e(46,0,4,1),e(130,8,4,1),empty,empty], # stop/fire/retreat
 [e(12,0,2),e(36,10,2,1),e(156,0,3),e(132,10,3,1)], # pincer
 [e(24,0,5),e(64,8,5),e(112,16,5),e(152,24,5)], # swarm
 [e(84,10,1,1),empty,water(5,0,40),water(5,12,136)], # naval
 [e(32,0,4,1),e(132,8,4,1),empty,empty], # mixed with surviving boats
 [e(20,0,7),e(44,18,7,1),empty,empty], # staggered
 [e(38,12,0),e(88,0,0,1),e(138,12,0),e(88,24,0,1)], # V
 [e(16,0,2,1),e(38,10,2),e(150,0,3,1),e(128,10,3)], # final pincer
]
if LEVEL==2:
 surface2=np.frombuffer((A/'grecia_spawn.bin').read_bytes(),dtype=np.uint8).reshape(96,24)
 def land(w,delay,prefer):
  y=(768-(w*120+delay)//2-192)//8
  xs=[x*8 for x in range(0,22) if 0<=y and y+2<96 and np.all(surface2[y:y+2,x:x+2]==2)]
  return e(min(xs,key=lambda x:abs(x-prefer)),delay,6,2) if xs else empty
 waves=[
  [e(70,0,1,1),e(70,12,1),e(70,24,1,1),empty],
  [e(82,0,4,1),e(110,12,4,1),land(1,0,160),land(1,48,24)],
  [e(16,0,2,1),e(152,10,3),empty,empty],
  [e(38,0,4,1),e(130,12,4,1),empty,empty],
  [e(70,0,1),e(110,12,1,1),land(4,0,0),land(4,64,168)],
  [e(32,0,7,1),e(72,18,7),empty,empty],
  [e(32,0,5),e(152,16,5),empty,empty],
  [e(46,0,4,1),e(136,8,4,1),e(92,24,1),empty],
  [e(40,12,0),e(88,0,0,1),e(136,12,0),e(88,24,0,1)],
  [e(16,0,2,1),e(38,10,2),e(150,0,3,1),e(128,10,3)],
 ]
 print('Grecia wave table',waves)
if LEVEL>=3:
 surface=np.frombuffer((A/f'surface{LEVEL}.bin').read_bytes(),np.uint8).reshape(96,24)
 # Pick continuous land corridors for moving troops; aim for spread and avoid water.
 # Ground enemies advance 2 px/tick, relative to 0.5 px/tick background.
 used={}
 def ground(w,delay,prefer,kind):
  y=576-(w*120+delay)//2; movement=kind in (3,4)
  y0=max(0,y//8);y1=min(96,(y+(145 if movement else 16)+7)//8)
  xs=[x for x in range(0,22) if np.all(surface[y0:min(96,y0+2),x:x+2]==2)]
  if not xs:return empty
  def cost(x):
   region=surface[y0:y1,x:x+2];water=np.count_nonzero(region==1);blocked=np.count_nonzero(region==0)
   return water*1000+blocked*12+abs(x*8-prefer)+sum(180 for q in used.get(w,[]) if abs(x-q)<2)
  x=min(xs,key=cost);used.setdefault(w,[]).append(x);return e(x*8,delay,8 if movement else 6,kind)
 def troops(w,types,prefs,delays=(0,6,12,18)):
  return [ground(w,d,x,k) for d,x,k in zip(delays,prefs,types)]
 if LEVEL==3:
  waves=[
   troops(0,[3]*4,[32,72,112,152]),
   [e(44,12,0),e(88,0,0,1),e(132,12,0),empty],
   troops(2,[4,3,3,4],[32,72,112,152]),
   [e(46,0,4,1),e(130,8,4,1),ground(3,0,24,2),empty],
   [ground(4,0,24,3),ground(4,6,64,4),empty,ground(4,18,144,4)],
   [e(86,0,1),e(86,12,1),empty,e(86,24,1)],
   troops(6,[4,4,3,3],[24,64,104,144]),
   [e(16,0,2,1),e(150,10,3,1),ground(7,0,56,3),ground(7,16,120,4)],
   troops(8,[3,3,3,3],[24,64,104,144]),
   [e(38,12,0),e(88,0,0,1),e(138,12,0),e(88,24,0,1)],
  ]
 elif LEVEL==4:
  waves=[
   troops(0,[3,3,3,3],[16,48,136,160]),
   [e(16,0,2,1),e(40,10,2),e(150,0,3,1),e(126,10,3)],
   troops(2,[3,4,3,4],[16,48,136,160]),
   [e(46,0,4,1),e(130,8,4,1),ground(3,0,24,2),ground(3,0,152,2)],
   [ground(4,0,16,4),ground(4,12,48,3),empty,empty],
   [e(82,0,1),e(82,10,1),empty,empty],
   troops(6,[3,4,3,4],[16,48,136,160]),
   [e(24,0,5),e(64,8,5),e(112,16,5),e(152,24,5)],
   troops(8,[3,3,4,4],[16,48,136,160]),
   [e(16,0,2,1),e(40,10,2),e(150,0,3,1),e(126,10,3)],
  ]
 else:
  waves=[
   troops(0,[3,4,3,4],[16,48,80,112]),
   [e(38,12,0),e(88,0,0,1),e(138,12,0),e(88,24,0,1)],
   troops(2,[4,4,3,3],[16,48,80,112]),
   [e(32,0,4,1),e(132,8,4,1),ground(3,0,24,2),ground(3,0,104,2)],
   [ground(4,0,32,4),ground(4,12,96,3),empty,empty],
   [e(16,0,2,1),e(150,0,3,1),empty,empty],
   troops(6,[4,3,4,3],[16,48,80,112]),
   [e(24,0,5),e(64,6,5),e(112,12,5),e(152,18,5)],
   troops(8,[4,4,4,3],[16,48,80,112]),
   [e(86,0,1,1),e(86,8,1),e(86,16,1,1),e(86,24,1)],
  ]
 print('ground waves',LEVEL,waves)
# Strict V2 map lanes, lifetime-aware slots, no boats.
from ground_plan import ground_waves
surface = surface0 if LEVEL==1 else surface2 if LEVEL==2 else surface
waves, planned = ground_waves(surface,LEVEL,waves)
print('SAFE_PLAN',LEVEL,planned)
(ROOT/f'ground_plan{LEVEL}.json').write_text(json.dumps(planned))
data('wave_table',bytes(v for group in waves for rec in group for v in rec))
L('overlay_end');data('sine_table',[round(20*math.sin(2*math.pi*i/64))&255 for i in range(64)])
data('wave_ptr',[0,0]);data('wave_clock',[0]);
for i in range(4):
 data(f'e{i}_state',[0,0,0,0]);labels[f'e{i}_type']=labels[f'e{i}_state'];labels[f'e{i}_mode']=labels[f'e{i}_state']+1;labels[f'e{i}_age']=labels[f'e{i}_state']+2;labels[f'e{i}_base']=labels[f'e{i}_state']+3
for i in range(2):
 for name,val in [('dx',0),('dy',2),('major',0),('minor',0),('sign',0),('axis',0),('err',0)]:data(f'b{i}_{name}',[val])
data('expl2_ptr',b''.join(struct.pack('<H',EXP+192+i*24) for i in range(8)))
def ixload(n):X('ld ix,'+n,0xdd,0x21,0,0);fix.append((len(b)-2,n))
def ixget(o):X(f'ld a,(ix+{o})',0xdd,0x7e,o)
def ixput(o):X(f'ld (ix+{o}),a',0xdd,0x77,o)
L('wave_reset');zero('wave');zero('wave_clock');zero('sound');lh('wave_table');shm('wave_ptr');ret()
L('waves_step');
for i in range(4):
 n=f'e{i}';la(n+'_wait');R('or a');J(n+'_live','z');R('dec a');sa(n+'_wait');J(n+'_end','nz');setv(n+'_y',255);J(n+'_end');L(n+'_live')
 lhm('wave_ptr');ld(i*4);R('add hl,de','ex de,hl');lh(n);ixload(n+'_state');C('step_enemy');L(n+'_end')
la('wave_clock');R('inc a');cp(120);J('wave_tick_save','c');R('xor a');sa('wave_clock');la('wave');cp(9);J('wave_stop','nc');incv('wave');lhm('wave_ptr');ld(16);R('add hl,de');shm('wave_ptr');ret();L('wave_stop');setv('wave',10);ret();L('wave_tick_save');sa('wave_clock');ret()
L('clip_height');R('ld a,b');cp(177);ret('c');imm(192);R('sub b','push bc','ld b,a');la('draw_h');R('cp b');J('clip_keep','c');R('ld a,b');sa('draw_h');L('clip_keep');R('pop bc');ret()
exec((ROOT/'enemy_draw.py').read_text())
exec((ROOT/'attack.py').read_text())
