import numpy as np
import matplotlib.pyplot as plt

# Stochastic Lorenz 96 parameters
F = 8  # forcing parameter
H = 0.75  # coupling between slow and fast variables
C = 10  # time scale of variables y
B = 15  # inverse amplitude of the fast variables

h = 2e-4  # integration period in natural units
t_final = 10  # duration of the simulation in natural time units
NT = np.fix(t_final / h).astype(int)  # no. of discrete time steps
nosc = 20  # no. of oscillators (dimension of x)
fps = 10  # no. of fast variables (z) per slow variables (x)
nosc_fast = fps * nosc  # no. of fast variables (dz)
s2y = 4  # variance of the observations: slow variables
s2u = 1 / 10  # variance of the observations: fast variables
s2x = h / 2  # variance of the state noise: slow variables
s2z = h / 8  # variance of the state noise: fast variables
Tobs = 200  # states are observed every Tobs time steps

# Initial conditions
x = np.zeros([nosc, NT])
x[:, 0] = np.random.rand(nosc)
z = np.zeros([nosc_fast, NT])
z[:, 0] = (1 / (C * B)) * np.random.rand(nosc_fast) - 1 / (2 * C * B)

# Euler integration
ok = 0
while not ok:
    for n in np.arange(1, NT):
        # slow variables
        x[0, n] = x[0, n - 1] + h * (-x[nosc - 1, n - 1] * (x[nosc - 2, n - 1] - x[1, n - 1])) - x[0, n - 1] + F - (
                (H * C) / B) * np.sum(z[0:fps, n - 1]) + np.sqrt(s2x) * np.random.randn(1).item()
        x[1, n] = x[1, n - 1] + h * (-x[0, n - 1] * (x[nosc - 1, n - 1] - x[2, n - 1])) - x[1, n - 1] + F - (
                (H * C) / B) * np.sum(z[fps + np.arange(0, fps), n - 1]) + np.sqrt(s2x) * np.random.randn(1).item()

        for i in np.arange(2, nosc - 1):
            x[i, n] = x[i, n - 1] + h * (-x[i - 1, n - 1] * (x[i - 2, n - 1] - x[i + 1, n - 1])) - x[i, n - 1] + F - (
                    (H * C) / B) * np.sum(z[(i - 1) * fps + np.arange(0, fps), n - 1]) + np.sqrt(s2x) * np.random.randn(
                1).item()

        x[nosc - 1, n] = x[nosc - 1, n - 1] + h * (-x[nosc - 2, n - 1] * (x[nosc - 3, n - 1] - x[0, n - 1])) - x[
            nosc - 1, n - 1] + F - (
                                 (H * C) / B) * np.sum(z[(nosc - 2) * fps + np.arange(0, fps), n - 1]) + np.sqrt(
            s2x) * np.random.randn(1).item()

        # fast variables
        xaux = np.repeat(x[:, n - 1], fps)
        z[0, n] = (z[0, n - 1]
                   + h * (C * B * z[1, n - 1] * (z[nosc_fast - 1, n - 1] - z[2, n - 1])
                          - C * z[0, n - 1] + (F * C / B) + (C * H / B) * xaux[0])
                   + np.sqrt(s2z) * np.random.randn(1).item())

        z[1:nosc_fast - 3, n] = (z[1:nosc_fast - 3, n - 1]
                                 + h * (C * B * z[2:nosc_fast - 2, n - 1] * (
                        z[0:nosc_fast - 4, n - 1] - z[3:nosc_fast - 1, n - 1])
                                        - C * z[1:nosc_fast - 3, n - 1] + (F * C / B)
                                        + (C * H / B) * xaux[1:nosc_fast - 3])
                                 + np.sqrt(s2z) * np.random.randn(nosc_fast - 4))

        z[nosc_fast - 2, n] = (z[nosc_fast - 2, n - 1]
                               + h * (C * B * z[nosc_fast - 1, n - 1] * (z[nosc_fast - 3, n - 1] - z[0, n - 1])
                                      - C * z[nosc_fast - 2, n - 1] + (F * C / B) + (C * H / B) * xaux[nosc_fast - 2])
                               + np.sqrt(s2z) * np.random.randn(1).item())

        z[nosc_fast - 1, n] = (z[nosc_fast - 1, n - 1]
                               + h * (C * B * z[0, n - 1] * (z[nosc_fast - 2, n - 1] - z[1, n - 1])
                                      - C * z[nosc_fast - 1, n - 1] + (F * C / B) + (C * H / B) * xaux[nosc_fast - 1])
                               + np.sqrt(s2z) * np.random.randn(
                    1).item())

    ok = not np.any(np.isnan(x[0, :]) | np.isinf(x[0, :]))

# Observations
y = x + np.sqrt(s2y) * np.random.randn(nosc,NT)
u = z + np.sqrt(s2u) * np.random.randn(nosc_fast,NT)


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
plt.suptitle('Slow state and observations')


plt.figure(2)
idx_plotted_z = [1,22,43]
auxT = 20000
for i, idx in enumerate(idx_plotted_z):
    plt.subplot(len(idx_plotted_z), 1, i + 1)
    plt.plot(np.arange(0, auxT), z[idx, 0:auxT], 'k', label='state' if i == 0 else "")
    plt.plot(np.arange(0, auxT, Tobs), u[idx, 0:auxT:Tobs], '*', label='observations' if i == 0 else "")
    if i == 0:  # Add legend only to the first subplot to avoid repetition
        plt.legend()
plt.suptitle('Fast state and observations')
plt.show()


