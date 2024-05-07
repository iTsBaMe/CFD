import numpy as np
nx = 3
ny = 3

u = np.zeros((nx,nx))
print(u)
#u[1,:] = 0
u[1:,] = 10 #rows and columns are viewed as opposites in matlab
print(u)