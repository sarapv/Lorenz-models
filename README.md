# Lorenz models

* **Stochastic Lorenz 96 model** (available in Matlab, and Python) . This model has two different versions: (1) the mono-scale model, and (2) the multi-scale model. 
    
  * The multi-scale model has two state variables, $x$ and $z$, of dimensions $d_x$ and $d_z$ respectively. 
  While $x$ is a slow-changing variable, $z$ evolves fast in time. It also has four static parameters $F$, $H$, $C$ and $B$. 
  * The mono-scale model is a simpler version of the previous one, ignoring the variable $z$ and the influence it has in $x$. The number of 
  static parameters are also reduced, and there is only $F$.

  The dimension of the model can be tuned, making it interesting to try algorithms and methodologies in higher dimensions.

  
* **Stochastic Lorenz 63 model** (available in Matlab and Python). This is a 3-dimensional chaotic model, described by the SDEs:
    
    $$dx_1 = -S (x_1 - x_2) + \sigma dw_1,$$

    $$dx_2 = R x_1 - x_2 - x_1 x_3 + \sigma dw_2,$$

    $$dx_3 = x_1 x_2 - B x_3 + \sigma dw_3,$$
    
    where the $w_i$'s are independent 1-dimensional Wiener processes, $\sigma$ is the standard deviation of the state noise,
    and $S$, $R$, and $B$ are static parameters. 

# Some links

* [Wikipedia page of the Lorenz 63 system, with code in different programming languages](https://en.wikipedia.org/wiki/Lorenz_system)
* [Integration of Lorenz 63 model with a 4th Runge Kutta method (instead of Euler-Maruyama) in Python](https://blog.stackademic.com/lorenz-63-system-integration-using-4th-order-runge-kutta-methods-in-python-778d7dbc44c1)
* [The original paper of Edward N. Lorenz in the Journal of the Atmospheric Sciences, 1963](https://cdanfort.w3.uvm.edu/research/lorenz-1963.pdf)
* [Wikipedia page for the Lorenz 96 system](https://en.wikipedia.org/wiki/Lorenz_96_model)
* [Thesis of van Kekem, Dirk Leendert: Dynamics of the Lorenz-96 model.](https://pure.rug.nl/ws/portalfiles/portal/65106850/1_Introduction.pdf) I recommend to have a look at Figure 1.3 to understand the physical meaning of the model. There is also a summary of Lorenz's life and achievements.





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
