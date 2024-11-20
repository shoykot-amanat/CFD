# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 01:10:27 2024

@author: Shoykot Amanat
In this program, I will solve 1-D steady state heat conduction equation for a rod of length 1 m.
initial condition: T(t=0, x<0) = 0, T(t=0, x=1) = 1
Boundary condition: T(t=t, x=0) = 0, T(t=t, x=1) = 1
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l = 1 # rod length
n = 41 # number of grid points
# dx = l/(n-1) # distance between two adjacent grid points
max_iteration = 200 # specifying iteration number
tolerance = 1e-6  # Convergence criteria

T = np.zeros(n) # initialize array for temperature.
T[-1] = 1 # adjusting the array according to initial condition.
print(T)

# plot setup
#plt.ion() # start interactive mode
x = np.linspace(0, 1, n)
fig, ax = plt.subplots()
line, = ax.plot(x, T, label='Temperature Distribution', color='blue')
ax.set_xlabel('Position along the rod')
ax.set_ylabel('Temperature')
ax.set_title('1-D heat conduction')
ax.legend()



def update(frame):
    global T
    T_new = T.copy()
    for i in range(1, n-1):
        T_new[i] = 0.5 * (T[i+1] + T[i-1])

    # Check for convergence
    if np.max(np.abs(T_new - T)) < tolerance:
        print(f"Converged after {frame} iterations.")
        ani.event_source.stop()  # Stop the animation if converged
    
    T[:] = T_new
    line.set_ydata(T)
    return line,

ani = FuncAnimation(fig, update, frames=max_iteration, blit=True, interval=10)    

plt.show()
