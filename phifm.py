import numpy as np

L=64
N=L*L

mu=2.0-3.0/2.0
lambd=0.7/4.0
alpha=5.0

sweeps=110001
thermalization=10000
std=np.sqrt(1/(2*mu))
ising=np.random.normal(0,std,size=N)

f = open('confs.dat','w')
f.close()
for j in range(sweeps):
  for i in range(N):
    random_spin=np.random.randint(N)
    #helical boundary conditions
    nearest_neighbor=random_spin+1
    if(nearest_neighbor>=N):
        nearest_neighbor=nearest_neighbor-N
    sum1=ising[nearest_neighbor]

    nearest_neighbor=random_spin-1
    if(nearest_neighbor<0):
        nearest_neighbor=nearest_neighbor+N
    sum1+=ising[nearest_neighbor]

    nearest_neighbor=random_spin+L
    if(nearest_neighbor>=N):
        nearest_neighbor=nearest_neighbor-N
    sum1+=ising[nearest_neighbor]

    nearest_neighbor=random_spin-L
    if(nearest_neighbor<0):
        nearest_neighbor=nearest_neighbor+N
    sum1+=ising[nearest_neighbor]

    magnetization=np.abs(np.mean(ising))

    sum1=sum1-alpha*ising[random_spin]*magnetization

    mean=sum1/(2*mu)
    new_value=np.random.normal(mean,std)
    quartic=np.exp(-lambd*new_value**4)

    uniform=np.random.uniform()
    
    if quartic>uniform:
      ising[random_spin]=new_value

  if(j>=thermalization):
    f = open('confs.dat','a')
    np.savetxt(f,np.reshape(ising,(1,N)),fmt="%.5f")
    f.close()
