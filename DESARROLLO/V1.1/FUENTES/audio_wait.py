# Uncontended resident audio wait. The beeper uses ONLY the idle time which
# was formerly spent in HALT. IM2 sets a flag; the loop exits immediately.
# No stack tricks, no busy-wait inside the compositor or stack blitter.
# All effects leave port FE silent with black border.
L('irq_flag');data('irq_byte',[0]);data('noise_seed',[0xa7]);data('audio_kind',[0])
L('audio_noise');R('ld a,b','rrca');J('audio_noise_no_xor','nc');X('xor $b8',0xee,0xb8);L('audio_noise_no_xor');R('ld b,a');andi(31);X('add a,e',0x83);R('ld c,a');J('audio_toggle')
L('audio_tone');R('ld c,e');L('audio_toggle');R('ld a,d');X('xor 16',0xee,16);R('ld d,a');X('out ($fe),a',0xd3,0xfe)
L('audio_poll');la('irq_flag');R('or a');J('audio_done','nz');R('dec c');J('audio_poll','nz');la('audio_kind');cp(0x50);J('audio_noise','nc');cp(0x20);J('audio_noise','c');J('audio_tone')
L('audio_done');R('ld a,b');sa('noise_seed');R('xor a');X('out ($fe),a',0xd3,0xfe);ret()
L('audio_silent');R('halt');ret()
L('isr_audio');R('push af');imm(1);sa('irq_flag');R('pop af','ei');X('reti',0xed,0x4d)
L('music_tone');L('music_cycle');imm(16);X('out ($fe),a',0xd3,0xfe);R('ld c,d');L('music_hi');X('nop',0);X('nop',0);R('dec c');J('music_hi','nz');R('xor a');X('out ($fe),a',0xd3,0xfe);R('ld c,d');L('music_lo');X('nop',0);X('nop',0);R('dec c');J('music_lo','nz');R('dec b');J('music_cycle','nz');ret()
