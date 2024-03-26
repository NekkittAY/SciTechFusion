import numpy as np
from sympy import lambdify, symbols
from scipy.integrate import solve_ivp


def lambdify_func(func: str):
    """
    Lambdify function

    :param func: function for lambdify, string
    :return: lambdified function
    """

    f = lambdify(symbols('t, y'), func, 'jax')
    return f


def numerical_solve(func: str, y0: float, t0: float, tf: float, method: str ="RK45") -> tuple:
    """
    Numerical solve ODE function

    ODE solving methodS:
    1. Explicit Runge-Kutta method of order 3(2), RK23
    2. Explicit Runge-Kutta method of order 5(4), RK45
    3. Explicit Runge-Kutta method of order 8, DOP853
    4. others

    :param func: object function, string
    :param y0: initial values, float
    :param t0: initial time, float
    :param tf: final time, float
    :param method: method of solving, string
    :return: result of solving, tuple
    """

    y0 = np.array([y0])
    t0_tf = np.array([t0, tf])
    f = lambdify_func(func)

    sol = solve_ivp(f, t_span=t0_tf, y0=y0, method=method)

    return sol
