import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
# Define transfer function variable
s = ctrl.TransferFunction.s

# Define transfer functions
Gs = (5 * s + 10) / (s**2 + 4 * s + 5)
Ts = (5 * s + 10) / (s**2 + 9 * s + 15)

g1 = -1 / (s * (-5 * s + 1))

# Compute poles and zeros
poles_Ts = ctrl.pole(Ts)
poles_Gs = ctrl.pole(Gs)
zeros_Ts = ctrl.zero(Ts)
zeros_Gs = ctrl.zero(Gs)

# Print results
print("Poles of Ts:", poles_Ts)
print("Poles of Gs:", poles_Gs)
print("Zeros of Ts:", zeros_Ts)
print("Zeros of Gs:", zeros_Gs)

# Bode plot
plt.figure()
ctrl.bode(g1, dB=True)
plt.show()

# Nyquist plot
plt.figure()
ctrl.nyquist(g1)
plt.show()