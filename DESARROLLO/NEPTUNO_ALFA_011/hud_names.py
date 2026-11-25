"""Native 1bpp, variable-width compact lettering, 48 pixels inside the HUD frame."""
from PIL import Image
import numpy as np
NAMES=('MEDITERRANEO','GRECIA','SIRIA','FRANCIA','BARCELONA')
FONT={
'M':'10001/11011/10101/10101/10001/10001/10001','N':'1001/1101/1101/1011/1011/1001/1001','I':'1/1/1/1/1/1/1',
'E':'111/100/100/110/100/100/111','D':'110/101/101/101/101/101/110','T':'111/010/010/010/010/010/010',
'R':'110/101/101/110/101/101/101','A':'010/101/101/111/101/101/101','O':'010/101/101/101/101/101/010',
'G':'011/100/100/101/101/101/011','C':'011/100/100/100/100/100/011','S':'011/100/100/010/001/001/110',
'F':'111/100/100/110/100/100/100','B':'110/101/101/110/101/101/110','L':'100/100/100/100/100/100/111'}
def bitmap(level):
 glyphs=[np.array([[int(v) for v in row] for row in FONT[c].split('/')],dtype=np.uint8) for c in NAMES[level-1]]
 width=sum(g.shape[1] for g in glyphs)+len(glyphs)-1
 assert width<=48,(level,width)
 a=np.zeros((7,48),np.uint8);x=(48-width)//2
 for g in glyphs:a[:,x:x+g.shape[1]]=g;x+=g.shape[1]+1
 return np.packbits(a,axis=1).tobytes()
