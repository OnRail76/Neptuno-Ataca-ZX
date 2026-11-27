from test_cpu import *
import numpy as np
from collections import Counter
for lv in range(1,6):
 c=start(lv);surface=np.frombuffer((P/'assets'/({1:'spawn.bin',2:'grecia_spawn.bin'}.get(lv,f'surface{lv}.bin'))).read_bytes(),np.uint8).reshape(96,24)
 plan=json.loads((P/f'ground_plan{lv}.json').read_text());expected={(t,j):(x,k) for t,x,k,d,j in plan};seen={};last=[None]*4;fired=set();exits=Counter();speeds=Counter()
 for t in range(1248):
  c.setv('tick',(t+1)&255);c.call('waves_step');ground=[]
  for j in range(4):
   x,y,k=c.v(f'e{j}'),c.v(f'e{j}_y'),c.v(f'e{j}_type');now=None if y==255 else (x,y,k)
   if now and not last[j]:
    assert expected[t,j]==(x,k),(lv,t,j,now,expected.get((t,j)));seen[t,j]=(x,k)
   if now and last[j]:
    assert abs(x-last[j][0])<=2 and abs(y-last[j][1])<=2,(lv,t,j,last[j],now)
    if k in (3,4):assert x==last[j][0] and y-last[j][1] in ((1,2) if k==3 else (1,));speeds[k,y-last[j][1]]+=1
   if now and k>=2:
    wy=576-t//2+y;assert x<=168 and np.all(surface[wy//8:(wy+16+7)//8,x//8:x//8+2]==2),(lv,t,j,x,y,wy,k)
    ground.append((x,y,k))
   if not now and last[j] and last[j][2]>=2:assert last[j][1]>=190;exits[last[j][2]]+=1
   last[j]=now
  for i,(x,y,k) in enumerate(ground):
   for xx,yy,kk in ground[i+1:]:assert abs(x-xx)>=24
  for j in range(2):c.call(f'move_b{j}')
  before=[c.v(f'b{j}_y') for j in range(2)];c.call('enemy_attack')
  for j in range(2):
   if before[j]==255 and c.v(f'b{j}_y')!=255:
    for i,(x,y,k) in enumerate([v or (-100,-100,-1) for v in last]):
     if k>=2 and c.v(f'b{j}')==x+7 and c.v(f'b{j}_y')==y+8:
      t0=max(tt for tt,slot in seen if slot==i);fired.add((t0,i))
 assert seen==expected,(lv,len(seen),len(expected),set(expected)-set(seen))
 assert not any(v and v[2]>=2 for v in last),(lv,last)
 print('level',lv,'spawned',Counter(k for x,k in seen.values()),'ground exits',exits,'speeds',speeds,'ground fired',len(fired),'of',sum(k>=2 for x,k in seen.values()),flush=True)
 assert all((t,j) in fired for (t,j),(x,k) in seen.items() if k>=2),(lv,'turret did not fire')
# Every shot counts exactly once, no shifting or score until final hit.
for lv in range(1,6):
 for k,hp in [(0,1),(1,1),(2,1),(3,2),(4,3)]:
  c=start(lv,True);c.setv('e0',64);c.setv('e0_y',80);c.setv('e0_type',k);c.setv('e0_base',hp)
  for hit in range(1,hp+1):
   c.setv('s0',71);c.setv('s0_y',86);c.call('collisions');assert c.v('s0_y')==255;assert c.v('e0')==64 and c.v('e0_y')==80
   assert c.v('e0_wait')==(12 if hit==hp else 0);assert c.v('score3')==(1 if hit==hp else 0)
 print('resistance level',lv,'2/3 hits PASS')
