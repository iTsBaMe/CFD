import numpy as np
import matplotlib.pyplot as plt
import time, sys


#geometry
L = 2
nx = 101
dx = 2/(nx-1)

#initial conditions
u  = np.ones(nx)
for i in range(int(.5/dx),int(1/dx+1)):
    u[i] =2 


nt = 20
dt = 0.00025
c = 1

un = np.ones(nx)
for i in range (nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i] - ((c*dt)/dx)*(un[i] - un[i-1])
        
    plt.plot(np.linspace(0,2,nx),u)

print(u)
plt.show()