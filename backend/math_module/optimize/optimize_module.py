import numpy as np
from scipy.optimize import minimize, brute, shgo, dual_annealing, least_squares
from scipy.optimize import OptimizeResult
from sympy import symbols, lambdify
from ortools.math_opt.python import mathopt
from ortools.linear_solver import pywraplp


def lambdify_func(func: str, sym: str):
    f = lambdify(symbols(sym), func, 'jax')
    return f


def optimize_func(func: str, sym: str, x0: list, method='BFGS') -> OptimizeResult:
    x0 = np.array(x0)
    f = lambdify_func(func, sym)

    if method == 'lstsq':
        result = least_squares(f, x0)
    else:
        result = minimize(f, x0, method=method)

    return result


def bounds_optimize_func(func: str, sym: str, bounds: list, method='shgo') -> OptimizeResult:
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
             cs_bounds: list):

    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

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
