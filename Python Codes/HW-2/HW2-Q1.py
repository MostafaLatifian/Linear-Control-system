import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

s = ctrl.TransferFunction([1, 0], [1])

T = 202.02577 / (s**2 + 5.67376 * s + 127.86441)
G = T / (1 - T)
G = ctrl.minreal(G, verbose=False)

print(T)
print(G)

plt.figure()
time, response = ctrl.step_response(T)
plt.plot(time, response, label="Step Response of T")
plt.title("Step Response of T")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.grid()
plt.legend()

plt.figure()
time, response = ctrl.step_response(G)
plt.plot(time, response, label="Step Response of G", color='r')
plt.title("Step Response of G")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.grid()
plt.legend()

plt.show()