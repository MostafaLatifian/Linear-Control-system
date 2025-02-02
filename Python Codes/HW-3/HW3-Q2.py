import control as ctrl
import matplotlib.pyplot as plt

# Define transfer function variable
s = ctrl.TransferFunction.s

# Define transfer function
g = (s + 1) / (s**3 + 4 * s**2 + 5 * s)

# Plot root locus
plt.figure()
ctrl.rlocus(g)
plt.title('Root Locus')
plt.grid()
plt.show()
