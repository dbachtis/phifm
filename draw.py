import numpy as np
import PIL
from PIL import Image

def normal(x):
    return (x-np.min(x))/(np.max(x)-np.min(x))

confs=np.loadtxt("confs.dat")
L=int(np.sqrt(confs.shape[1]))

for i in range(confs.shape[0]):
  a=confs[i,:]
  a=np.reshape(a,(L,L))
  a=normal(a)*255
  im = Image.fromarray(a)
  s = PIL.Image.fromarray(a).convert('L')
  s.save( './draw/im'+str(i)+'.jpg' )
