# Lorenz models

* **Stochastic Lorenz 96 model** (available in Matlab, and Python) . This model is described by two types of state 
    variables: $D$-dimensional slow-changing variables, $\boldsymbol{x}$, and $N$-dimensional fast-changing 
    variables, $\boldsymbol{z}$. Both types of variables are coupled. Their SDEs are described by
  
    $$d\boldsymbol{x} = \boldsymbol{f}_x (\boldsymbol{x},\boldsymbol{z}) dt + \sigma_x d\boldsymbol{w}_x,$$
 
    $$d\boldsymbol{z} =  \boldsymbol{f}_z (\boldsymbol{x},\boldsymbol{z}) dt + \sigma_z d\boldsymbol{w}_z,$$

    where the elements of each function, $\boldsymbol{f}_x$ and 
    $\boldsymbol{f}_z$, at a specific time step are

    $$f_{x,j} (\boldsymbol{x},\boldsymbol{z}) = - x_{j-1} (x_{j-2} - x_{j+1}) - x_j + F - \frac{HC}{B} \sum_{l=(j-1)L}^{Lj-1} z_l,$$

    $$f_{z,l} (\boldsymbol{x},\boldsymbol{z}) = -C B z_{l+1} (z_{l+2} - z_{l-1}) - C z_l + \frac{CF}{B} + \frac{HC}{B} x_{\lfloor \frac{l-1}{L} \rfloor}.$$

    Here, $F$, $H$, $C$ and $B$ are static parameters. The dynamic variables are assumed to be arranged on a circular structure. 
    We used Euler integration to obtain a discrete-time version of the model (with integration step $h$).
  
  
* **Stochastic Lorenz 63 model** (available in Matlab and Python). This is a 3-dimensional model, described by the SDEs:
    
    $$dx_1 = -S (x_1 - x_2) + \sigma dw_1,$$

    $$dx_2 = R x_1 - x_2 - x_1 x_3 + \sigma dw_2,$$

    $$dx_3 = x_1 x_2 - B x_3 + \sigma dw_3,$$
    
    where the $w_i$'s are independent 1-dimensional Wiener processes, $\sigma$ is the standard deviation of the state noise,
    and $S$, $R$, and $B$ are static parameters. We used Euler integration to obtain a discrete-time version of the model 
    (with integration step $h$).

# Some links

* [Wikipedia page of the Lorenz 63 system, with code in different programming languages](https://en.wikipedia.org/wiki/Lorenz_system)
* [Integration of Lorenz 63 model with a 4th Runge Kutta method (instead of Euler-Maruyama) in Python](https://blog.stackademic.com/lorenz-63-system-integration-using-4th-order-runge-kutta-methods-in-python-778d7dbc44c1)
* [The original paper of Edward N. Lorenz in the Journal of the Atmospheric Sciences, 1963](https://cdanfort.w3.uvm.edu/research/lorenz-1963.pdf)
* [Wikipedia page for the Lorenz 96 system](https://en.wikipedia.org/wiki/Lorenz_96_model)
* [Thesis of van Kekem, Dirk Leendert: Dynamics of the Lorenz-96 model.](https://pure.rug.nl/ws/portalfiles/portal/65106850/1_Introduction.pdf) I recommend to have a look at Figure 1.3, to understand the physical meaning of the model. There is also a summary of Lorenz's life and achievements.





# MIT License

Copyright (c) 2023 Sara Pérez Vieites


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
