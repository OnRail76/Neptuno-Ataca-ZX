# Audio event queue and original one-shot title tune (single-channel beeper).
# Event state: upper nibble = priority/timbre; lower nibble = remaining IRQs.
# Request never blocks, preserves BC. No change to game logic or renderer.
for name,value in [('beep',0x14),('sfx_spread',0x25),('sfx_hit',0x33),('sfx_power',0x49),('boom',0x58),('sfx_heavy',0x6c),('sfx_death',0x7f),('sfx_boss',0x8f)]:
 L(name);imm(value);J('sfx_request')
L('sfx_request');R('push bc','ld b,a');la('sound');andi(240);R('cp b');J('sfx_keep','nc');R('ld a,b');sa('sound');L('sfx_keep');R('pop bc');ret()
# Title and victory melody are original, note events stepped once per interrupt.
# Each record: frame duration, half-period delay, number of periods per frame.
# A note occupies <~16 ms, leaving time for input and interrupts.
import math

def tune_bytes(notes):
 out=[]
 for midi,frames in notes:
  if midi is None:out.extend((frames,0,0));continue
  f=440*2**((midi+12-69)/12)
  # inner delay is DEC C (4) + JP NZ (10), approx 44*C+62 T per cycle (two NOPs per half-period)
  c=max(1,min(255,round((3500000/f-62)/44)))
  periods=max(1,min(255,int(48000/(44*c+62))))
  out.extend((frames,c,periods))
 return out+[0,0,0]
# D minor, heroic chromatic arcade march, original single-channel tune.
notes=[(62,10),(62,6),(65,10),(69,16),(None,4),(67,10),(65,10),(62,14),(57,10),(60,10),(62,12),(65,12),(None,4),(69,10),(69,6),(72,10),(74,16),(None,4),(72,10),(69,10),(67,10),(65,10),(64,10),(65,10),(69,10),(74,26),(None,4)]
victory=[(62,7),(65,7),(69,7),(74,20),(72,7),(74,20),(None,4)]
data('title_music',tune_bytes(notes));data('victory_music',tune_bytes(victory));data('music_ptr',[0,0]);data('music_frames',[0]);data('music_delay',[0]);data('music_periods',[0]);data('music_active',[0])
L('music_start');shm('music_ptr');zero('music_frames');setv('music_active',1);ret()
L('music_tick');la('music_active');R('or a');ret('z');la('music_frames');R('or a');J('music_play','nz');lhm('music_ptr');R('ld a,(hl)','inc hl','or a');J('music_stop','z');sa('music_frames');R('ld a,(hl)','inc hl');sa('music_delay');R('ld a,(hl)','inc hl');sa('music_periods');shm('music_ptr')
L('music_play');decv('music_frames');la('music_periods');R('or a');ret('z');R('ld b,a');la('music_delay');R('ld d,a');J('music_tone')
L('music_stop');zero('music_active');ret()
# Music runs ONLY outside the renderer, with IM2 active and normal stack.
L('audio_wait');la('sound');R('or a');J('audio_silent','z');R('ld b,a');zero('irq_flag');R('ld a,b');sa('audio_kind');andi(15);R('dec a');J('audio_last','z');R('ld a,b','dec a');sa('sound');J('audio_prepare')
L('audio_last');zero('sound')
L('audio_prepare');R('ld a,b');andi(15);R('ld c,a');imm(16);R('sub c','ld c,a');R('ld a,b');andi(240);cp(0x50);J('audio_noise_setup','nc');cp(0x40);J('audio_power_setup','z');cp(0x30);J('audio_hit_setup','z');cp(0x20);J('audio_spread_setup','z');J('audio_noise_setup')
L('audio_spread_setup');R('ld a,c','add a,a');add(10);J('audio_tone_setup')
L('audio_hit_setup');imm(5);J('audio_tone_setup')
L('audio_power_setup');R('ld a,b');andi(15);R('add a,a','add a,a');add(8);J('audio_tone_setup')
L('audio_noise_setup');R('ld a,c','add a,a');add(4);R('ld e,a','ld a,b');andi(240);R('rrca','rrca','rrca','rrca','add a,a');X('add a,e',0x83);R('ld e,a');la('noise_seed');R('ld b,a','ld d,0');J('audio_noise')
L('audio_tone_setup');R('ld e,a','ld d,0');J('audio_tone')
