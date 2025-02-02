import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function Ls
s = ctrl.TransferFunction.s
Ls = 200 / (s * (s + 1) * (s + 10))

# Define the gain kp
kp = 0.05

# First Gs with kp + 0.1*s
Gs1 = (kp + 0.1 * s) * Ls
plt.figure(1)
ctrl.margin(Gs1)

# Second Gs with kp + 0.3*s
Gs2 = (kp + 0.3 * s) * Ls
plt.figure(2)
ctrl.margin(Gs2)

# Third Gs with kp + 0.5*s
Gs3 = (kp + 0.5 * s) * Ls
plt.figure(3)
ctrl.margin(Gs3)

plt.show()
