#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r1 = 5.
r2 = 5.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# y0 = psi
# x = z/d

# Right-hand side of the system: 
# y0' = y1
# y1' = r1^2 sinh(y0)    
def fun(x, y):
    return np.vstack((y[1], r1**2*np.sinh(y[0])))

# Boundary conditions:
# y1(left) = 0
# y1(right)+2r1r2 = 0
def bc(ya, yb):
    return np.array([ya[1], yb[1]+2.0*r1*r2])

# Solving for x in [0;0.5]
x = np.linspace(0., 0.5, 10000)
y = np.zeros((2, x.size))

# Initial guess for the potential profile
r1init = 1.
r3init = 3.135322030076839  # r2init = 1000
y[0] = 2.*np.log(r1init/(2.*r3init)*np.cos(r3init*x))    

# Calling solve_bvp
res = solve_bvp(fun, bc, x, y, tol=1.e-6, max_nodes=5000000)


x_plot = np.linspace(0., 0.5, 500)
y_plot = res.sol(x_plot)[0]
plt.plot(x_plot, y_plot, label='numerical')

plt.legend()
plt.xlabel(r"$z/d$")
plt.ylabel(r"$\psi$")

plt.show()
