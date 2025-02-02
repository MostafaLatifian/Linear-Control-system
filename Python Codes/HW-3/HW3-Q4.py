import control as ctrl
import matplotlib.pyplot as plt

# Define transfer function variable
s = ctrl.TransferFunction.s

# Define transfer function
g = 100 * (s + 1) / (s**2 * (s + 5) * (s + 2))

# Plot root locus
plt.figure()
ctrl.rlocus(g)
plt.title('Root Locus')
plt.grid()
plt.show()

# Compute DC gain for Ka calculation
Ka = ctrl.dcgain(g * s**2)

# Compute steady-state error
ess = 1 / Ka

# Print results
print("Ka:", Ka)
print("Steady-state error (ess):", ess)