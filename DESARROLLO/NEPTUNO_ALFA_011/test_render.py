from test_cpu import *
from PIL import Image
import sys
lv=int(sys.argv[1]);world=Image.open(P/f'terrain{lv}.png').convert('1').tobytes();c=start(lv);assert c.logical()==world[-4608:]
attrs=bytes(c.m[0x5800:0x5b00]);worst=[0,0];bad=[];h2=sy['frame_b_wait']
# stress full traversal with triple fire + movement. Keep temporary invulnerability refreshed.
for f in range(770):
 c.setv('invul',150);c.setv('spread_lo',244);c.setv('spread_hi',1);c.keys={'space','p'} if f%100<40 else {'space','o'} if f%100<80 else {'space'}
 c.rununtil('frame_a_ready');c.rununtil('blit_top');snap=c.logical();c.rununtil(h2);a=c.cycles-c.halt_times[-1];worst[0]=max(worst[0],a)
 c.rununtil('frame_b_ready');c.rununtil('restore_snapshot');assert c.video()==snap,('blit',lv,f)
 c.rununtil('main');bb=c.cycles-c.halt_times[-1];worst[1]=max(worst[1],bb)
 assert c.logical()==c.logical(0xc700),('restore',lv,f)
 rem=int.from_bytes(c.m[sy['remaining']:sy['remaining']+2],'little');assert c.logical()==world[rem*24:rem*24+4608],('world',lv,f,rem)
 assert bytes(c.m[0x5800:0x5b00])==attrs
 if a>=69855 or bb>=69855:bad.append((f,a,bb))
 if f%100==0:print('frame',lv,f,'A/B',a,bb,'remaining',rem,'boss',c.v('boss'),flush=True)
 if c.v('boss')==2:break
print('level',lv,'worst',worst,'overruns',bad[:15],len(bad),'boss',c.v('boss'),flush=True)
assert c.v('boss')==2
