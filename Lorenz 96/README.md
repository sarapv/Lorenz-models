# Stochastic Lorenz 96 model

We use the **Euler-Maruyama scheme** to integrate the SDEs of Lorenz 96 model. This model has two different versions: (1) the mono-scale and (2) the multi-scale version.

* **The mono-scale version** describes the evolution of the system, for $t=1,\ldots,T$, by

    $$x_{j,t+1} = x_{j,t} + h ( x_{j-1,t} (x_{j-2,t} - x_{j+1,t}) - x_{j,t} + F ) + \sqrt{h} \sigma_x w_{t},$$

    for $j = 1, \ldots, d_x$.

* ** The multi-scale version** describes the evolution of the two states of the system, for $t=1,\ldots,T$, by

    $$x_{t+1} = x_t + h f_x (x_t,z_t)  + \sqrt{h} \sigma_x w_{x,t},$$
 
    $$z_{t+1} = z_t + h f_z (x_t,z_t) + \sqrt{h} \sigma_z w_{z,t},$$

    where the the elements or components of functions $\boldsymbol{f}_x$ and $\boldsymbol{f}_z$ are

    $$f_{x,j} (\boldsymbol{x},\boldsymbol{z}) = - x_{j-1} (x_{j-2} - x_{j+1}) - x_j + F - \frac{HC}{B} \sum_{l=(j-1)L}^{Lj-1} z_l,$$

    $$f_{z,l} (\boldsymbol{x},\boldsymbol{z}) = -C B z_{l+1} (z_{l+2} - z_{l-1}) - C z_l + \frac{CF}{B} + \frac{HC}{B} x_{\lfloor \frac{l-1}{L} \rfloor},$$

    for $j = 1, \ldots, d_x$ and $l = 1,\ldots, d_z$.

# More useful info

* An interesting characteristic of the Lorenz 96 model is that you get to **choose the dimension of the state**: $d_x$ and $d_z$. In this implementation we get $d_x = 20$ and $d_z = 10 d_x = 200$.

* The parameters are usually set to $F = 8$, $H = 0.75$, $C = 10$, and $B = 15$, since the system exhibits chaotic behavior for these (and nearby) values.

* The integration step $h$ has to be small enough (e.g., $h = 10^{-4}$) to not get inaccurate results, otherwise the model might "explode". 

* Once $h$ is small, then the total number of time steps $T$ has to be big enough (e.g., $T = 10000$) to let the state evolve. 

Some links:
* [Wikipedia page for the Lorenz 96 system](https://en.wikipedia.org/wiki/Lorenz_96_model)
* [Thesis of van Kekem, Dirk Leendert: Dynamics of the Lorenz-96 model.](https://pure.rug.nl/ws/portalfiles/portal/65106850/1_Introduction.pdf) I recommend to have a look at Figure 1.3, to understand the physical meaning of the model.
