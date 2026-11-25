"""Headless instruction-level smoke test of the emitted Z80 subset.
Not a Spectrum emulator: no ULA contention, ROM, display timing or audio.
HALT/FRAMES and keyboard ports are modelled to exercise game logic.
"""
from pathlib import Path
import json,struct,functools
P=Path(__file__).parent; sy=json.loads((P/'symbols.json').read_text());code=(P/'kernel.bin').read_bytes();org=0x6000
class CPU:
 def __init__(self):
  self.m=bytearray(65536);self.m[org:org+len(code)]=code;self.r=[0]*8;self.pc=org;self.sp=0;self.ix=0;self.f=0;self.t=0;self.keys=set();self.halts=0;self.stop=None
 def read(self,n):return self.m[n&65535]
 def write(self,n,v):
  n&=65535
  assert n>=0x4000,('write to ROM',hex(n),hex(self.pc));self.m[n]=v&255
 def fetch(self):a=self.read(self.pc);self.pc=(self.pc+1)&65535;return a
 def word(self):a=self.fetch();return a+256*self.fetch()
 def get16(self,i):return self.sp if i==3 else (self.r[2*i]<<8)|self.r[2*i+1]
 def set16(self,i,n):
  n&=65535
  if i==3:self.sp=n
  else:self.r[2*i]=n>>8;self.r[2*i+1]=n&255
 def get(self,i):return self.read(self.get16(2)) if i==6 else self.r[i]
 def set(self,i,v):
  if i==6:self.write(self.get16(2),v)
  else:self.r[i]=v&255
 def push(self,n):self.sp=(self.sp-2)&65535;self.write(self.sp,n);self.write(self.sp+1,n>>8)
 def pop(self):n=self.read(self.sp)+256*self.read(self.sp+1);self.sp=(self.sp+2)&65535;return n
 def fl(self,n,c=0):self.f=(0x40 if not n&255 else 0)|(0x80 if n&128 else 0)|(c&1)
 def cond(self,i):return [not self.f&64,bool(self.f&64),not self.f&1,bool(self.f&1),not self.f&4,bool(self.f&4),not self.f&128,bool(self.f&128)][i]
 def frames(self,n=1):
  v=(int.from_bytes(self.m[23672:23675],'little')+n)&0xffffff;self.m[23672:23675]=v.to_bytes(3,'little')
 def addt(self,n):
  self.t+=n
  if self.t>=69888:q,self.t=divmod(self.t,69888);self.frames(q)
 def alu(self,k,v):
  a=self.r[7]
  if k==0:n=a+v;self.fl(n,n>255)
  elif k==2 or k==7:n=a-v;self.fl(n,n<0)
  elif k==4:n=a&v;self.fl(n)
  elif k==5:n=a^v;self.fl(n)
  elif k==6:n=a|v;self.fl(n)
  else:raise Exception(('alu',k))
  if k!=7:self.r[7]=n&255
 def step(self):
  pc=self.pc;o=self.fetch();self.addt(4)
  if o==0x76:self.frames();self.t=0;self.halts+=1;return 'halt'
  if 0x40<=o<0x80:self.set((o>>3)&7,self.get(o&7));self.addt(3 if (o&7)==6 or (o>>3)&7==6 else 0);return
  if 0x80<=o<0xc0:self.alu((o>>3)&7,self.get(o&7));return
  if o&0xc7==0x06:self.set((o>>3)&7,self.fetch());self.addt(3);return
  if o&0xc7 in (0x04,0x05):i=(o>>3)&7;v=(self.get(i)+(1 if o&7==4 else -1))&255;self.set(i,v);self.fl(v,self.f&1);return
  if o&0xcf==1:self.set16((o>>4)&3,self.word());self.addt(6);return
  if o&0xcf in (3,0xb):i=(o>>4)&3;self.set16(i,self.get16(i)+(1 if o&15==3 else -1));return
  if o&0xcf==9:n=self.get16(2)+self.get16((o>>4)&3);self.set16(2,n);self.f=(self.f&0xc0)|(n>65535);return
  if o in (0x3a,0x32,0x2a,0x22):n=self.word();self.addt(9)
  if o==0x3a:self.r[7]=self.read(n);return
  if o==0x32:self.write(n,self.r[7]);return
  if o==0x2a:self.set16(2,self.read(n)+256*self.read(n+1));return
  if o==0x22:v=self.get16(2);self.write(n,v);self.write(n+1,v>>8);return
  if o in (0x1a,0x12):
   if o==0x1a:self.r[7]=self.read(self.get16(1))
   else:self.write(self.get16(1),self.r[7])
   return
  if o==0x2f:self.r[7]^=255;return
  if o in (7,15):a=self.r[7];c=(a>>7 if o==7 else a&1);self.r[7]=((a<<1)|c)&255 if o==7 else (a>>1)|(c<<7);self.f=(self.f&0xc0)|c;return
  if o==0xeb:a=self.get16(1);self.set16(1,self.get16(2));self.set16(2,a);return
  if o in (0xf3,0xfb):return
  if o==0xd3:self.fetch();return
  if o==0xc3:self.pc=self.word();return
  if o&0xc7==0xc2:n=self.word();self.pc=n if self.cond((o>>3)&7) else self.pc;return
  if o==0xcd:n=self.word();self.push(self.pc);self.pc=n;self.addt(13);return
  if o==0xc9:self.pc=self.pop();self.addt(6);return
  if o&0xc7==0xc0:
   if self.cond((o>>3)&7):self.pc=self.pop()
   return
  if o&0xcf==0xc5:i=(o>>4)&3;self.push((self.r[7]<<8)|self.f if i==3 else self.get16(i));return
  if o&0xcf==0xc1:
   i=(o>>4)&3;n=self.pop()
   if i==3:self.r[7]=n>>8;self.f=n&255
   else:self.set16(i,n)
   return
  if o&0xc7==0xc6:self.alu((o>>3)&7,self.fetch());return
  if o==0xcb:k=self.fetch();assert k&0xc0==0x40;v=self.get(k&7);self.f=(self.f&1)|(0 if v&(1<<((k>>3)&7)) else 64);return
  if o==0xdd:
   k=self.fetch()
   if k==0xe1:self.ix=self.pop();return
   if k==0xe5:self.push(self.ix);return
   if k==0x23:self.ix=(self.ix+1)&65535;return
   if k in (0xa6,0xb6,0x7e):v=self.read(self.ix+self.fetch());self.addt(15)
   if k==0x77:self.write(self.ix+self.fetch(),self.r[7]);return
   if k==0x36:off=self.fetch();self.write(self.ix+off,self.fetch());return
   if k==0xa6:self.alu(4,v);return
   if k==0xb6:self.alu(6,v);return
   if k==0x7e:self.r[7]=v;return
   raise Exception(('DD',hex(k),hex(pc)))
  if o==0xed:
   k=self.fetch()
   if k==0x56:return
   if k==0x78:
    p=self.get16(0);a=255
    for port,key,bit in [(0xfbfe,'q',0),(0xfdfe,'a',0),(0xdffe,'o',1),(0xdffe,'p',0),(0x7ffe,'space',0)]:
     if port==p and key in self.keys:a&=~(1<<bit)
    if p&255==31:a=0
    self.r[7]=a;self.fl(a,self.f&1);return
   if k in (0x42,0x52):n=self.get16(2)-self.get16(0 if k==0x42 else 1)-(self.f&1);self.set16(2,n);self.f=(64 if n&65535==0 else 0)|(128 if n&32768 else 0)|(n<0);return
   if k in (0xa0,0xb0):
    n=1 if k==0xa0 else self.get16(0) or 65536;h=self.get16(2);d=self.get16(1)
    # forward bytewise, supports LDIR overlaps
    for _ in range(n):self.write(d,self.read(h));d=(d+1)&65535;h=(h+1)&65535
    self.set16(2,h);self.set16(1,d);self.set16(0,self.get16(0)-n);self.addt(n*(16 if k==0xa0 else 21));return
   raise Exception(('ED',hex(k),hex(pc)))
  raise Exception(('unknown opcode',hex(o),hex(pc)))
 def rununtil(self,name,limit=2000000):
  t=sy[name]
  for _ in range(limit):
   if self.pc==t:return
   self.step()
  raise Exception(('limit',name,hex(self.pc)))
 def v(self,n):return self.m[sy[n]]
 def setv(self,n,v):self.m[sy[n]]=v
 def one_loop(self,keys=()):
  assert self.pc==sy['loop'];self.keys=set(keys);self.step();self.rununtil('loop')
 def screen(self):return bytes(self.m[0x4000:0x5b00])
# Additional Z80 subset, exact nominal instruction timings for this binary.
# ROM tape operation is stubbed; this is not a full ULA emulator.
from collections import Counter
class EngineCPU(CPU):
 def __init__(self,level=1):
  super().__init__();self.alt=[0]*6;self.iy=0;self.i=0;self.cycles=0;self.halt_times=[];self.video_writes=[];self.border=[];self.audio_events=[];self.phase=(P/f'phase{level}.bin').read_bytes();self.joy=0;self.blocks=tape_blocks(P/(['NEPTUNO_ATACA_011.tap','NEPTUNO_ATACA_GRECIA_011.tap','NEPTUNO_ATACA_SIRIA_011.tap','NEPTUNO_ATACA_FRANCIA_011.tap','NEPTUNO_ATACA_BARCELONA_011.tap'][level-1]));self.tape_pos=8;self.time_mode=True;self.contend=True
 def addt(self,n):pass
 def wrdelay(self,t):
  q=t%69888-14335
  if 0<=q<192*224 and q%224<128:return (6,5,4,3,2,1,0,0)[q%8]
  return 0
 def step(self):
  pc=self.pc;o=self.m[pc];k=self.m[(pc+1)&65535];t=self.cycles
  if pc==0x0556:
   assert self.f&1;assert self.tape_pos<len(self.blocks),('tape exhausted',self.tape_pos);blk=self.blocks[self.tape_pos];self.tape_pos+=1;size=self.get16(1);flag=self.r[7]
   if blk[0]==flag and len(blk)==size+2:
    self.m[self.ix:self.ix+size]=blk[1:-1];self.f|=1
   else:self.f&=~1
   self.pc=self.pop();self.cycles+=100;return
  if o==0x76:
   self.pc+=1;self.cycles=(self.cycles//69888+1)*69888+88;self.m[sy["irq_flag"]]=1;self.halt_times.append(self.cycles);return
  # compute base timing before execution, including branch conditions
  if 0x40<=o<0x80:n=7 if (o&7)==6 or (o>>3)&7==6 else 4
  elif 0x80<=o<0xc0:n=7 if (o&7)==6 else 4
  elif o&0xc7==0x06:n=10 if (o>>3)&7==6 else 7
  elif o&0xc7 in (0x04,0x05):n=11 if (o>>3)&7==6 else 4
  elif o&0xcf==1:n=10
  elif o&0xcf in (3,0xb):n=6
  elif o&0xcf==9:n=11
  elif o in (0x3a,0x32):n=13
  elif o in (0x2a,0x22):n=16
  elif o in (0x1a,0x12,0x02,0x0a):n=7
  elif o in (0x07,0x0f,0xeb,0xf3,0xfb,0xd9,0x37,0x2f,0x00):n=4
  elif o==0xd3:n=11
  elif o==0xc3 or o&0xc7==0xc2:n=10
  elif o==0xcd:n=17
  elif o==0xc9:n=10
  elif o&0xc7==0xc0:n=11 if self.cond((o>>3)&7) else 5
  elif o&0xcf==0xc5:n=11
  elif o&0xcf==0xc1:n=10
  elif o&0xc7==0xc6:n=7
  elif o==0xcb:n=8
  elif o in (0xdd,0xfd):n=14 if k==0x21 else 15 if k==0xe5 else 19 if k in (0x7e,0x77,0x36,0xa6,0xb6) else 10 if k==0x23 else 14
  elif o==0xed:
   if k in (0x56,0x5e):n=8
   elif k==0x47:n=9
   elif k in (0x42,0x52):n=15
   elif k in (0x4b,0x5b,0x73,0x7b,0x53):n=20
   elif k==0x78:n=12
   elif k in (0xa0,0xb0):n=16 if k==0xa0 else 21*((self.get16(0) or 65536)-1)+16
   elif k==0x4d:n=14
   else:raise AssertionError(('ED timing',hex(k),hex(pc)))
  else:raise AssertionError(('timing',hex(o),hex(pc)))
  # approximate ULA delay on actual contended memory accesses; exact push write timing
  # (all stack-blast instructions and data reads execute in uncontended RAM).
  delay=0
  if o&0xcf==0xc5 and 0x4000<=self.sp-2<0x8000:
   if self.contend:delay=self.wrdelay(t+5);delay+=self.wrdelay(t+8+delay)
   if self.sp<=0x5800:self.video_writes.extend([(self.sp-1,t+5),(self.sp-2,t+8+delay)])
  elif o in (0x3a,0x32,0x2a,0x22) or o==0xed and k in (0x4b,0x5b,0x73,0x7b,0x53):
   a=int.from_bytes(self.m[pc+(2 if o==0xed else 1):pc+(4 if o==0xed else 3)],'little')
   if self.contend and 0x4000<=a<0x8000:
    delay=self.wrdelay(t+10 if o!=0xed else t+14)
    if o in (0x2a,0x22) or o==0xed:delay+=self.wrdelay(t+(13 if o!=0xed else 17)+delay)
  elif 0x40<=o<0xc0 and ((o&7)==6 or (o<0x80 and (o>>3)&7==6)):
   if self.contend and 0x4000<=self.get16(2)<0x8000:delay=self.wrdelay(t+4)
  if o in (0x02,0x0a):
   self.pc+=1
   if o==0x02:self.write(self.get16(0),self.r[7])
   else:self.r[7]=self.read(self.get16(0))
  elif o==0xd9:self.pc+=1;self.r[:6],self.alt=self.alt,self.r[:6]
  elif o==0x37:self.pc+=1;self.f|=1
  elif o==0x00:self.pc+=1
  elif o in (0xdd,0xfd) and k==0x21:
   self.pc+=2;v=self.word();self.ix=v if o==0xdd else self.ix;self.iy=v if o==0xfd else self.iy
  elif o==0xed and k in (0x4b,0x5b,0x73,0x7b,0x53):
   self.pc+=2;a=self.word()
   if k in (0x4b,0x5b,0x7b):self.set16({0x4b:0,0x5b:1,0x7b:3}[k],self.read(a)+256*self.read(a+1))
   else:
    v=self.sp if k==0x73 else self.get16(1);self.write(a,v);self.write(a+1,v>>8)
  elif o==0xed and k in (0x47,0x5e,0x4d):
   self.pc+=2
   if k==0x47:self.i=self.r[7]
   if k==0x4d:self.pc=self.pop()
  elif o==0xed and k==0x78 and self.get16(0)&255==31:
   self.pc+=2;self.r[7]=self.joy;self.fl(self.joy,self.f&1)
  else:
   if o==0xd3:self.border.append(self.r[7]);self.audio_events.append((self.cycles,self.r[7]));
   super().step()
  self.cycles+=n+delay
  # Model the IM2 flag and its 88 T response during the interruptible wait.
  if t//69888!=self.cycles//69888 and (sy['audio_noise']<=pc<sy['isr_audio'] or sy['audio_wait']<=pc<sy['audio_tone_setup']+12):
   self.m[sy['irq_flag']]=1;self.cycles+=88;self.halt_times.append(self.cycles)
 def rununtil(self,name,limit=1000000):
  addr=sy[name] if isinstance(name,str) else name
  for _ in range(limit):
   if self.pc==addr:return
   self.step()
  raise AssertionError(('limit',name,hex(self.pc)))
 def call(self,name):
  sp=self.sp;self.push(0x2222);self.pc=sy[name];self.rununtil(0x2222);assert self.sp==sp
 def logical(self,base=0x9000):
  p=self.v('head')*24;raw=self.m[base:base+4608];return bytes(raw[p:]+raw[:p])
 def video(self):return b''.join(self.m[0x4000+((y&192)<<5)+((y&7)<<8)+((y&56)<<2):0x4000+((y&192)<<5)+((y&7)<<8)+((y&56)<<2)+24] for y in range(192))

def tape_blocks(path):
 data=path.read_bytes();i=0;out=[]
 while i<len(data):
  n=int.from_bytes(data[i:i+2],'little');i+=2;b=data[i:i+n];i+=n;assert len(b)==n and functools.reduce(int.__xor__,b,0)==0;out.append(b)
 assert i==len(data);return out
from PIL import Image

def title_frame(c,keys=(),joy=0):
 assert c.pc==sy['title_loop'];c.keys=set(keys);c.joy=joy;c.step();c.rununtil('title_loop')
def start(level=1,cheat=False):
 c=EngineCPU(level);c.rununtil('title_loop');assert c.screen()==(P/'assets/TITULO.scr').read_bytes();title_frame(c)
 if cheat:
  for keys in [('a',),('a',),(),('a',),(),('space',)]:title_frame(c,keys)
  assert c.v('cheat_on')==1;title_frame(c)
 c.keys={'space'};c.step();c.rununtil('main');c.keys=set();assert c.sp==0x9000 and c.v('phase_id')==level;return c
