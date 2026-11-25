from test_cpu import *
from hud_names import bitmap,NAMES
from PIL import Image
import hashlib
old=P.parent/'NEPTUNO_ALFA_010'; assert old.exists()
for lv in range(1,6):
 c=start(lv); rows=b''.join(bytes(c.m[0x4000+((y&192)<<5)+((y&7)<<8)+((y&56)<<2)+25:0x4000+((y&192)<<5)+((y&7)<<8)+((y&56)<<2)+31]) for y in range(168,175));assert rows==bitmap(lv),(lv,rows.hex(),bitmap(lv).hex())
 assert bytes(c.m[0x5800+21*32+25:0x5800+21*32+31])==bytes([c.v('phase_color')])*6
 assert c.logical()==Image.open(P/f'terrain{lv}.png').convert('1').tobytes()[-4608:]
 assert (P/f'ground_plan{lv}.json').read_bytes()==(old/f'ground_plan{lv}.json').read_bytes()
 # compare all sprite assets and full original map bank for first two levels
 phase=(P/f'phase{lv}.bin').read_bytes(); prev=(old/f'phase{lv}.bin').read_bytes();assert phase[0xf100-0xa200:]==prev[0xf100-0xa200:]
 if lv<=2:assert phase[0xd900-0xa200:0xf100-0xa200]==prev[0xd900-0xa200:0xf100-0xa200]
 # Actual screenshot from emulated video RAM, with bright and normal Spectrum palette.
 raw=c.screen(); im=Image.new('RGB',(256,192));pix=im.load()
 for y in range(192):
  off=((y&192)<<5)+((y&7)<<8)+((y&56)<<2)
  for x in range(256):
   at=raw[6144+(y//8)*32+x//8]; ink=raw[off+x//8]&(128>>(x%8));color=(at&7) if ink else ((at>>3)&7);v=255 if at&64 else 205;pix[x,y]=(v if color&2 else 0,v if color&4 else 0,v if color&1 else 0)
 im.resize((768,576),Image.Resampling.NEAREST).save(P/f'captura_fase{lv}.png')
 print(NAMES[lv-1], 'HUD, map init, unchanged routes and sprites PASS',flush=True)
