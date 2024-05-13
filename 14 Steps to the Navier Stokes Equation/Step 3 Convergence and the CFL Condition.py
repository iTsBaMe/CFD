import numpy
from matplotlib import pyplot

def upwind_c(nx, c):
    dx = 2 / (nx - 1)
    nt = 20    #nt is the number of timesteps we want to calculate
    c = c
    
    dt = 0.01 # compute dt based on Courant number
    
    

    u = numpy.ones(nx) 
    u[int(.5/dx):int(1 / dx + 1)] = 2

    un = numpy.ones(nx)
    #'''Choose which nodes to use for differencing based on the direction of
    #velocity on the interface to always use information from upstream nodes
    F = lambda c: (max(c/(abs(c)+1e-6), 0), max(-c/(abs(c)+1e-6), 0))
    #You can try to let c = 0.0 and see what is going on
    
    for n in range(nt):  #iterate through time
        un = u.copy() ##copy the existing values of u into un
        
        for i in range(1, nx-1):
            # Coefficients to the east side of the node (i+1)
            fe1, fe2 = F(c)
            # Coefficients to the west side of the node (i-1)
            fw1, fw2 = F(c)
            # Differential values on the east side interface
            ue = un[i] * fe1 + un[i+1] * fe2
            # Differential values on the wast side interface
            uw = un[i-1] * fw1 + un[i]* fw2
            u[i] = un[i] - c*dt/dx * (ue - uw)
        #for i in range(1, nx):
            #u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        
    pyplot.plot(numpy.linspace(0, 2, nx), u)
    print("CFL number =", c*dt/dx)
    print("dt =", dt)
    pyplot.show()


upwind_c(141,1) #try 141 the solution blows up. But doesnt when we use dt = 0.01
