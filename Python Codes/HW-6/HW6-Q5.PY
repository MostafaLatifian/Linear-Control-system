
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
ctrl.bode(Gs1, dB=True, margins=True)
plt.grid(True)
plt.title("Bode Plot with Margins for Gs1 (kp + 0.1s)")

# Second Gs with kp + 0.3*s
Gs2 = (kp + 0.3 * s) * Ls
plt.figure(2)
ctrl.bode(Gs2, dB=True, margins=True)
plt.grid(True)
plt.title("Bode Plot with Margins for Gs2 (kp + 0.3s)")

# Third Gs with kp + 0.5*s
Gs3 = (kp + 0.5 * s) * Ls
plt.figure(3)
