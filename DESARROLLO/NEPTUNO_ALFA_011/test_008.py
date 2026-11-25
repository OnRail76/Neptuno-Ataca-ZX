"""Regression tests of actual emitted machine code. ROM tape and ULA approximated."""
from test_cpu import *
import numpy as np
# Full boot path and five multicarga transitions, including actual final screen bytes.
from loader import BOOT
boot_sy=json.loads((P/'bootstrap_symbols.json').read_text());c=EngineCPU(1);c.m[BOOT:BOOT+len(c.blocks[3])-2]=c.blocks[3][1:-1];c.pc=BOOT;c.sp=0x5f00;c.tape_pos=4;c.joy=0
c.rununtil(boot_sy['press']);assert c.screen()==(P/'assets/CARGA.scr').read_bytes();c.keys={'space'};c.rununtil(boot_sy['release']);c.keys=set();c.rununtil('title_loop');assert c.screen()==(P/'assets/TITULO.scr').read_bytes();title_frame(c)
for keys in [('a',),(),('a',),(),('space',),()]:title_frame(c,keys)
assert c.v('cheat_on')==1;c.keys={'space'};c.step();c.rununtil('main');c.keys=set();c.setv('lives',2);c.setv('score3',7)
for lv in range(1,6):
 assert c.v('phase_id')==lv and c.v('lives')==2 and c.v('score3')==(7+lv-1)%10 and c.v('cheat_on')==1
 world=Image.open(P/f'terrain{lv}.png').convert('1').tobytes();assert c.logical()==world[-4608:]
 # Simulate boss defeat via actual shot collision, then native destruction.
 c.setv('boss',2);c.setv('boss_hp',1);c.setv('s0',70);c.setv('s0_y',100);c.call('collisions');assert c.v('boss')==3
 for _ in range(73):c.call('scroll_one')
 assert c.v('game_state')==2;c.pc=sy['end_game']
 if lv<5:
  c.rununtil('press_loop');assert c.screen()==(P/'assets/FASE_SUPERADA.scr').read_bytes();c.keys={'space'};c.rununtil('tape_release');c.keys=set();c.rununtil('main')
 else:
  c.rununtil('press_loop');assert c.screen()==(P/'assets/FINAL_FASE5.scr').read_bytes();assert c.tape_pos==len(c.blocks)
 print('campaign phase',lv,'boss destruction, screen and tape transition: PASS',flush=True)
# Actual DDA vectors; at nearest target crossing error <=2 pixels for all quadrants.
for tx,ty in [(24,24),(100,24),(165,24),(24,100),(165,100),(24,165),(100,165),(165,165),(110,110),(40,165),(165,40),(88,156)]:
 c=start(2);c.setv('player',tx-6);c.setv('player_y',ty-6);c.set16(0,100*256+100);c.call('fire_aim');assert c.v('b0_y')==100;steps=abs(max(abs(tx-100),abs(ty-100)))//2
 for _ in range(steps):c.call('move_b0')
 assert abs(c.v('b0')-tx)<=2 and abs(c.v('b0_y')-ty)<=2,(tx,ty,c.v('b0'),c.v('b0_y'))
print('DDA directed ball: 12 vectors all quadrants PASS',flush=True)
# Ensure every turret can fire actual balls in an uninterrupted no-kill encounter.
for lv in range(1,6):
 c=start(lv);last=[None]*4;counts=[0]*10;types={};table=c.m[sy['wave_table']:sy['wave_table']+160];actual=[];turrets=[];fired=set();last_b=[None]*2
 for t in range(1248):
  c.setv('tick',(t+1)&255);w=c.v('wave');c.call('waves_step')
  for j in range(4):
   x,y=c.v(f'e{j}'),c.v(f'e{j}_y');now=None if y==255 else (x,y)
   if now is not None and last[j] is None:
    counts[w]+=1;typ=c.v(f'e{j}_type');types[typ]=types.get(typ,0)+1;actual.append((w,j,typ));
    if lv>=2 and typ==2:turrets.append((w,j,t,x))
   if now is not None and last[j] is not None:
    assert abs(x-last[j][0])<=2 and abs(y-last[j][1])<=2,(lv,t,j,last[j],now)
    if c.v(f'e{j}_mode')==8:assert y-last[j][1]==2 and x==last[j][0]
   last[j]=now
  for j in range(2):c.call(f'move_b{j}')
  before=[c.v(f'b{j}_y') for j in range(2)];c.call('enemy_attack')
  for j in range(2):
   if before[j]==255 and c.v(f'b{j}_y')!=255:
    for w0,k,t0,x in turrets:
     if last[k] is not None and c.v(f'e{k}_type')==2 and c.v(f'b{j}')==x+7 and c.v(f'b{j}_y')==last[k][1]+8:fired.add((w0,k))
 expected=[sum(table[16*w+4*j+1]!=255 for j in range(4)) for w in range(10)];assert counts==expected,(lv,counts,expected)
 assert len(fired)==len(turrets),(lv,turrets,fired)
 print('stage',lv,'all waves',sum(counts),'types',types,'turrets fired',len(fired),'of',len(turrets),flush=True)
# Ground units reach y=190 then exit; render clips the bottom instead of wrapping.
c=start(3);c.setv('e0',64);c.setv('e0_y',190);c.setv('e0_mode',8);c.setv('e0_type',3);before=c.logical();c.call('draw_snapshot');c.call('restore_snapshot');assert c.logical()==before;c.call('waves_step');assert c.v('e0_y')==255;print('Ground exit and clipping PASS')
# tank resistance 4+ and collision correctness of all normal slots
for lv in range(1,6):
 c=start(lv);c.setv('cheat_on',1);c.setv('e0',64);c.setv('e0_y',80);c.setv('e0_type',4 if lv>=3 else 0);c.setv('s0',71);c.setv('s0_y',86);c.call('collisions');assert c.v('s0_y')==255
 if lv>=4:
  assert c.v('e0_type')==5 and c.v('e0_wait')==0;c.setv('s0',71);c.setv('s0_y',86);c.call('collisions');assert c.v('s0_y')==255
 assert c.v('e0_wait')==12 and c.v('score3')==1
 print('stage',lv,'collision/resistance PASS')
