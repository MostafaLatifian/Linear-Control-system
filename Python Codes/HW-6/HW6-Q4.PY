import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function Ls
s = ctrl.TransferFunction.s
Ls = 2500 / (s * (s + 25))

# Bode plot with margin for Ls
plt.figure(1)
ctrl.margin(Ls)

# Define the controllers Cs1 and Cs2
Cs1 = (1.35 * (0.1 * s + 1)) / (0.142 * s + 1)
Cs2 = (0.027 * s + 1) / (1.35 * (0.015 * s + 1))

# Overall system Gs
Gs = Ls * Cs1 * Cs2

# Bode plot with margin for Gs
plt.figure(2)
ctrl.margin(Gs)

plt.show()
