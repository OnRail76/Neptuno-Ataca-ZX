from test_cpu import EngineCPU, tape_blocks, P, sy
import json,struct,hashlib
from loader import BOOT, bootstrap, guard
boot_sy=json.loads((P/'bootstrap_symbols.json').read_text())
# Verify new TAP block structure, checksums and loader payloads.
for name in sorted(P.glob('*_V1.1.tap')):
 blocks=tape_blocks(name)
 assert len(blocks) in (15,17,19,21,23)
 assert blocks[7][1:-1]==(P/'kernel.bin').read_bytes()
 assert blocks[3][1:-1]==(P/'bootstrap.bin').read_bytes()
 assert int.from_bytes(blocks[2][14:16],'little')==BOOT
 assert blocks[5][1:-1]==(P/'assets/CARGA.scr').read_bytes()
 assert blocks[12][1:-1]==(P/'assets/TITULO.scr').read_bytes()
 print(name.name,'checksums, loader and screens PASS')
# Boot from the exact TAP data loaded by BASIC. ROM LD-BYTES is mocked by EngineCPU.
for lv in (1,2):
 for mode in ('space','kempston'):
  c=EngineCPU(lv);c.m[BOOT:BOOT+len(c.blocks[3])-2]=c.blocks[3][1:-1];c.pc=BOOT;c.sp=0x5f00;c.tape_pos=4;c.joy=255 if mode=='space' else 0
  # simulated held button prior to beep, then release
  def setfire(down):
   c.keys={'space'} if down and mode=='space' else set();c.joy=(16 if down else 0) if mode=='kempston' else 255
  setfire(True);c.rununtil(boot_sy['initial_release']);assert c.screen()==(P/'assets/CARGA.scr').read_bytes() and c.tape_pos==6
  assert len(c.border)==180
  for i in range(5):c.step();c.rununtil(boot_sy['initial_release'])
  setfire(False);c.rununtil(boot_sy['press']);assert c.tape_pos==6
  # invalid bus readings and idle do not confirm
  for v in (255,240,0,4):
   c.joy=v;c.step();c.rununtil(boot_sy['press']);assert c.tape_pos==6
  setfire(True);c.rununtil(boot_sy['release']);assert c.tape_pos==6
  for i in range(15):c.step();c.rununtil(boot_sy['release']);assert c.tape_pos==6
  setfire(False);n=c.cycles;c.rununtil(0x6000);assert c.tape_pos==8 and c.cycles-n>=7*69888
  c.rununtil('title_loop');assert c.screen()==(P/'assets/TITULO.scr').read_bytes() and c.v('phase_id')==lv and c.tape_pos==13
  print('Boot stage',lv,mode,'hold/release, BEEP, title: PASS')
# Test phase-transition guard with a held press.
for mode in ('space','kempston'):
 c=EngineCPU(1);c.rununtil('title_loop');c.setv('game_state',2);c.pc=sy['end_game'];c.rununtil('press_loop');c.keys={'space'} if mode=='space' else set();c.joy=16 if mode=='kempston' else 0;c.rununtil('tape_release')
 for _ in range(12):c.step();c.rununtil('tape_release');assert c.tape_pos==13
 c.keys=set();c.joy=0;c.rununtil('main');assert c.tape_pos==15 and c.v('phase_id')==2
 print('Phase change',mode,'held key does not start ROM load: PASS')
