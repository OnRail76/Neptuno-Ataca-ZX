from pathlib import Path
p=Path('waves.py');s=p.read_text();a=s.index("data('wave_table'")
s=s[:a]+'''if LEVEL>=3:
 surface=np.frombuffer((A/f'surface{LEVEL}.bin').read_bytes(),np.uint8).reshape(96,24)
 # Pick continuous land corridors for moving troops; aim for spread and avoid water.
 # Ground enemies advance 2 px/tick, relative to 0.5 px/tick background.
 used={}
 def ground(w,delay,prefer,kind):
  y=576-(w*120+delay)//2; movement=kind in (3,4)
  y0=max(0,y//8);y1=min(96,(y+(145 if movement else 16)+7)//8)
  xs=[x for x in range(0,22) if np.all(surface[y0:min(96,y0+2),x:x+2]==2)]
  if not xs:return empty
  def cost(x):
   region=surface[y0:y1,x:x+2];water=np.count_nonzero(region==1);blocked=np.count_nonzero(region==0)
   return water*1000+blocked*12+abs(x*8-prefer)+sum(70 for q in used.get(w,[]) if abs(x-q)<2)
  x=min(xs,key=cost);used.setdefault(w,[]).append(x);return e(x*8,delay,8 if movement else 6,kind)
 def troops(w,types,prefs,delays=(0,8,16,24)):
  return [ground(w,d,x,k) for d,x,k in zip(delays,prefs,types)]
 if LEVEL==3:
  waves=[
   troops(0,[3]*4,[32,72,112,152]),
   [e(44,12,0),e(88,0,0,1),e(132,12,0),empty],
   troops(2,[4,3,3,4],[32,72,112,152]),
   [e(46,0,4,1),e(130,8,4,1),ground(3,0,24,2),empty],
   troops(4,[3,4,3,4],[24,64,104,144]),
   [e(86,0,1),e(86,12,1),e(86,24,1),empty],
   troops(6,[4,4,3,3],[24,64,104,144]),
   [e(16,0,2,1),e(150,10,3,1),ground(7,0,56,3),ground(7,16,120,4)],
   troops(8,[3,3,3,3],[24,64,104,144]),
   [e(38,12,0),e(88,0,0,1),e(138,12,0),e(88,24,0,1)],
  ]
 elif LEVEL==4:
  waves=[
   troops(0,[3,3,3,3],[16,48,136,160]),
   [e(16,0,2,1),e(40,10,2),e(150,0,3,1),e(126,10,3)],
   troops(2,[3,4,3,4],[16,48,136,160]),
   [e(46,0,4,1),e(130,8,4,1),ground(3,0,24,2),ground(3,24,152,2)],
   troops(4,[4,3,4,3],[16,48,136,160]),
   [e(82,0,1),e(82,10,1),e(82,20,1),e(82,30,1)],
   troops(6,[3,4,3,4],[16,48,136,160]),
   [e(24,0,5),e(64,8,5),e(112,16,5),e(152,24,5)],
   troops(8,[3,3,4,4],[16,48,136,160]),
   [e(16,0,2,1),e(40,10,2),e(150,0,3,1),e(126,10,3)],
  ]
 else:
  waves=[
   troops(0,[3,4,3,4],[16,48,80,112]),
   [e(38,12,0),e(88,0,0,1),e(138,12,0),e(88,24,0,1)],
   troops(2,[4,4,3,3],[16,48,80,112]),
   [e(32,0,4,1),e(132,8,4,1),ground(3,0,24,2),ground(3,24,104,2)],
   troops(4,[3,4,3,4],[16,48,80,112]),
   [e(16,0,2,1),e(38,8,2),e(150,0,3,1),e(128,8,3)],
   troops(6,[4,3,4,3],[16,48,80,112]),
   [e(24,0,5),e(64,6,5),e(112,12,5),e(152,18,5)],
   troops(8,[4,4,4,3],[16,48,80,112]),
   [e(86,0,1,1),e(86,8,1),e(86,16,1,1),e(86,24,1)],
  ]
 print('ground waves',LEVEL,waves)
''' + s[a:]
s=s.replace("for i in range(2):data(f'b{i}_dx',[0])", "for i in range(2):data(f'b{i}_dx',[0]);data(f'b{i}_dy',[2])")
# move clip_height into low area, new code with minimal cost fast common path; preserve HL/BC/DE
s=s.replace("exec((ROOT/'attack.py').read_text())", """L('clip_height');R('ld a,b');cp(177);ret('c');imm(192);R('sub b','push bc','ld b,a');la('draw_h');R('cp b');J('clip_keep','c');R('ld a,b');sa('draw_h');L('clip_keep');R('pop bc');ret()
exec((ROOT/'attack.py').read_text())""")
p.write_text(s)
