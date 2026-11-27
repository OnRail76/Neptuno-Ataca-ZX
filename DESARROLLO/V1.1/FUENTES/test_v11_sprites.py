"""V1.1: actual Z80 sprite dispatch for every family, native pixels and restore."""
from test_cpu import *
import numpy as np
import hashlib
manifest=json.loads((P/'original_v10_manifest.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
D=(P/'DRON_bitmap.bin').read_bytes();B=(P/'NAVE_VERTICAL_bitmap.bin').read_bytes()
for lv in range(1,6):
 c=start(lv);ref=manifest[str(lv)];phase=(P/f'phase{lv}.bin').read_bytes()
 assert sha((P/f'terrain{lv}.png').read_bytes())==ref['terrain'];assert sha((P/f'ground_plan{lv}.json').read_bytes())==ref['plan']
 for addr,n,h in ref['ranges']:assert sha(phase[addr-0xa200:addr-0xa200+n])==h
 def check(kind,tick,x,y,sprite,air=False):
  c.setv('tick',tick);c.set16(0,(y<<8)|x);c.r[7]=kind
  back=np.unpackbits(np.frombuffer(c.logical(),np.uint8)).reshape(192,192).copy();expected=back.copy();xx=x&~1 if air else x;h=min(16,192-y);expected[y:y+h,xx:xx+16]|=sprite[:h]
  c.call('draw_enemy_type');assert c.logical()==np.packbits(expected,axis=1).tobytes(),(lv,kind,tick,x,y)
  c.set16(0,(y<<8)|x);c.r[7]=16;c.call('restore_rect');assert c.logical()==np.packbits(back,axis=1).tobytes()
 for kind,ticks,frames,bank in [(0,[0,8],[2,1],D),(1,[0,8,16,24],[4,5,6,5],B)]:
  for tick,frame in zip(ticks,frames):
   sprite=np.unpackbits(np.frombuffer(bank[frame*32:(frame+1)*32],np.uint8)).reshape(16,16)
   for x in range(64,72):check(kind,tick,x,80 if x%2==0 else 181,sprite,True)
 for direction,px,py,sa,ta in [('S',64,144,0xfde0,0xfe40),('N',64,16,0xfa00,0xfe70),('W',8,80,0xf940,0xff00),('E',144,80,0xf9a0,0xff30)]:
  c.setv('player',px);c.setv('player_y',py)
  for kind,addr in [(3,sa),(4,ta),(2,{'S':0xf8e0,'N':0xf910,'W':0xfea0,'E':0xfed0}[direction])]:
   for tick in range(0,32,8):
    a=addr+(48 if kind==3 and tick&8 else 0);sprite=np.unpackbits(np.frombuffer(phase[a-0xa200:a-0xa200+48],np.uint8)).reshape(16,24)[:,:16]
    check(kind,tick,64,80,sprite)
 print('Phase',lv,'original terrain + wave plan + ground banks; 96 draw/restore comparisons PASS',flush=True)
