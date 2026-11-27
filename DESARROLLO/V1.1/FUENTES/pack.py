"""Build both resident/data packets and assemble real ZX Spectrum TAP images."""
from pathlib import Path
import struct, functools, json, subprocess, sys, os
from loader import bootstrap, guard, BOOT
P=Path(__file__).resolve().parent; A=P/'assets'
for i in range(1,6):subprocess.run([sys.executable,str(P/'build.py')],check=True,env={**os.environ,'NEPTUNO_LEVEL':str(i)})
s1=json.loads((P/'symbols1.json').read_text());ks=[(P/f'kernel{i}.bin').read_bytes() for i in range(1,6)];k1=ks[0];x,y=[s1[s]-0x6000 for s in ('overlay_start','overlay_end')]
for i,k in enumerate(ks,1):
 assert s1==json.loads((P/f'symbols{i}.json').read_text()),i
 assert k1[:x]==k[:x] and k1[y:]==k[y:],i
k=k1[:x]+bytes(y-x)+k1[y:];k,asm,guard_labels=guard(k,s1);(P/'kernel.bin').write_bytes(k);(P/'tape_guard.asm').write_text(asm);(P/'symbols.json').write_text(json.dumps({**s1,**guard_labels},indent=2))
for i,ki in enumerate(ks,1):(P/f'overlay{i}.bin').write_bytes(ki[x:y])
def block(flag,p):
 q=bytes([flag])+p;return struct.pack('<H',len(q)+1)+q+bytes([functools.reduce(int.__xor__,q,0)])
def header(t,n,l,p1,p2):return block(0,bytes([t])+n.encode().ljust(10,b' ')[:10]+struct.pack('<HHH',l,p1,p2))
def num(n):return str(n).encode()+bytes([14,0,0,n&255,n>>8,0])
def line(n,s):return struct.pack('>H',n)+struct.pack('<H',len(s)+1)+s+b'\r'
# BASIC merely loads and enters the native bootstrap before screen loading.
program=b''.join([line(10,bytes([0xe7])+num(0)+b':'+bytes([0xda])+num(0)+b':'+bytes([0xd9])+num(7)+b':'+bytes([0xfd])+num(24575)),line(20,bytes([0xef])+b'""'+bytes([0xaf])),line(30,bytes([0xf9,0xc0])+num(BOOT))])
(boot,bootasm),bootlabels=bootstrap();(P/'bootstrap.bin').write_bytes(boot);(P/'bootstrap.asm').write_text(bootasm);(P/'bootstrap_symbols.json').write_text(json.dumps(bootlabels,indent=2))
def screen(name,f):
 r=(A/f).read_bytes();assert len(r)==6912;return header(3,name,len(r),0x4000,0)+block(255,r)
prefix=header(0,'NEPTUNO',len(program),10,len(program))+block(255,program)+header(3,'ARRANQUE',len(boot),BOOT,0)+block(255,boot)+screen('CARGA','CARGA.scr')+header(3,'ENGINE',len(k),0x6000,0)+block(255,k)
def phase(i):return block(255,(P/f'overlay{i}.bin').read_bytes())+block(255,(P/f'phase{i}.bin').read_bytes())
for i,name in enumerate(['NEPTUNO_ATACA_V1.1.tap','NEPTUNO_ATACA_GRECIA_V1.1.tap','NEPTUNO_ATACA_SIRIA_V1.1.tap','NEPTUNO_ATACA_FRANCIA_V1.1.tap','NEPTUNO_ATACA_BARCELONA_V1.1.tap'],1):
 data=prefix+header(3,'INICIO',y-x,s1['overlay_start'],0)+phase(i)+screen('TITULO','TITULO.scr')+b''.join(phase(j) for j in range(i+1,6))+screen('FINAL','FINAL_FASE5.scr')
 (P/name).write_bytes(data);j=0;out=[]
 while j<len(data):
  n=int.from_bytes(data[j:j+2],'little');j+=2;blk=data[j:j+n];j+=n;assert len(blk)==n and functools.reduce(int.__xor__,blk,0)==0;out.append((blk[0],n-2))
 assert j==len(data);print(name,len(data),out)
