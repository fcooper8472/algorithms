The Forward Euler method is a first-order numerical method for solving ordinary differential equations with a given initial value.

Given an initial value problem of the form

$$y'(t) = f(t, y(t))$$

with initial condition

$$y(t_0)=y_0$$

then for a given step size $\Delta t$, we say that $t_n = t_0 + n\Delta t$, and the approximate solution is given by

$$y(t_{n+1}) = y(t_n) + \Delta t f(t_n, y(t_n))$$

etc.

- some steps
- in the
- algorithm
