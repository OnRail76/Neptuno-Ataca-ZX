from test_cpu import *
from loader import BOOT
# Start via Kempston and verify title cheat. The ROM load is mocked.
boot=json.loads((P/'bootstrap_symbols.json').read_text());c=EngineCPU(1);c.m[BOOT:BOOT+len(c.blocks[3])-2]=c.blocks[3][1:-1];c.pc=BOOT;c.sp=0x5f00;c.tape_pos=4;c.joy=0;c.rununtil(boot['press']);c.joy=16;c.rununtil(boot['release']);c.joy=0;c.rununtil('title_loop');title_frame(c)
for v in [4,4,0,4,0,16,16,0]:title_frame(c,joy=v)
assert c.v('cheat_on')==1;c.joy=16;c.step();c.rununtil('main');assert c.v('cheat_on')==1
print('Kempston load + title cheat PASS')
c=start(1);c.call('lose_life');assert c.v('lives')==2 and c.v('death')==1
for i in range(39):c.call('logic');assert c.v('death')==1
c.call('logic');assert c.v('death')==2
for i in range(34):c.call('logic');assert c.v('death')==2
c.call('logic');assert c.v('death')==0 and c.v('invul')==150
print('death/respawn 40 + 35 + 150 ticks PASS')
for lv in range(1,6):
 c=start(lv);th=list(c.m[sy['boss_thresholds']:sy['boss_thresholds']+3]);res=[]
 for hp in [c.v('initial_hp'),th[0]-1,th[1]-1,th[2]-1]:
  c.setv('boss',2);c.setv('boss_hp',hp);c.setv('tick',0);c.setv('b0_y',255);c.setv('b1_y',255);c.call('enemy_attack');assert c.v('b0_y')!=255
  res.append((c.v('b0'),c.v('b0_dx'),c.v('b0_dy'),c.v('b0_major'),c.v('b1_y')))
 assert len(set(res))>=3,(lv,res)
 print('boss',lv,'four attack bands',res)
# actual sprite shapes in binary (shift zero) and static attributes
for lv in range(1,6):
 c=start(lv);raw=c.m[0xfd80:0xfd8c];assert raw[::3]==bytes([0x60,0xf0,0xf0,0x60]);assert all(v==0 for i,v in enumerate(raw) if i%3)
 assert len((P/f'phase{lv}.bin').read_bytes())==24064
 print('level',lv,'ball sprite and exact phase memory PASS')
