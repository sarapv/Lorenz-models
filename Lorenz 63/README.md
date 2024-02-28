
# Stochastic Lorenz 63 model

We use the **Euler-Maruyama scheme** with step-size $h$ to integrate the SDEs of Lorenz 63 model. So the evolution of the state of the system is described, for $t=1,\ldots,T$, by

$$x_{1,t+1} = x_{1,t} - h S (x_{1,t} - x_{2,t}) + \sqrt{h} \sigma w_{1,t},$$

$$x_{2,t+1} = x_{2,t}  + h (R x_{1,t} - x_{2,t} - x_{1,t} x_{3,t}) + \sqrt{h} \sigma w_{2,t},$$

$$x_{3,t+1} = x_{3,t}   +  h (x_{1,t} x_{2,t} - B x_{3,t}) + \sqrt{h} \sigma w_{3,t},$$


# Some useful info 

* The parameters are usually set to $S = 10$, $B = \frac{8}{3}$ and $R = 28$, since the system exhibits chaotic behavior for these (and nearby) values.

* The integration step $h$ has to be small enough (e.g., $h = 10^{-3}$) to not get inaccurate results, otherwise the model might "explode". 

* Once $h$ is small, then the total number of time steps $T$ has to be big enough (e.g., $T = 10000$) to let the state evolve. 


Some links:
* [Wikipedia page of the Lorenz system, with code in different programming languages](https://en.wikipedia.org/wiki/Lorenz_system)
* [Integration of Lorenz 63 model with a 4th Runge Kutta method (instead of Euler-Maruyama) in Python](https://blog.stackademic.com/lorenz-63-system-integration-using-4th-order-runge-kutta-methods-in-python-778d7dbc44c1)
* [The original paper of Edward N. Lorenz in the Journal of the Atmospheric Sciences, 1963](https://cdanfort.w3.uvm.edu/research/lorenz-1963.pdf)
