We use the Euler-Maruyama scheme to integrate the SDEs of Lorenz 96 model. So the evolution of the state of the system is described, for $t=1,\ldots,T$, by

$$\boldsymbol{x}_{t+1}$$

$$\boldsymbol{x}(t+1) = \boldsymbol{x}(t)+ h \boldsymbol{f}_x (\boldsymbol{x}(t),\boldsymbol{z}(t))  + \sqrt{h} \sigma_x \boldsymbol{w}_{x}(t),$$
 
$$\boldsymbol{z}(t+1) =  \boldsymbol{z}(t) + h \boldsymbol{f}_z (\boldsymbol{x}(t),\boldsymbol{z}(t)) + \sqrt{h} \sigma_z \boldsymbol{w}_{z}(t),$$

where the the elements or components of functions $\boldsymbol{f}_x$ and $\boldsymbol{f}_z$ are

$$f_{x,j} (\boldsymbol{x},\boldsymbol{z}) = - x_{j-1} (x_{j-2} - x_{j+1}) - x_j + F - \frac{HC}{B} \sum_{l=(j-1)L}^{Lj-1} z_l,$$

$$f_{z,l} (\boldsymbol{x},\boldsymbol{z}) = -C B z_{l+1} (z_{l+2} - z_{l-1}) - C z_l + \frac{CF}{B} + \frac{HC}{B} x_{\lfloor \frac{l-1}{L} \rfloor},$$

for $j = 1, \lotds, d_x$ and $l = 1,\ldots, d_z$.

* An interesting characteristic of the Lorenz 96 model is that you get to **choose the dimension of the state**: $d_x$ and $d_z$. In this implementation we get $d_x = 20$ and $d_z = 10 d_x = 200$.

* The parameters are usually set to $F = 8$, $H = 0.75$, $C = 10$, and $B = 15$, since the system exhibits chaotic behavior for these (and nearby) values.

* The integration step $h$ has to be small enough (e.g., $h = 10^{-4}$) to not get inaccurate results, otherwise the model might "explode". 

* Once $h$ is small, then the total number of time steps $T$ has to be big enough (e.g., $T = 10000$) to let the state evolve. 
