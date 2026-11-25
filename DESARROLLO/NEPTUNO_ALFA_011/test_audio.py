"""Machine-code audio regression. ULA/IRQ approximate; no hardware listening claim."""
from test_cpu import *
from collections import Counter
import wave
# Actual notes from emitted code. Frame count and one-shot playback.
c=EngineCPU();c.rununtil('title_loop');s=c.cycles
for i in range(360):
 c.audio_events.clear();title_frame(c)
 if i==0: assert len(c.audio_events)>10
 if i==299: assert c.v('music_active')==0
 if i>=300: assert not c.audio_events,('music repeated',i)
assert c.v('music_active')==0
print('title original melody: one-shot, silent after end, 360 polls PASS',flush=True)
# Confirm that an early key starts the game and the two-down cheat still works.
c=start(1,True);assert c.v('cheat_on') and not c.v('music_active')
print('interruptible title + cheat PASS',flush=True)
# All effects on emitted CPU; low priority cannot interrupt higher priority.
for name,length in [('beep',4),('sfx_spread',5),('sfx_hit',3),('sfx_power',9),('boom',8),('sfx_heavy',12),('sfx_death',15),('sfx_boss',15)]:
 c=start(1);c.call(name);rank=c.v('sound')>>4;assert c.v('sound')&15==length
 if rank>1:c.call('beep');assert c.v('sound')>>4==rank
 transitions=0
 for i in range(length):
  # Approximate 13,000 idle T-states after game logic.
  c.cycles=(c.cycles//69888)*69888+56000
  c.audio_events.clear();ts=c.cycles;c.call('audio_wait');elapsed=c.cycles-ts
  assert 13888<=elapsed<=14250,(name,elapsed)
  assert c.audio_events[-1][1]==0 and len(c.audio_events)>4
  transitions+=len(c.audio_events)
 assert c.v('sound')==0
 print(name,length,'interrupts,',transitions,'port writes, priority and IRQ deadline PASS',flush=True)
# Confirm actual event routing, not just standalone sound functions.
c=start(1,True);c.setv('fire',1);c.call('logic');assert c.v('sound')>>4==1
c=start(1,True);c.setv('spread_lo',10);c.setv('fire',1);c.call('logic');assert c.v('sound')>>4==2
c=start(3,True);c.setv('e0',64);c.setv('e0_y',80);c.setv('e0_type',4);c.setv('e0_base',3)
for expect in [3,3,6]:
 c.setv('sound',0);c.setv('s0',71);c.setv('s0_y',86);c.call('collisions');assert c.v('sound')>>4==expect
c.call('lose_life');assert c.v('sound')>>4==7
c=start(1,True);c.setv('powerup',c.v('player'));c.setv('powerup_y',c.v('player_y'));c.call('power_collision');assert c.v('sound')>>4==4
c=start(1,True);c.setv('boss',2);c.setv('boss_hp',1);c.setv('s0',70);c.setv('s0_y',100);c.call('collisions');assert c.v('sound')>>4==8
print('actual shot, spread, heavy damage, destruction, death, pickup and boss routing PASS',flush=True)
