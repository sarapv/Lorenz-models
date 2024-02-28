
We use the Euler-Maruyama scheme to integrate the SDEs of Lorenz 63 model. So the state of the system is described by

$$x_{1,t+1} = x_{1,t} - h S (x_{1,t} - x_{2,t}) + \sqrt{h} \sigma w_{1,t},$$

$$x_{2,t+1} = x_{2,t}  + h (R x_{1,t} - x_{2,t} - x_{1,t} x_{3,t}) + \sqrt{h} \sigma w_{2,t},$$

$$x_{3,t+1} = x_{3,t}   +  h (x_{1,t} x_{2,t} - B x_{3,t}) + \sqrt{h} \sigma w_{3,t},$$

* The parameters are usually set to $S = 10$, $B = \frac{8}{3}$ and $R = 28$, since the system exhibits chaotic behavior for these (and nearby) values.

* The integration step $h$ has to be small enough (e.g., $h = 10^{-3}$) to not get inaccurate results in the discretization process. This might lead the model to explode. 

* The $h$ is small, then the total number of time steps $T$ has to be big enough (e.g., $T = 10000$) to let the state evolve. 