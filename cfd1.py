# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:54:46 2024

@author: Shoykot Amanat
"""
import numpy as np
import matplotlib.pyplot as plt
import sys, time

nx = 41 # number of grid points
dx = 2 / (nx - 1) # distance between adjacent grid points
nt = 25 # number of timestep we want to calculate
dt = 0.025 # time step
c = 1 # velocity of wave

u = np.ones(nx)
u[int(0.5/dx) : int(1/dx + 1)] = 2 # setting u = 2 as per our I.C.
print(u)

plt.plot(np.linspace(0,2,nx), u)

un = np.ones(nx) # initializing a temporary array

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i] - c * dt/dx * (un[i] - un[i-1])
    
plt.plot(np.linspace(0,2,nx), u)


