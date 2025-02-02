import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function Ls
s = ctrl.TransferFunction.s
Ls = 10 / (s * (s**2 + 2*s + 5) * (s + 3))

# Bode plot with margin for Ls
plt.figure(1)
ctrl.margin(Ls)
plt.grid()

# Define the controller Cs
Cs = (30 * (28.14 * s + 1)) / (844.24 * s + 1)

# Closed-loop transfer function Ts
Ts = Cs * Ls

# Bode plot with margin for Ts
plt.figure(2)
ctrl.margin(Ts)
plt.grid()

plt.show()
