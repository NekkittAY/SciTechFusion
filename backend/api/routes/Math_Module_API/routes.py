from fastapi import APIRouter, Depends, status
from backend.math_module import *
from .models import *


router = APIRouter()


@router.post("/AnalyticalIntegration",
             summary="Analytical integration",
             description="Analytical integration",
             response_description="Result of integration",
             status_code=status.HTTP_200_OK)
async def analytical_integration(data: AnalyticalInteg = Depends()) -> dict:
    """
    Post data for analytical integration function

    :param data: data, AnalyticalInteg
    :return: result, dict
    """

    result = analytical_integ(data.expr, data.sym)
    return {"result": f"{result}"}


@router.post("/NumericalIntegrationFunc",
             summary="Numerical integration by function",
             description="Numerical integration",
             response_description="Result of numerical integration",
             status_code=status.HTTP_200_OK)
async def numerical_integration_func(data: NumIntegFunc = Depends()) -> dict:
    """
    Post data for numerical integration function

    :param data: data, NumIntegFunc
    :return: result, dict
    """
    result = numerical_integ_func(data.function, data.sym, data.a, data.b)
    return {"result": result[0]}


@router.post("/NumericalIntegrationDots",
             summary="Numerical integration by values",
             description="Numerical integration by values",
             response_description="Result of numerical integration by values",
             status_code=status.HTTP_200_OK)
async def numerical_integration_dots(data: NumIntegDots = Depends()) -> dict:
    """
    Post data for numerical integration by function values

    :param data: data, NumIntegDots
    :return: result, dict
    """

    result = numerical_integ_dots(data.arr, data.method)
    return {"result": result}


@router.post("/Interpolate",
             summary="Interpolation by values",
             description="Interpolation by values",
             response_description="Result of interpolation",
             status_code=status.HTTP_200_OK)
async def interpolation(data: Interp = Depends()) -> dict:
    """
    Post data for interpolation by values

    :param data: data, Interp
    :return: result, dict
    """

    result = interpolate(data.x, data.y, data.x0, data.method)
    return {"result": result}


@router.post("/ODE_Solve",
             summary="Solve ODE",
             description="Solve ODE",
             response_description="Result of solving ODE",
             status_code=status.HTTP_200_OK)
async def solve_ode(data: OdeNumSolve = Depends()) -> dict:
    """
    Post data for solving ODE

    :param data: data, OdeNumSolve
    :return: result, dict
    """

    result = numerical_solve_ode(data.function, data.y0, data.t0, data.tf, data.method)
    return {"result": f"{result}"}


@router.post("/Optimize_Function",
             summary="Optimize function",
             description="Optimize function",
             response_description="Result of optimization",
             status_code=status.HTTP_200_OK)
async def opt_func(data: OptFunc = Depends()) -> dict:
    """
    Post data for optimization

    :param data: data, OptFunc
    :return: result, dict
    """

    result = optimize_func(data.function, data.sym, data.x0, data.method)
    return {"result": f"{result}"}


@router.post("/Optimize_Function_Bounds",
             summary="Optimize function with bounds",
             description="Optimize function with bounds",
             response_description="Result of optimization with bounds",
             status_code=status.HTTP_200_OK)
async def bounds_opt_func(data: BoundsOptFunc = Depends()) -> dict:
    """
    Post data for optimization with bounds

    :param data: data, BoundsOptFunc
    :return: result, dict
    """

    result = bounds_optimize_func(data.function, data.sym, data.bounds, data.method)
    return {"result": f"{result}"}


@router.post("/Optimize_OR",
             summary="Optimize function by OR-Tools",
             description="Optimize function by OR-Tools",
             response_description="Result of optimization by OR-Tools",
             status_code=status.HTTP_200_OK)
async def or_opt_func(data: OROpt = Depends()) -> dict:
    """
    Post data for optimization by OR-Tools

    :param data: data, OROpt
    :return: result, dict
    """

    result = optimize_or(data.function, data.lin_cons, data.sym, data.bounds)
    return {"result": f"{result}"}


@router.post("/Optimize_LR",
             summary="Linear programming function by OR-Tools",
             description="Linear programming function by OR-Tools",
             response_description="Result of LP",
             status_code=status.HTTP_200_OK)
async def lr_opt_func(data: LPSolve = Depends()) -> dict:
    """
    Post data for Linear programming function by OR-Tools

    :param data: data, LPSolve
    :return: result, dict
    """

    result = LP_solve(data.sym, data.sym_bounds, data.sym_coeff, data.sym_cs_coeff, data.cs_bounds)
    return {"result": f"{result}"}


@router.post("/Expand_Expression",
             summary="Expand expression",
             description="expand expression",
             response_description="Result of expand",
             status_code=status.HTTP_200_OK)
async def expand_expr(data: ExprExpand = Depends()) -> dict:
    """
    Post data for expand expression

    :param data: data, ExprExpand
    :return: result, dict
    """

    result = expr_expand(data.expr)
    return {"result": f"{result}"}


@router.post("/Simplify_Expression",
             summary="Simplify expression",
             description="simplify expression",
             response_description="Result of simplify",
             status_code=status.HTTP_200_OK)
async def simplify_expr(data: ExprSimplify = Depends()) -> dict:
    """
    Post data for simplify expression

    :param data: data, ExprSimplify
    :return: result, dict
    """

    result = expr_simplify(data.expr)
    return {"result": f"{result}"}


@router.post("/Solve_Expression",
             summary="Solve expression",
             description="solve expression",
             response_description="Result of solving",
             status_code=status.HTTP_200_OK)
async def solve_expr(data: ExprSolve = Depends()) -> dict:
    """
    Post data for solve expression

    :param data: data, ExprSolve
    :return: result, dict
    """

    result = expr_solve(data.expr)
    return {"result": f"{result}"}


@router.post("/Solve_Nonlinear_System",
             summary="Solve nonlinear system",
             description="solve nonlinear system",
             response_description="Result of solving system",
             status_code=status.HTTP_200_OK)
async def solve_nonlinear_system(data: SolveNonlin = Depends()) -> dict:
    """
    Post data for solve nonlinear system

    :param data: data, SolveNonlin
    :return: result, dict
    """

    result = solve_nonlinear(data.exprs, data.sym)
    return {"result": f"{result}"}


@router.post("/Derivative_Function",
             summary="Find derivative of function",
             description="find derivative of function",
             response_description="Derivative of function",
             status_code=status.HTTP_200_OK)
async def diff_func(data: DiffExpr = Depends()) -> dict:
    """
    Post data for find derivative of function

    :param data: data, SolveNonlin
    :return: result, dict
    """

    result = diff_expr(data.expr, data.sym)
    return {"result": f"{result}"}


@router.post("/Limit_Function",
             summary="Find limit of function",
             description="find lim of function",
             response_description="Limit of function",
             status_code=status.HTTP_200_OK)
async def limit_func(data: LimExpr = Depends()) -> dict:
    """
    Post data for find limit of function

    :param data: data, LimExpr
    :return: result, dict
    """

    result = limit_expr(data.expr, data.sym, data.lim)
    return {"result": f"{result}"}


@router.post("/Groebner_System",
             summary="Find Groebner basis of system",
             description="find Groebner basis of system",
             response_description="Groebner basis of system",
             status_code=status.HTTP_200_OK)
async def groebner_sys(data: GroebnerExpr = Depends()) -> dict:
    """
    Post data for find groebner basis of system

    :param data: data, GroebnerExpr
    :return: result, dict
    """

    result = groebner_expr(data.exprs)
    return {"result": f"{result}"}
