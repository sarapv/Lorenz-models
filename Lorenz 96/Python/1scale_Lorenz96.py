import numpy as np
import matplotlib.pyplot as plt

# Stochastic Lorenz 96 parameters
F = 8  # forcing parameter

h = 2e-4  # integration period in natural units
t_final = 10  # duration of the simulation in natural time units
NT = np.fix(t_final / h).astype(int)  # no. of discrete time steps
nosc = 20  # no. of oscillators (dimension of x)
s2y = 4  # variance of the observations
s2x = 1 / 2  # variance of the state noise
Tobs = 200  # states are observed every Tobs time steps

# Initial conditions
x = np.zeros([nosc, NT])
x[:, 0] = np.random.rand(nosc)

# Euler integration
ok = 0
while not ok:
    for n in np.arange(1, NT):
        # slow variables
        x[0, n] = x[0, n - 1] + h * ((-x[nosc - 1, n - 1] * (x[nosc - 2, n - 1] - x[1, n - 1])) - x[0, n - 1] + F ) + np.sqrt(h*s2x) * np.random.randn(1).item()
        x[1, n] = x[1, n - 1] + h * ((-x[0, n - 1] * (x[nosc - 1, n - 1] - x[2, n - 1])) - x[1, n - 1] + F ) + np.sqrt(h*s2x) * np.random.randn(1).item()

        for i in np.arange(2, nosc - 1):
            x[i, n] = x[i, n - 1] + h * ((-x[i - 1, n - 1] * (x[i - 2, n - 1] - x[i + 1, n - 1])) - x[i, n - 1] + F) + np.sqrt(h*s2x) * np.random.randn(
                1).item()

        x[nosc - 1, n] = x[nosc - 1, n - 1] + h * ((-x[nosc - 2, n - 1] * (x[nosc - 3, n - 1] - x[0, n - 1])) - x[
            nosc - 1, n - 1] + F) + np.sqrt(h*s2x) * np.random.randn(1).item()


    ok = not np.any(np.isnan(x[0, :]) | np.isinf(x[0, :]))

# Observations
y = x + np.sqrt(s2y) * np.random.randn(nosc,NT)


# Figures
plt.figure(1)
idx_plotted = [1,2,4]
auxT = 20000
for i, idx in enumerate(idx_plotted):
    plt.subplot(len(idx_plotted), 1, i + 1)
    plt.plot(np.arange(0, auxT), x[idx, 0:auxT], 'k', label='state' if i == 0 else "")
    plt.plot(np.arange(0, auxT, Tobs), y[idx, 0:auxT:Tobs], '*', label='observations' if i == 0 else "")
    if i == 0:  # Add legend only to the first subplot to avoid repetition
        plt.legend()
plt.suptitle('State and observations')
plt.show()


