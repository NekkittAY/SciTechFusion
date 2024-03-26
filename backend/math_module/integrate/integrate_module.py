from numpy import array
from scipy.integrate import quad, simpson, romb
from sympy.parsing import parse_expr
from sympy import integrate, lambdify, symbols


def analytical_integ(expr: str, sym: str) -> str:
    expr = parse_expr(expr)
    result_expr = integrate(expr, symbols(sym))
    return result_expr


def numerical_integ_func(func: list,
                         sym: str,
                         a: float,
                         b: float) -> float:
    f = lambdify(symbols(sym), func, 'jax')
    result = quad(f, a, b)
    return result


def numerical_integ_dots(arr: list, method: str) -> float:
    arr = array(arr)

    if method == "simpson":
        result = simpson(arr)
    else:
        result = romb(arr)

    return result
