"""Offline collision-safe spawn planning on the authoritative V2 surface map.
World coordinate: 576 - floor(t/2) + y. 16x16 whole footprint.
No pathfinding during gameplay; units continue to the bottom in safe straight lanes.
"""
import numpy as np
EMPTY=(0,255,0,0)

def ground_waves(surface, level, original):
 out=[[EMPTY]*4 for _ in range(10)]; busy=[0]*4; entries=[]
 def valid(x,t,kind):
  dur=192 if kind==4 else 154 if kind==3 else 384
  if t+dur>1248:return False
  for age in range(dur):
   # Conservative +/-1 margin for render / scroll phase.
   y=age if kind==4 else age+age//4 if kind==3 else age//2
   if y>=192:break
   wy=576-(t+age)//2+y
   lo=max(0,wy-1);hi=min(768,wy+17)
   if wy<0 or wy+16>768 or not np.all(surface[lo//8:(hi+7)//8,x//8:x//8+2]==2):return False
  return True
 def add(t,rec,slot):
  x,d,m,k=rec;w=t//120;out[w][slot]=(x,t%120,m,k)
  dur=192 if k==4 else 154 if k==3 else 384 if k==2 else 89
  busy[slot]=t+dur+13;entries.append((t,x,k,dur,slot))
 def ground(w,kind,prefer,offset):
  options=[]
  for t in range(w*120+offset,min((w+1)*120,w*120+offset+50),4):
   slots=[i for i in range(4) if out[w][i]==EMPTY and busy[i]<=t]
   if not slots:continue
   dur=192 if kind==4 else 154 if kind==3 else 384
   for x in range(0,169,8):
    # Ground units never share a lane if their lifetime overlaps, even if killed early.
    if any(k>=2 and t<tt+dd+8 and tt<t+dur+8 and abs(x-xx)<24 for tt,xx,k,dd,_ in entries):continue
    if valid(x,t,kind):options.append((abs(x-prefer)+(t-w*120-offset)*.6,t,x,slots[0]))
  if not options:return False
  _,t,x,i=min(options);add(t,(x,0,6 if kind==2 else 8,kind),i);return True
 def air(w,rec):
  x,d,m,k=rec
  if d==255 or k>=2:return False
  for t in range(w*120+d,min((w+1)*120,w*120+d+32),4):
   for i in range(4):
    if out[w][i]==EMPTY and busy[i]<=t:
     add(t,rec,i);return True
  return False
 # Retain air pattern and reserve a limited number of slots for persistent terrain enemies.
 for w in range(10):
  if level==1:
   # Replace naval encounters by two land emplacements, if a valid bank exists.
   if w in (1,5):ground(w,2,16 if w==1 else 160,0)
   for rec in original[w]:air(w,rec)
   if w==5:
    for rec in [(48,16,4,1),(128,28,1,0)]:air(w,rec)
  elif level==2:
   if w in (1,4,6):ground(w,2,[16,160,16][(1,4,6).index(w)],0)
   for rec in original[w]:air(w,rec)
  else:
   if w in (0,2,4,6,8):
    kinds=[3,4,3] if (w+level)%4 else [4,3,4]
    prefs=([40,88,144] if level==3 else [24,104,160] if level==4 else [24,64,112])
    for j,(k,x) in enumerate(zip(kinds,prefs)):ground(w,k,x,j*20)
   if w==3:ground(w,2,24,0)
   for rec in original[w]:air(w,rec)
   if w%2==0:
    for rec in [(36,72,4,1),(132,84,0,0)]:air(w,rec)
 return out,entries
