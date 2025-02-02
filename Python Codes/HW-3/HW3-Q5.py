import control as ctrl
import matplotlib.pyplot as plt

# Define transfer function variable
s = ctrl.TransferFunction.s

# Define transfer functions
Gs = (5 * s + 10) / (s**2 + 4 * s + 5)
Ts = (5 * s + 10) / (s**2 + 9 * s + 15)

# Compute poles and zeros
poles_Ts = ctrl.poles(Ts)
poles_Gs = ctrl.poles(Gs)
zeros_Ts = ctrl.zeros(Ts)
zeros_Gs = ctrl.zeros(Gs)

# Print results
print("Poles of Ts:", poles_Ts)
print("Poles of Gs:", poles_Gs)
print("Zeros of Ts:", zeros_Ts)
print("Zeros of Gs:", zeros_Gs)
