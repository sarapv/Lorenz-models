import numpy as np
import matplotlib.pyplot as plt

# Parameters
s = 10
r = 28
b = 8 / 3

h = 1e-3  # time (integration) step
T = 20000  # total number of time steps
Tobs = 40  # steps/time between observations

s2x = h / 2  # variance of the state noise
s2y = 1  # variance of the observation noise

dx = 3  # dimension of the state
idx_observed = np.array([0, 2])  # which states are 'observed'
dy = len(idx_observed)  # dimension of the observation

x = np.zeros([3, T])
y = np.zeros([len(idx_observed), T])

# initialization
xinit = np.array([-5.91652, -5.52332, 24.5723])
x[:, 0] = xinit + np.sqrt(s2x) * np.random.randn(dx)
y[:, 0] = x[idx_observed, 0] + np.sqrt(s2y) * np.random.randn(dy)

# Generating ground truth / synthetic data
for t in np.arange(1, T):
    x[0, t] = x[0, t - 1] + h * (-s * (x[0, t - 1] - x[1, t - 1])) + np.sqrt(s2x * h) * np.random.randn(1).item()
    x[1, t] = x[1, t - 1] + h * (r * x[0, t - 1] - x[1, t - 1] - (x[0, t - 1] * x[2, t - 1])) + np.sqrt(
        s2x * h) * np.random.randn(1).item()
    x[2, t] = x[2, t - 1] + h * ((-b * x[2, t - 1]) + (x[0, t - 1] * x[1, t - 1])) + np.sqrt(s2x * h) * np.random.randn(
        1).item()

    if t % Tobs == 1:
        y[:, t] = x[idx_observed, t] + np.sqrt(s2y) * np.random.randn(dy)

# First figure: State and observations
plt.figure(1)
for i, idx in enumerate(idx_observed):
    plt.subplot(len(idx_observed), 1, i + 1)
    plt.plot(np.arange(0, T), x[idx, :], 'k', label='state' if i == 0 else "")
    plt.plot(np.arange(1, T, Tobs), y[i, 1:T:Tobs], '*', label='observations' if i == 0 else "")
    if i == 0:  # Add legend only to the first subplot to avoid repetition
        plt.legend()
plt.suptitle('State and observations')

# Second figure: XY, XZ, YZ planes
plt.figure(2)

# XY plane
plt.subplot(311)
plt.plot(x[0, :], x[1, :])
plt.title('XY plane')

# XZ plane
plt.subplot(312)
plt.plot(x[0, :], x[2, :])
plt.title('XZ plane')

# YZ plane
plt.subplot(313)
plt.plot(x[1, :], x[2, :])
plt.title('YZ plane')

plt.show()
