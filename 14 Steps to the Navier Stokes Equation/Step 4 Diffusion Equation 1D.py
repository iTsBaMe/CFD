import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2/(nx - 1)
nt = 20
nu = 0.3 
sigma = 0.2
dt = sigma*dx**2/nu

u= np.ones(nx)
u[int(0.5/dx):int(1/dx + 1)] = 2

un = np.ones(nx)

for i in range(nt):
    un = u.copy()
    for j in range(nx):
        u[i] = un[i] + nu * dt/dx**2*(un[i+1] -2*un[i] + un[i-1])

plt.plot(np.linspace(0,2,nx),u)
plt.show()


print(f"The time step is {dt}")

