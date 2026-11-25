from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, zipfile,io
P=Path(__file__).parent; A=P/'assets'
z=zipfile.ZipFile(P.parent/'NEPTUNO_ATACA_ZX_MAPAS_V2_ARQUITECTURA.zip'); b=zipfile.ZipFile(P.parent/'NEPTUNO_ATACA_ZX_48K_BANCO_1BPP.zip'); e=zipfile.ZipFile(P.parent/'NEPTUNO_ATACA_ZX_ENEMIGOS_V2.zip')
for lv,n,boss in [(3,'03_SIRIA','03_TANQUE_MAESTRO'),(4,'04_FRANCIA_NOCHE','04_EIFFEL_MUTANTE'),(5,'05_BARCELONA','05_TRONO_HELADO_XV')]:
 p='NEPTUNO_ZX_MAPAS_V2/'+n+'/'; im=Image.open(io.BytesIO(z.read(p+'mapa.png'))).convert('1'); im.save(A/f'map{lv}_original.png'); (A/f'surface{lv}.bin').write_bytes(z.read(p+'spawn.bin'))
 a=np.array(im,dtype=np.uint8); # Remove isolated pixels; retain contiguous architectural outlines. Thin dense areas on land only.
 count=sum(np.roll(np.roll(a,dy,0),dx,1) for dy in (-1,0,1) for dx in (-1,0,1) if dx or dy)
 a[(a==1)&(count==0)]=0
 Image.fromarray(a*255).convert('1').save(A/f'map{lv}.png')
 for kind in ('PNG','MASK'):
  im=Image.open(io.BytesIO(b.read('NEPTUNO_ZX_1BPP/'+boss+'/'+kind+'/activo_00.png'))).convert('1'); w,h=im.size; nw=min(144,w); nh=min(144,round(h*nw/w)); im.resize((nw,nh),Image.Resampling.NEAREST).save(A/f'boss{lv}_{kind}.png')
for typ,file in [('soldier','SOLDADO/PNG/apuntado_S_00.png'),('tank','TANQUE_SIRIA/PNG/S_00.png')]:
 im=Image.open(io.BytesIO(e.read('NEPTUNO_ZX_ENEMIGOS_V2/'+file))).convert('RGBA'); ar=np.array(im); out=Image.fromarray(((ar[:,:,:3].max(2)>100)&(ar[:,:,3]>100)).astype(np.uint8)*255).convert('1').resize((16,16),Image.Resampling.NEAREST);out.save(A/f'{typ}.png')
# native, centered 5x7 pixel text, black paper, bright yellow/cyan
font={'F':[31,16,16,30,16,16,16],'A':[14,17,17,31,17,17,17],'S':[15,16,16,14,1,1,30],'E':[31,16,16,30,16,16,31],'U':[17,17,17,17,17,17,14],'P':[30,17,17,30,16,16,16],'R':[30,17,17,30,20,18,17],'D':[30,17,17,17,17,17,30],'C':[14,17,16,16,16,17,14],'I':[31,4,4,4,4,4,31],'/':[1,1,2,4,8,16,16],' ':[0]*7}
im=Image.new('1',(256,192));d=ImageDraw.Draw(im)
def text(s,y,k):
 x=(256-(len(s)*6-1)*k)//2
 for c in s:
  for j,r in enumerate(font[c]):
   for i in range(5):
    if r&(16>>i):d.rectangle((x+i*k,y+j*k,x+(i+1)*k-1,y+(j+1)*k-1),fill=1)
  x+=6*k
text('FASE',64,4);text('SUPERADA',96,4)
raw=im.tobytes();scr=bytearray(6912)
for y in range(192):
 off=((y&192)<<5)+((y&7)<<8)+((y&56)<<2);scr[off:off+32]=raw[y*32:y*32+32]
for y in range(24):scr[6144+y*32:6144+(y+1)*32]=bytes([0x45 if y>=17 else 0x46])*32
(A/'FASE_SUPERADA.scr').write_bytes(scr);(A/'FASE_SUPERADA_2.scr').write_bytes(scr)
im.save(P/'fase_superada_bitmap.png')
