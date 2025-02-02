import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function
s = ctrl.TransferFunction.s
g1 = (0.1 * (0.1 * s + 1)) / (0.01 * s + 1)

# Bode plot
plt.figure(1)
ctrl.bode(g1)

# Nyquist plot
plt.figure(2)
ctrl.nyquist(g1)

plt.show()
