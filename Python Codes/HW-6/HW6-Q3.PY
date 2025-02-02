import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function Ls
s = ctrl.TransferFunction.s
Ls = np.exp(-0.4 * s) / (0.2 * s + 1)

# Define the controller Cs
Cs = 0.045 + 1 / s

# Open-loop transfer function (Ls * Cs)
plt.figure(1)
ctrl.margin(Ls * Cs)
plt.grid()

# Closed-loop transfer function Ts
Ts = (Cs * Ls) / (1 + Cs * Ls)

# Step response plot for Ts
plt.figure(2)
time, response = ctrl.step_response(Ts)
plt.plot(time, response)

# Step info for Ts
step_info = ctrl.step_info(Ts)
print(step_info)

plt.show()
