from test_cpu import *
import copy,sys
from PIL import Image
# Verify title presses, cheat, collisions, and real data-block transition.
c=start(1,True);assert c.v('cheat_on')==1 and len(c.border)>100
for j in range(4):c.setv(f'e{j}',c.v('player'));c.setv(f'e{j}_y',c.v('player_y'))
c.setv('invul',0);c.call('collisions');assert c.v('lives')==3 and c.v('death')==0
c.setv('lives',2);c.setv('score3',7);c.setv('game_state',2);c.pc=sy['end_game'];c.rununtil('press_loop');c.keys={'space'};c.rununtil('tape_release');c.keys=set();c.rununtil('main');assert c.v('phase_id')==2 and c.v('cheat_on')==1 and c.v('lives')==2 and c.v('score3')==7 and c.tape_pos==15
assert c.logical()==Image.open(P/'terrain2.png').convert('1').tobytes()[-4608:]
print('Cheat, 150-HALT result, campaign transition, carried lives/score/cheat, correct Greece map: PASS',flush=True)
# restart via tape rewind
c.setv('game_state',1);c.pc=sy['end_game'];c.keys=set();c.rununtil('press_loop');c.tape_pos=0;c.keys={'space'};c.rununtil('tape_release');c.keys=set();c.rununtil('title_loop');assert c.screen()==(P/'assets/TITULO.scr').read_bytes() and c.v('cheat_on')==0;print('Rewind to start and new title: PASS',flush=True)
# normal loss, explosion and respawn.
c=start();c.call('lose_life');assert c.v('lives')==2 and c.v('death')==1
for i in range(39):c.call('logic');assert c.v('death')==1
c.call('logic');assert c.v('death')==2
for i in range(34):c.call('logic');assert c.v('death')==2
c.call('logic');assert c.v('death')==0 and c.v('invul')==150
print('Normal death/respawn: PASS',flush=True)
# all scheduled spawns and trajectories, direct native routines
for lv in (1,2):
 c=start(lv);count=[0]*10;last=[None]*4;ground=[]
 for t in range(1248):
  c.setv('tick',(t+1)&255);w=c.v('wave');c.call('waves_step')
  for j in range(4):
   x,y=c.v(f'e{j}'),c.v(f'e{j}_y');now=None if y==255 else (x,y)
   if now is not None and last[j] is None:
    assert y==0 and w<10;count[w]+=1
    if c.v(f'e{j}_mode')==6:ground.append((t,x))
   if now is not None and last[j] is not None:assert abs(x-last[j][0])<=2 and abs(y-last[j][1])<=2,(lv,t,j,last[j],now)
   last[j]=now
 expected=[4,3,2,4,4,3,2,2,4,4] if lv==1 else [3,4,2,2,4,2,2,3,4,4]
 assert count==expected,(lv,count,expected)
 print('Stage',lv,'waves',count,'total',sum(count),'ground',ground,flush=True)
 if lv==2:
  import numpy as np
  surface=np.frombuffer((P/'assets/grecia_spawn.bin').read_bytes(),np.uint8).reshape(96,24);surface=np.repeat(np.repeat(surface,8,0),8,1)
  for t,x in ground:
   y=576-t//2;assert np.all(surface[y:y+16,x:x+16]==2),(t,x,y)
 for hp in ([20,15,10,5] if lv==1 else [28,22,15,7]):
  c=start(lv);c.setv('boss',2);c.setv('boss_hp',hp);c.setv('tick',0);c.call('enemy_attack');assert c.v('b0_y')!=255;print('boss',lv,hp,c.v('b0'),c.v('b0_dx'),c.v('b1_y'),flush=True)
 c=start(lv);c.setv('boss',2);c.setv('boss_hp',1);c.setv('invul',150);c.setv('s0',70);c.setv('s0_y',100);c.call('collisions');assert c.v('boss')==3
 for _ in range(73):c.call('scroll_one')
 assert c.v('game_state')==2
 print('boss destruction',lv,'PASS',flush=True)
# Kempston: down held cannot count twice, fire held cannot start after confirmation.
c=EngineCPU(1);c.rununtil('title_loop');title_frame(c)
for j in [4,4,0,4,0,16]:title_frame(c,joy=j)
assert c.v('cheat_on')==1 and c.v('joymode')==1;title_frame(c,joy=16);title_frame(c,joy=0);c.joy=16;c.step();c.rununtil('main');assert c.v('cheat_on')==1
print('Kempston cheat with release detection: PASS',flush=True)
c=start(1);c.setv('powerup',c.v('player'));c.setv('powerup_y',c.v('player_y'));c.call('power_collision');assert c.v('spread_hi')==1 and c.v('spread_lo')==244
for j in range(6):c.setv(f's{j}_y',255)
c.setv('fire',1);c.setv('cool',0);c.call('logic');assert all(c.v(f's{j}_y')!=255 for j in (0,1,2));c.setv('fire',0)
for i in range(499):c.setv('invul',150);c.call('logic')
assert c.v('spread_lo')==0 and c.v('spread_hi')==0;print('SPREAD 500 ticks: PASS',flush=True)
for lv in (1,2):
 base=start(lv)
 for enemy in range(4):
  for shot in range(6):
   c=copy.deepcopy(base);c.setv('cheat_on',1)
   for j in range(4):c.setv(f'e{j}',32+j*40);c.setv(f'e{j}_y',80);c.setv(f'e{j}_wait',0)
   ex=c.v(f'e{enemy}');c.setv(f's{shot}',ex+7);c.setv(f's{shot}_y',86);before=[(c.v(f'e{j}'),c.v(f'e{j}_y')) for j in range(4)];c.call('collisions');assert c.v(f'e{enemy}_wait')==12 and c.v(f's{shot}_y')==255 and c.v('score3')==1;assert all((c.v(f'e{j}'),c.v(f'e{j}_y'))==before[j] for j in range(4))
 print('Stage',lv,'24 collision combinations PASS',flush=True)
