"""Lossless 512-tile bank: retain roads, coast, landmarks and object footprints.
Standardize only complete ordinary buildings, never substitute partial tiles.
Input: scenery_rebuilt (regenerated V2 without mixed-cell textures).
"""
from pathlib import Path
from PIL import Image,ImageDraw
import numpy as np,json
from collections import Counter
P=Path(__file__).parent; A=P/'assets'
def tiles(a):
 return [np.packbits(a[y:y+8,x:x+8],axis=1).tobytes() for y in range(0,a.shape[0],8) for x in range(0,192,8)]
def boss_rows(i):
 boss=Image.open(A/f'boss{i}_PNG.png').convert('1'); mk=Image.open(A/f'boss{i}_MASK.png').convert('1').point(lambda v:255-v); im=Image.new('1',(192,192));im.paste(boss,(24,144-boss.height),mk);return np.array(im,dtype=np.uint8)
def model(i,variant,w,h):
 im=Image.new('1',(w,h));d=ImageDraw.Draw(im);r=w-1;b=h-1;c=w//2
 if i==3:
  if variant==0:
   d.rectangle((0,1,r,b-1),outline=1);d.rectangle((3,4,r-3,b-4),outline=1);d.line((c,b-4,c,b-1),fill=1)
  else:
   d.polygon([(0,3),(2,1),(r-2,1),(r,3),(r,b-1),(0,b-1)],outline=1);d.line((0,4,r,4),fill=1);d.rectangle((3,b-4,r-3,b-1),outline=1);d.line((4,6,4,b-6),fill=1);d.line((r-4,6,r-4,b-6),fill=1)
 elif i==4:
  d.polygon([(0,4),(2,1),(r-2,1),(r,4),(r,b-1),(0,b-1)],outline=1);d.line((0,6,r,6),fill=1);d.line((0,11,r,11),fill=1)
  for u in (2,c,r-2):d.point((u,3),fill=1);d.rectangle((u-1,8,u+1,9),outline=1);d.point((u,13),fill=1)
 elif i==5:
  d.polygon([(2,0),(r-2,0),(r,2),(r,b-2),(r-2,b),(2,b),(0,b-2),(0,2)],outline=1)
  if variant==0:d.rectangle((3,4,r-3,b-4),outline=1);d.line((c,b-4,c,b-1),fill=1)
  else:
   for yy in (5,10):
    d.line((1,yy-2,r-1,yy-2),fill=1)
    for u in (2,c,r-2):d.rectangle((u-1,yy,u+1,yy+1),outline=1)
 return np.array(im,dtype=np.uint8)
report={}
for i,n in [(3,'03_SIRIA'),(4,'04_FRANCIA_NOCHE'),(5,'05_BARCELONA')]:
 src=P/'scenery_rebuilt'/n; a=np.array(Image.open(src/'mapa.png').convert('1'),dtype=np.uint8); old=a.copy(); assert (src/'spawn.bin').read_bytes()==(A/f'surface{i}.bin').read_bytes(); objs=json.loads((src/'objects.json').read_text()); boss=boss_rows(i); bt=tiles(boss); initial=len(set(bt+tiles(a))); changes=[]
 # All ordinary buildings have the original 17x23 footprint. Landmarks remain untouched.
 candidates=[(x,y,r,b) for x,y,r,b in objs if r-x==16 and b-y==22]; cnt=Counter(bt+tiles(a))
 def local(a,x,y,r,b):
  return [np.packbits(a[yy:yy+8,xx:xx+8],axis=1).tobytes() for yy in range(y//8*8,b//8*8+8,8) for xx in range(x//8*8,r//8*8+8,8)]
 while len(cnt)>512:
  best=None
  for obj in candidates:
   x,y,r,b=obj; orig=a[y:b+1,x:r+1].copy(); oldt=local(a,*obj); variant=((x//3+y//7)%4)%2
   # Prefer retaining the first screen; use entire new motifs inside the original footprint.
   for w,h,align in [(12,16,4),(12,16,8),(8,16,8),(12,18,4)]:
    for xx in range((x+align-1)//align*align,r-w+2,align):
     for yy in range((y+align-1)//align*align,b-h+2,align):
      a[y:b+1,x:r+1]=0;a[yy:yy+h,xx:xx+w]=model(i,variant,w,h); newt=local(a,*obj); delta=Counter(newt);delta.subtract(oldt);gain=sum((cnt[k]>0)-(cnt[k]+v>0) for k,v in delta.items());
      # Prefer larger buildings and keep initial screen as close to original as possible.
      score=(gain-(3 if y>=576 else 0)-(1 if w==8 else 0),gain,w*h)
      if gain>0 and (best is None or score>best[0]):best=(score,obj,a[y:b+1,x:r+1].copy(),delta)
   a[y:b+1,x:r+1]=orig
  if best is None:raise RuntimeError((i,len(cnt)))
  _,obj,img,delta=best;x,y,r,b=obj;a[y:b+1,x:r+1]=img;cnt.update(delta);cnt=+cnt;candidates.remove(obj);changes.append(obj)
 assert len(set(bt+tiles(a)))==len(cnt)<=512
 # All differences in complete original building footprints only; all other pixels unchanged from rebuilt scenery.
 diff=a!=old;mask=np.zeros_like(a,dtype=bool)
 for x,y,r,b in changes:mask[y:b+1,x:r+1]=True
 assert not np.any(diff&~mask)
 Image.fromarray(a*255).convert('1').save(A/f'map{i}.png');report[i]={'initial_tiles':initial,'final_tiles':len(cnt),'standardized_buildings':changes,'initial_screen_standardized':sum(y>=576 for x,y,r,b in changes),'surface_unchanged':True};print(i,report[i],flush=True)
(P/'scenery_report.json').write_text(json.dumps(report,indent=2))
