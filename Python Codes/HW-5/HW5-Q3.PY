!pip install control
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function variable
s = ctrl.TransferFunction.s

# Define the transfer function without the delay term
g1_num = [5, 5]
g1_den = [5, 1, 0]
g1_tf = ctrl.TransferFunction(g1_num, g1_den)

# Use Padé approximation to approximate the time delay term np.exp(-2 * s)
delay_num, delay_den = ctrl.pade(2, 2)
delay_tf = ctrl.TransferFunction(delay_num, delay_den)

# Multiply the transfer function by the delay term
g1 = g1_tf * delay_tf

# Bode plot with margin
plt.figure(1)
ctrl.bode(g1)

plt.show()
plt.close('all')  # Close all figures to ensure they render correctly
