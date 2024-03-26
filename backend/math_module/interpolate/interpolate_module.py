from numpy import array, interp
from scipy.interpolate import KroghInterpolator, CubicSpline, BarycentricInterpolator, Akima1DInterpolator


def interpolate(x: list, y: list, x0: float, method: str = "linear") -> float:
    x = array(x)
    y = array(y)

    result = None

    if method == "linear":
        result = interp(x0, x, y)
    elif method == "Krogh":
        result = KroghInterpolator(x, y)(x0)
    elif method == "Splines":
        result = CubicSpline(x, y)(x0)
    elif method == "Barycentric":
        result = BarycentricInterpolator(x, y)(x0)
    elif method == "Akima":
        result = Akima1DInterpolator(x, y)(x0)

    return result
