import numpy as np
import matplotlib.pyplot as plt

nx = 81
dx = 2/(nx -1)
dt = 0.025
nt = 20

u = np.ones(nx)
u[:1] = 1
u[int(.5/dx): int(1/dx + 1)] =2 

CFL = 0.9
dt  = CFL * dx/max(abs(u))

un = np.ones(nx)

for i in range(nt):
    un = u.copy()
    for j in range(1,nx-1):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])        
    plt.plot(np.linspace(0, 2, nx), u)
plt.show()




