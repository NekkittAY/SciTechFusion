import numpy as np
from scipy.optimize import minimize, brute, shgo, dual_annealing, least_squares
from scipy.optimize import OptimizeResult
from sympy import symbols, lambdify
from ortools.math_opt.python import mathopt
from ortools.linear_solver import pywraplp


def lambdify_func(func: str, sym: str):
    """
    Lambdify function

    :param func: function for lambdify, string
    :param sym: symbols - arguments, string
    :return: lambdified function
    """

    f = lambdify(symbols(sym), func, 'jax')
    return f


def optimize_func(func: str, sym: str, x0: list, method: str ='BFGS') -> OptimizeResult:
    """
    Optimization function

    Optimizing methods:
    1. Least Squares method
    2. BFGS method / L-BFGS-B method
    3. Nelder-Mead method
    4. Powell method
    5. and other

    :param func: function for optimization, string
    :param sym: symbols in function, string
    :param x0: initial values, list
    :param method: methods for optimization
    :return: Optimize result
    """

    x0 = np.array(x0)
    f = lambdify_func(func, sym)

    if method == 'lstsq':
        result = least_squares(f, x0)
    else:
        result = minimize(f, x0, method=method)

    return result


def bounds_optimize_func(func: str, sym: str, bounds: list, method: str ='shgo') -> OptimizeResult:
    """Optimization function with bounds methods

    Optimizing methods:
    1. Dual annealing method
    2. Shgo method
    3. Brute method

    :param func: function for optimization, string
    :param sym: symbols in function, string
    :param bounds: bounds values, list
    :param method: methods for optimization
    :return: Optimize result
    """

    bounds = np.array(bounds)
    f = lambdify_func(func, sym)

    result = None

    if method == 'dual_annealing':
        result = dual_annealing(f, bounds)
    elif method == 'shgo':
        result = shgo(f, bounds)
    elif method == 'brute':
        result = brute(f, bounds)

    return result


def optimize_or(func: str, lin_cons: list, sym: str, bounds: list) -> np.ndarray:
    """OR-Tools optimization function

    :param func: function for optimization, string
    :param lin_cons: linear conditions, list
    :param sym: symbols in function, string
    :param bounds: bounds conditions, list
    :return: Optimization result, np.ndarray
    """

    model = mathopt.Model(name="MatOpt")

    for i in range(len(sym)):
        exec(f'{sym[i]} = model.add_variable(lb={bounds[i][0]}, ub={bounds[i][1]}, name="{sym[i]}")')

    for lc in lin_cons:
        model.add_linear_constraint(eval(lc))

    model.maximize(eval(func))

    params = mathopt.SolveParameters(enable_output=True)

    result = mathopt.solve(model, mathopt.SolverType.GLOP, params=params)
    if result.termination.reason != mathopt.TerminationReason.OPTIMAL:
        raise RuntimeError(f"model failed to solve: {result.termination}")

    return np.array([result.objective_value(), result.variable_values()])


def LP_solve(sym: list,
             sym_bounds: list,
             sym_coeff: list,
             sym_cs_coeff: list,
             cs_bounds: list) -> dict:
    """Linear programming OR-Tools function

    :param sym: arguments for conditions, list
    :param sym_bounds: bounds conditions for args, list
    :param sym_coeff: coefficients for args in object function, list
    :param sym_cs_coeff: coefficients for args in constraint, list
    :param cs_bounds: constraint bounds values, list
    :return: Result of solving, dict
    """

    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return {}

    for i in range(len(sym)):
        exec(f'{sym[i]} = solver.NumVar({sym_bounds[i][0]}, {sym_bounds[i][1]}, "{sym[i]}")')

    ct = solver.Constraint(cs_bounds[0], cs_bounds[1], "ct")
    for i in range(len(sym)):
        exec(f'ct.SetCoefficient({sym[i]}, {sym_cs_coeff[i]})')

    objective = solver.Objective()

    for i in range(len(sym)):
        exec(f'objective.SetCoefficient({sym[i]}, {sym_coeff[i]})')

    objective.SetMaximization()

    solver.Solve()

    result = {'obj': objective.Value()}

    for i in range(len(sym)):
        result[f'{sym[i]}'] = eval(f'{sym[i]}.solution_value()')

    return result
