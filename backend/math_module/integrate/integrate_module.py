from numpy import array
from scipy.integrate import quad, simpson, romb
from sympy.parsing import parse_expr
from sympy import integrate, lambdify, symbols


def analytical_integ(expr: str, sym: str) -> str:
    """
    Analytical integral solve function

    :param expr: expression of integral, string
    :param sym: differential, string
    :return: solved integral, string
    """
    expr = parse_expr(expr)
    result_expr = integrate(expr, symbols(sym))
    return result_expr


def numerical_integ_func(func: str,
                         sym: str,
                         a: float,
                         b: float) -> float:
    """
    Numerical integral solve function

    :param func: function of integral, list
    :param sym: arguments of function under integral, string
    :param a: lower limit of interval, float
    :param b: upper limit of interval, float
    :return: result of integration, float
    """
    f = lambdify(symbols(sym), func, 'jax')
    result = quad(f, a, b)
    return result


def numerical_integ_dots(arr: list, method: str = 'simpson') -> float:
    """
    Numerical integral solve function by values of function

    Methods of integration:
    1. Simpson's method
    2. Romb method

    :param arr: array of values of function, list
    :param method: method of integration, string
    :return:
    """
    arr = array(arr)

    if method == "simpson":
        result = simpson(arr)
    else:
        result = romb(arr)

    return result
