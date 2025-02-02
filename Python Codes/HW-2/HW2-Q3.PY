import control as ctrl
import matplotlib.pyplot as plt

# Define transfer function variable
s = ctrl.TransferFunction.s

# Define transfer function
g = (s + 3) / (s * (s + 5) * (s + 6) * (s**2 + 2 * s + 2))

# Plot root locus
plt.figure()
ctrl.rlocus(g)
plt.title('Root Locus')
plt.grid()
plt.show()