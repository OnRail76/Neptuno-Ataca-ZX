"""Native Z80 boot and tape-release guard. No BASIC polling of SPACE."""
import struct
class Emit:
 def __init__(self,org):self.org=org;self.b=bytearray();self.labels={};self.fix=[];self.lines=[f'ORG ${org:04X}']
 def label(self,n):self.labels[n]=self.org+len(self.b);self.lines.append(n+':')
 def e(self,s,*v):self.b.extend(v);self.lines.append('    '+s)
 def w(self,s,op,n):
  self.e(s,*op);i=len(self.b);self.b.extend(b'\0\0')
  if isinstance(n,str):self.fix.append((i,n))
  else:self.b[i:i+2]=struct.pack('<H',n)
 def jp(self,n,cond=''):self.w('jp '+(cond+',' if cond else '')+str(n),[{'':0xc3,'z':0xca,'nz':0xc2,'nc':0xd2}[cond]],n)
 def call(self,n):self.w('call '+str(n),[0xcd],n)
 def finish(self):
  for i,n in self.fix:self.b[i:i+2]=struct.pack('<H',self.labels[n])
  return bytes(self.b),'\n'.join(self.lines)+'\n'
BOOT=0xa200

def bootstrap():
 a=Emit(BOOT);e=a.e;w=a.w;l=a.label;j=a.jp;c=a.call
 # BASIC USR has valid SP and IY; use ROM IM1. No return on successful boot.
 e('im 1',0xed,0x56);e('ei',0xfb)
 def load(dest,n,flag):
  w('ld ix,'+str(dest),[0xdd,0x21],dest);w('ld de,'+str(n),[0x11],n)
  e('ld a,'+str(flag),0x3e,flag);e('scf',0x37);c(0x0556);j('error','nc')
 load('header',17,0);load(0x4000,6912,255)
 # Beep after the entire screen is loaded. No keyboard check by BASIC.
 e('di',0xf3);e('ld b,90',0x06,90);l('tone');e('ld a,16',0x3e,16);e('out ($fe),a',0xd3,0xfe);e('ld c,100',0x0e,100);l('hi');e('dec c',0x0d);j('hi','nz');e('xor a',0xaf);e('out ($fe),a',0xd3,0xfe);e('ld c,100',0x0e,100);l('lo');e('dec c',0x0d);j('lo','nz');e('dec b',0x05);j('tone','nz');e('ei',0xfb)
 # A held key from before the beep is not a new confirmation.
 l('initial_release');e('halt',0x76);c('fire');j('initial_release','nz')
 l('press');e('halt',0x76);c('fire');j('press','z')
 l('confirm');e('halt',0x76);c('fire');j('press','z')
 l('release_reset');e('ld d,8',0x16,8);l('release');e('halt',0x76);c('fire');j('release_reset','nz');e('dec d',0x15);j('release','nz')
 # Both SPACE and FIRE now released for eight IRQs before loading.
 l('load_engine');load('header',17,0);load(0x6000,0x3000,255);j(0x6000)
 l('fire');w('ld bc,$7ffe',[0x01],0x7ffe);e('in a,(c)',0xed,0x78);e('bit 0,a',0xcb,0x47);j('yes','z')
 w('ld bc,$001f',[0x01],31);e('in a,(c)',0xed,0x78);e('and $f0',0xe6,0xf0);e('cp $10',0xfe,0x10);j('no','nz');l('yes');e('ld a,1',0x3e,1);e('or a',0xb7);e('ret',0xc9);l('no');e('xor a',0xaf);e('ret',0xc9)
 l('error');e('ld a,2',0x3e,2);e('out ($fe),a',0xd3,0xfe);e('ei',0xfb);w('ld bc,0',[0x01],0);e('ret',0xc9)
 l('header');e('defs 17,0',*([0]*17));return a.finish(),a.labels

def guard(kernel,sy):
 # Patch ONLY the wait_press routine. Preserve all game addresses/timing.
 org=0x8e91;a=Emit(org);e=a.e;w=a.w;l=a.label;j=a.jp;c=a.call
 def poll():e('halt',0x76);c(sy['keys']);w('ld a,(fire)',[0x3a],sy['fire']);e('or a',0xb7)
 l('tape_press');poll();j('tape_press','z');l('tape_release_reset');e('ld d,8',0x16,8);l('tape_release');poll();j('tape_release_reset','nz');e('dec d',0x15);j('tape_release','nz');e('ret',0xc9)
 code,asm=a.finish();k=bytearray(kernel);idx=org-0x6000;assert not any(k[idx:idx+len(code)]);assert org+len(code)<0x8f00;k[idx:idx+len(code)]=code
 start=sy['press_loop']-0x6000;end=sy['reset_game']-0x6000;assert end-start==12 and k[end-1]==0xc9;k[start:end]=bytes([0xc3])+struct.pack('<H',org)+bytes(end-start-3)
 return bytes(k),asm,a.labels
