from sympy.parsing import parse_expr
from sympy import solve, simplify, expand, symbols
from sympy.solvers import nonlinsolve
from sympy import diff, limit, groebner


def expr_expand(expr: str) -> str:
    expr = parse_expr(expr)
    result_expr = expand(expr)
    return result_expr


def expr_simplify(expr: str) -> str:
    expr = parse_expr(expr)
    result_expr = simplify(expr)
    return result_expr


def expr_solve(expr: str) -> str:
    expr = parse_expr(expr)
    result_expr = solve(expr)
    return result_expr


def solve_nonlinear(exprs: list, sym: str) -> list:
    result = nonlinsolve([parse_expr(expr) for expr in exprs], symbols(sym))
    return result


def diff_expr(expr: str, sym: str) -> str:
    expr = parse_expr(expr)
    result_expr = diff(expr, sym)
    return result_expr


def limit_expr(expr: str, sym: str, lim: float) -> float:
    expr = parse_expr(expr)
    result_expr = limit(expr, sym, lim)
    return result_expr


def groebner_expr(exprs: list) -> list:
    result = groebner([parse_expr(expr) for expr in exprs])
    return result
