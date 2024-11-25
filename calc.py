import numpy as np

confs=np.loadtxt("confs.dat")
magn1=np.sum(confs,axis=1)
magn2=np.roll(magn1,-1,axis=0)
returns=(magn2-magn1)/2
returns=returns[:-1]
np.savetxt("returns.dat",returns)
