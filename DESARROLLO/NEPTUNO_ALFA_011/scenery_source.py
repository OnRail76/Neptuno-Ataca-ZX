from PIL import Image,ImageDraw,ImageFont
import numpy as np, zipfile,io,math,json, pathlib,random
ROOT=pathlib.Path(__file__).parent / "scenery_rebuilt"
ROOT.mkdir(exist_ok=True)
import os
Z=zipfile.ZipFile(os.environ.get('NEPTUNO_SMS_ASSETS',str(ROOT.parent.parent/'NEPTUNO_ATACA_RECURSOS_COMPLETOS_SMS.zip')))
W,H=192,768
names=['01_MEDITERRANEO','02_GRECIA','03_SIRIA','04_FRANCIA_NOCHE','05_BARCELONA']
boss=['Acorazado Glacial','Rodas II','Tanque Maestro','Eiffel Mutante','Trono Helado XV']
# Interior samples from original sheets, not edge pieces. Normalize into sparse repeating textures.
samples=[((0,6),(0,0)),((0,0),(2,0)),((0,0),(0,0)),((0,0),(0,4)),((0,7),(0,0))]
Y,X=np.indices((H,W))
manifest=[]; previews=[]
for k,name in enumerate(names):
 n='01_TERRENOS/'+name+'/'+('02_terreno_16x16_RGBA.png' if k==0 else 'terreno_16x16_RGBA.png')
 src=np.array(Image.open(io.BytesIO(Z.read(n))).convert('RGB'),dtype=float)
 def tex(tx,ty,density):
  a=src[ty*16:ty*16+16,tx*16:tx*16+16]; lum=a@np.array([.299,.587,.114]); q=np.quantile(lum,1-density); b=lum>q; return b[Y%16,X%16]
 water=tex(*samples[k][0],.025); land=tex(*samples[k][1],.075)
 # terrain class 0 water, 1 ground, 2 road, 3 structures
 cls=np.zeros((H,W),np.uint8)
 if k==0:
  l=24+10*np.sin(Y/55)+6*np.sin(Y/23); r=164+12*np.sin(Y/72+1)
  cls[(X<l)|(X>r)]=1
  for cx,cy,rx,ry in [(145,570,19,39),(48,300,19,32),(152,133,13,27)]: cls[((X-cx)/rx)**2+((Y-cy)/ry)**2<1]=1
 elif k==1:
  l=30+12*np.sin(Y/60);r=150+14*np.sin(Y/80)
  cls[(X<l)|(X>r)|(Y<176)]=1
  cls[(Y<176)&(abs(X-96)<17)]=2
 elif k==2:
  cls[:]=1; center=96+25*np.sin(Y/100);cls[abs(X-center)<20]=2
 elif k==3:
  center=96+22*np.sin(Y/140); cls[:]=1; cls[abs(X-center)<20]=0
  cls[(abs(X-center)>25)&(abs(X-center)<36)]=2
  for y in (160,384,608): cls[(Y>=y)&(Y<y+24)]=2
 else:
  cls[:]=1; coast=151+9*np.sin(Y/65);cls[X>coast]=0
  cls[(X>coast-13)&(X<=coast)]=2
  cls[(X>=56)&(X<88)]=2
  for y in (120,320,520,680): cls[(Y>=y)&(Y<y+20)&(X<=coast)]=2
 # terrain edge traced continuously from class mask (no hand-picked corner tiles)
 def edge(a):
  p=np.pad(a,1,mode='edge');return a&(~p[:-2,1:-1]|~p[2:,1:-1]|~p[1:-1,:-2]|~p[1:-1,2:])
 ground=cls==1; sea=cls==0; road=cls==2
 bitmap=edge(sea)|edge(road) if k>=2 else (water&sea)|(land&ground)|edge(sea)|edge(road)
 # sparse road markings; use original source sample for surface texture only outside roads
 if k==2: bitmap|=road&(abs(X-center)<1)&((Y%16)<7)
 if k==4: bitmap|=road&(X==72)&((Y%16)<7)
 im=Image.fromarray(bitmap.astype('uint8')*255).convert('1');d=ImageDraw.Draw(im)
 # Draw buildings as whole objects, never clipped across terrain boundary. Use original tile texture for roofs.
 rng=random.Random(410+k); objects=[]
 # Individual complete landmark from supplied decoration sheet, placed on clear ground.
 def original_object(path,crop,x,y,w,h,terrain=1):
  srcim=Image.open(io.BytesIO(Z.read(path))).convert('RGBA')
  if crop:srcim=srcim.crop(crop)
  bb=srcim.getchannel('A').getbbox()
  if not bb:return False
  srcim=srcim.crop(bb);srcim.thumbnail((w,h),Image.Resampling.LANCZOS)
  a=np.array(srcim); hh,ww=a.shape[:2]; mask=a[:,:,3]>100
  if not np.all(cls[y:y+hh,x:x+ww][mask]==terrain):return False
  lum=a[:,:,:3]@np.array([.299,.587,.114]); bw=Image.fromarray((lum>115).astype('uint8')*255).convert('1')
  im.paste(bw,(x,y),Image.fromarray(mask.astype('uint8')*255));cls[y:y+hh,x:x+ww][mask]=3;objects.append((x,y,x+ww-1,y+hh-1));return True
 deco='01_TERRENOS/'+name+'/'
 if k==1:original_object(deco+'TEMPLO_RGBA.png',None,8,48,64,48)
 if k==2:original_object(deco+'decoracion_RGBA.png',(0,0,95,90),12,80,40,40)
 if k==3:original_object(deco+'decoracion_RGBA.png',(0,0,145,265),5,36,43,80)
 if k==4:original_object(deco+'decoracion_RGBA.png',(0,0,175,210),6,32,46,62)
 
 def building(x,y,w,h,kind):
  if x<2 or x+w>=W-2 or y<2 or y+h>=H-2 or not np.all(cls[y:y+h+1,x:x+w+1]==1): return False
  if any(not(x+w+4<a or x>b+4 or y+h+4<c or y>e+4) for a,c,b,e in objects):return False
  objects.append((x,y,x+w,y+h));d.rectangle((x,y,x+w,y+h),fill=0,outline=1)
  # Native 1-bit architectural motifs, bounded by the original footprint.
  def line(points): d.line([(x+u,y+v) for u,v in points],fill=1)
  def rect(u,v,U,V,fill=None): d.rectangle((x+u,y+v,x+U,y+V),outline=1,fill=fill)
  def poly(points,fill=None): d.polygon([(x+u,y+v) for u,v in points],outline=1,fill=fill)
  # Select variety without consuming the original placement RNG.
  variant=(x//3+y//7)%4
  d.rectangle((x,y,x+w,y+h),fill=0)
  if k==0:
   if variant==0: # lighthouse, stepped base and lantern
    rect(3,h-4,w-3,h-1);poly([(4,h-4),(5,5),(w-5,5),(w-4,h-4)]);rect(4,2,w-4,5);line([(3,2),(w//2,0),(w-3,2)]);line([(5,9),(w-5,9)]);line([(5,12),(w-5,12)])
   else: # coastal houses, pitched roofs and shutters
    poly([(0,5),(w//2,0),(w,5),(w-1,h-1),(1,h-1)]);line([(0,5),(w,5)]);line([(w//2,1),(w//2,4)]);rect(2,7,4,9);rect(w-4,7,w-2,9);rect(w//2-1,h-4,w//2+1,h-1)
    if variant==2:line([(2,3),(w//2,3)]);line([(2,h-3),(4,h-3)])
  elif k==1:
   if variant%2==0: # cycladic chapel with dome and cross
    rect(1,6,w-1,h-1);poly([(3,6),(3,4),(5,2),(w-5,2),(w-3,4),(w-3,6)]);line([(w//2,0),(w//2,2)]);line([(w//2-1,1),(w//2+1,1)]);rect(w//2-1,h-5,w//2+1,h-1);d.point((x+3,y+9),fill=1)
   else: # classical colonnade
    poly([(0,5),(w//2,0),(w,5)],1);line([(0,7),(w,7)]);line([(0,h-2),(w,h-2)]);
    for u in (2,w//2,w-2):line([(u,8),(u,h-3)])
  elif k==2:
   if variant%2==0: # courtyard house, parapet and entrance
    rect(0,1,w,h-1);rect(3,4,w-3,h-5);rect(6,7,w-6,h-8);line([(w//2,h-5),(w//2,h-1)]);line([(2,2),(w-2,2)])
   else: # flat-roof warehouse with ribs and loading gate
    poly([(0,4),(3,1),(w-3,1),(w,4),(w,h-1),(0,h-1)]);line([(0,4),(w,4)]);line([(0,h-5),(w,h-5)]);rect(5,h-4,w-5,h-1)
    for u in range(3,w-2,4):line([(u,6),(u,h-7)])
  elif k==3: # mansard roof, dormers and facade
   poly([(0,6),(3,1),(w-3,1),(w,6),(w,h-1),(0,h-1)]);line([(0,7),(w,7)]);line([(0,14),(w,14)]);line([(3,2),(w-3,2)])
   for u in (3,w//2,w-3):
    line([(u-1,5),(u,4),(u+1,5)]);rect(u-1,9,u+1,11);rect(u-1,16,u+1,18)
   if variant%2:rect(w//2-2,h-4,w//2+2,h-1)
  else: # chamfered Eixample blocks, inner courtyard or modernist facade
   poly([(3,0),(w-3,0),(w,3),(w,h-3),(w-3,h),(3,h),(0,h-3),(0,3)])
   if variant%2==0:
    rect(4,5,w-4,h-5)
    for u in (3,w//2,w-3):d.point((x+u,y+2),fill=1);d.point((x+u,y+h-2),fill=1)
    line([(w//2,h-5),(w//2,h-1)])
   else:
    line([(2,6),(w-2,6)]);line([(2,13),(w-2,13)])
    for u in (3,w//2,w-3):
     line([(u-1,4),(u,2),(u+1,4)]);rect(u-1,8,u+1,11);rect(u-1,15,u+1,18)
  cls[y:y+h+1,x:x+w+1]=3;return True
 for y in range(35,H-35,38 if k>=2 else 58):
  for x in ([8,39,125,158] if k<2 else [8,39,131,161] if k==2 else [8,33,145,169] if k==3 else [8,33,102,127]):
   if rng.random()<.78:building(x+rng.randrange(-2,3),y+rng.randrange(-7,8),12 if k<2 else 16,14 if k<2 else 22,'temple' if k==1 else 'ruin' if k==2 else 'house')
 
 # Sparse ships, aligned in water, with continuous hull and deck. not enemies themselves.
 if k==0:
  for x,y in [(79,650),(112,440),(81,240),(110,95)]:
   if np.all(cls[y:y+30,x:x+12]==0):
    d.polygon([(x+6,y),(x+11,y+7),(x+11,y+26),(x+6,y+29),(x,y+26),(x,y+7)],fill=0,outline=1);d.rectangle((x+3,y+9,x+8,y+19),outline=1);d.line((x+6,y+3,x+6,y+8),fill=1);cls[y:y+30,x:x+12]=3
 arr=np.array(im,dtype=np.uint8)
 if k>=2:
  # Only apply repeating texture to fully homogeneous, empty cells, never mixed architecture tiles.
  for yy in range(0,H,8):
   for xx in range(0,W,8):
    c=cls[yy:yy+8,xx:xx+8]; a=arr[yy:yy+8,xx:xx+8]
    if not a.any() and np.all(c==1):a[:]=land[yy:yy+8,xx:xx+8]
    elif not a.any() and np.all(c==0):a[:]=water[yy:yy+8,xx:xx+8]
  im=Image.fromarray(arr*255).convert('1')
 tiles=[]; idx={}; ids=[]
 for y in range(0,H,8):
  for x in range(0,W,8):
   t=np.packbits(arr[y:y+8,x:x+8],axis=1).tobytes()
   if t not in idx:idx[t]=len(tiles);tiles.append(t)
   ids.append(idx[t])
 out=ROOT/name;out.mkdir(exist_ok=True); (out/'class.bin').write_bytes(cls.tobytes()); (out/'objects.json').write_text(json.dumps(objects)); im.save(out/'mapa.png');(out/'tiles.bin').write_bytes(b''.join(tiles));(out/'map_u16le.bin').write_bytes(np.array(ids,dtype='<u2').tobytes());
 # category per tile: only wholly ground/road permits ground spawn. water likewise. mixed no spawn.
 spawn=[]
 for y in range(0,H,8):
  for x in range(0,W,8):
   c=cls[y:y+8,x:x+8];spawn.append(1 if np.all(c==0) else 2 if np.all((c==1)|(c==2)) else 0)
 (out/'spawn.bin').write_bytes(bytes(spawn));
 packed=bytes(sum(spawn[i+j]<<(2*j) for j in range(4)) for i in range(0,len(spawn),4));(out/'spawn_2bpp.bin').write_bytes(packed)
 import zlib
 (out/'tiles.deflate').write_bytes(zlib.compress(b''.join(tiles),9));(out/'map.deflate').write_bytes(zlib.compress(np.array(ids,dtype='<u2').tobytes(),9))
 assert all(((packed[i//4]>>(2*(i%4)))&3)==v for i,v in enumerate(spawn))
 
 if len(tiles)<=256:(out/'map_u8.bin').write_bytes(bytes(ids))
 with (out/'mapa.asm').open('w') as f:
  f.write('; 24 x 96 caracteres, fila superior primero; scroll desde abajo\nmapa_tiles:\n')
  for t in tiles:f.write(' db '+','.join(str(v) for v in t)+'\n')
  f.write('mapa_indices:\n');
  for i in range(0,len(ids),24):f.write(' '+('db' if len(tiles)<=256 else 'dw')+' '+','.join(map(str,ids[i:i+24]))+'\n')
 rebuilt=np.zeros_like(arr)
 for i,t in enumerate(ids):y,x=divmod(i,24);rebuilt[y*8:y*8+8,x*8:x*8+8]=np.unpackbits(np.frombuffer(tiles[t],dtype=np.uint8)).reshape(8,8)
 assert np.array_equal(rebuilt,arr)
 manifest.append(dict(fase=name,jefe=boss[k],tiles=len(tiles),bytes_tiles=len(tiles)*8,bytes_map=2304*(1 if len(tiles)<=256 else 2),bytes_spawn=576,source=n,objetos=len(objects)))
 previews.append(im.convert('RGB'))
(ROOT/'inventario.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)); atlas=Image.new('RGB',(5*200,800),'black');dd=ImageDraw.Draw(atlas)
for i,im in enumerate(previews):atlas.paste(im,(i*200,24));dd.text((i*200+3,4),names[i],fill='white')
atlas.save(ROOT/'ATLAS.png');print(manifest)
