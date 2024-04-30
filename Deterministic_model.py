import numpy as np
import matplotlib.pyplot as plt

# Parameters
a10 = 1
a11 = 0.02
a12 = 0.1
a20 = 0.15
a21 = 0.01
u = 0.001
v = 0.001

# Initial conditions
X1_0 = 10
Y1_0 = 5
X2_0 = 0
Y2_0 = 0

# Time parameters
t0 = 0
tf = 50  # Final time
dt = 0.01  # Time step

def dx1_dt(X1, Y1, X2, u):
    return X1 * (a10 - a11*X1 - a12*Y1) + u*(X2 - X1)

def dy1_dt(X1, Y1, Y2, v):
    return Y1 * (-a20 + a21*X1) + v*(Y2 - Y1)

def dx2_dt(X2, Y2, X1, u):
    return X2 * (a10 - a11*X2 - a12*Y2) + u*(X1 - X2)

def dy2_dt(X2, Y2, Y1, v):
    return Y2 * (-a20 + a21*X2) + v*(Y1 - Y2)

t_values = np.arange(t0, tf, dt)
X1_values = np.zeros_like(t_values)
Y1_values = np.zeros_like(t_values)
X2_values = np.zeros_like(t_values)
Y2_values = np.zeros_like(t_values)

X1_values[0] = X1_0
Y1_values[0] = Y1_0
X2_values[0] = X2_0
Y2_values[0] = Y2_0

for i in range(1, len(t_values)):
    X1_values[i] = X1_values[i-1] + dt * dx1_dt(X1_values[i-1], Y1_values[i-1], X2_values[i-1], u)
    Y1_values[i] = Y1_values[i-1] + dt * dy1_dt(X1_values[i-1], Y1_values[i-1], Y2_values[i-1], v)
    X2_values[i] = X2_values[i-1] + dt * dx2_dt(X2_values[i-1], Y2_values[i-1], X1_values[i-1], u)
    Y2_values[i] = Y2_values[i-1] + dt * dy2_dt(X2_values[i-1], Y2_values[i-1], Y1_values[i-1], v)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_values, X1_values, label='Prey 1')
plt.plot(t_values, Y1_values, label='Predator 1')
plt.plot(t_values, X2_values, label='Prey 2')
plt.plot(t_values, Y2_values, label='Predator 2')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model with Migration')
plt.legend()
plt.grid(True)
plt.show()
