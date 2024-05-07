import numpy as np
import matplotlib.pyplot as plt

nx = 141
dx = 2/(nx -1)
nt = 20

u = np.ones(nx)
u[:]= -1
u[int(.5 / dx) : int(1 / dx + 1)] = -2  #then set u = 2 between 0.5 and 1 as per our I.C.s

CFL = 0.9
dt  = CFL * dx/max(abs(u))

plt.plot(np.linspace(0, 2, nx), u);
plt.show()

for n in range(nt):  #iterate through time
    un = u.copy() ##copy the existing values of u into un
    
    F = lambda c: (max(c/(abs(c)+1e-6), 0), max(-c/(abs(c)+1e-6), 0))
    
    for i in range(1, nx-1):  ##now we'll iterate through the u array
        # Coefficients to the east side of the node (i+1)
        fe1, fe2 = F(u[i])
        # Coefficients to the west side of the node (i-1)
        fw1, fw2 = F(u[i])
        # Differential values on the east side interface
        ue = un[i] * fe1 + un[i+1] * fe2
        # Differential values on the wast side interface
        uw = un[i-1] * fw1 + un[i]* fw2
        u[i] = un[i] - un[i] * dt / dx * (ue - uw)

        #u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])        
    plt.plot(np.linspace(0, 2, nx), u) ##Plot the results
    plt.show()




