import numpy as np

L=64
N=L*L

mu=2.0-1.8/2.0
lambd=0.1/4.0
alpha=4.0

sweeps=1000001
thermalization=10000
std=np.sqrt(1/(2*mu))
phi4=np.random.normal(0,std,size=N)

f = open('confs.dat','w')
f.close()
magnetization=np.sum(phi4)

for j in range(thermalization+sweeps):
  for i in range(N):
    random_spin=np.random.randint(N)
    
    #helical boundary conditions
    nearest_neighbor=random_spin+1
    if(nearest_neighbor>=N):
        nearest_neighbor=nearest_neighbor-N
    sum1=phi4[nearest_neighbor]

    nearest_neighbor=random_spin-1
    if(nearest_neighbor<0):
        nearest_neighbor=nearest_neighbor+N
    sum1+=phi4[nearest_neighbor]

    nearest_neighbor=random_spin+L
    if(nearest_neighbor>=N):
        nearest_neighbor=nearest_neighbor-N
    sum1+=phi4[nearest_neighbor]

    nearest_neighbor=random_spin-L
    if(nearest_neighbor<0):
        nearest_neighbor=nearest_neighbor+N
    sum1+=phi4[nearest_neighbor]

    sum1=sum1-alpha*phi4[random_spin]*np.abs(magnetization/N)
    mean=sum1/(2*mu)
    new_value=np.random.normal(mean,std)
    quartic=np.exp(-lambd*new_value**4)
    uniform=np.random.uniform()
    
    if quartic>uniform:
      magnetization=magnetization-phi4[random_spin]+new_value
      phi4[random_spin]=new_value

  if(j>=thermalization):
    f = open('confs.dat','a')
    np.savetxt(f,np.reshape(phi4,(1,N)),fmt="%.7f")
    f.close()

