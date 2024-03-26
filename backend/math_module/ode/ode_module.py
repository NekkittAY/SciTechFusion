import numpy as np
from sympy import lambdify, symbols
from scipy.integrate import solve_ivp


def lambdify_func(func: str):
    f = lambdify(symbols('t, y'), func, 'jax')
    return f


def numerical_solve(func: str, y0: float, t0: float, tf: float, method="RK45") -> tuple:
    y0 = np.array([y0])
    t0_tf = np.array([t0, tf])
    f = lambdify_func(func)

    sol = solve_ivp(f, t_span=t0_tf, y0=y0, method=method)

    return sol
