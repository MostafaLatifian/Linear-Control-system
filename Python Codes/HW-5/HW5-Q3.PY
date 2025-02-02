import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function
s = ctrl.TransferFunction.s
g1 = (5 * (s + 1) * np.exp(-2 * s)) / (s * (5 * s + 1))

# Bode plot with margin
plt.figure(1)
ctrl.margin(g1)

plt.show()
