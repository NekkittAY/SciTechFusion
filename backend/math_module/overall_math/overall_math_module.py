from sympy.parsing import parse_expr
from sympy import solve, simplify, expand, symbols
from sympy.solvers import nonlinsolve
from sympy import diff, limit, groebner


def expr_expand(expr: str) -> str:
    """
    Function to expand expression

    :param expr: expression, string
    :return: expand expression, string
    """

    expr = parse_expr(expr)
    result_expr = expand(expr)
    return result_expr


def expr_simplify(expr: str) -> str:
    """
    Function to simplify expression

    :param expr: expression, string
    :return: simplify expression, string
    """

    expr = parse_expr(expr)
    result_expr = simplify(expr)
    return result_expr


def expr_solve(expr: str) -> str:
    """
    Solving function

    :param expr: expression, string
    :return: solved expression, string
    """

    expr = parse_expr(expr)
    result_expr = solve(expr)
    return result_expr


def solve_nonlinear(exprs: list, sym: str) -> list:
    """
    Solve nonlinear system function

    :param exprs: expressions, list
    :param sym: symbols in expression, string
    :return: solved system, list
    """

    result = nonlinsolve([parse_expr(expr) for expr in exprs], symbols(sym))
    return result


def diff_expr(expr: str, sym: str) -> str:
    """
    Derivative of expression

    :param expr: expression, string
    :param sym: symbol for derivative, differential; string
    :return: derivative of expression, string
    """

    expr = parse_expr(expr)
    result_expr = diff(expr, sym)
    return result_expr


def limit_expr(expr: str, sym: str, lim: float) -> float:
    """
    Limit of expression

    :param expr: expression, string
    :param sym: symbol for limit, string
    :param lim: lim number, float
    :return: limit of expression, float
    """

    expr = parse_expr(expr)
    result_expr = limit(expr, sym, lim)
    return result_expr


def groebner_expr(exprs: list) -> list:
    """
    Groebner basis

    :param exprs: expressions, list
    :return: groebner basis, list
    """

    result = groebner([parse_expr(expr) for expr in exprs])
    return result
