import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function
s = ctrl.TransferFunction.s
g1 = (-(s + 1) * (s + 2) * (s + 3) * (s + 4)) / (s**3 * (s + 100))

# Bode plot
plt.figure(1)
ctrl.bode(g1)

# Nyquist plot
plt.figure(2)
ctrl.nyquist(g1)

plt.show()
