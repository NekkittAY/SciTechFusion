from pydantic import BaseModel, Field


class AnalyticalInteg(BaseModel):
    expr: str = Field(...)
    sym: str = Field(...)


class NumIntegFunc(BaseModel):
    function: str = Field(...)
    sym: str = Field(...)
    a: float = Field(...)
    b: float = Field(...)


class NumIntegDots(BaseModel):
    arr: list[float] = Field(...)
    method: str | None = 'simpson'


class Interp(BaseModel):
    x: list[float] = Field(...)
    y: list[float] = Field(...)
    x0: float = Field(...)
    method: str | None = 'linear'


class OdeNumSolve(BaseModel):
    function: str = Field(...)
    y0: float = Field(...)
    t0: float = Field(...)
    tf: float = Field(...)
    method: str | None = 'RK45'


class OptFunc(BaseModel):
    function: str = Field(...)
    sym: str = Field(...)
    x0: list[float] = Field(...)
    method: str | None = 'BFGS'


class BoundsOptFunc(BaseModel):
    function: str = Field(...)
    sym: str = Field(...)
    bounds: list[list] = Field(...)
    method: str | None = 'shgo'


class OROpt(BaseModel):
    function: str = Field(...)
    lin_cons: list[str] = Field(...)
    sym: list[str] = Field(...)
    bounds: list[list] = Field(...)


class LPSolve(BaseModel):
    sym: list[str] = Field(...)
    sym_bounds: list[list] = Field(...)
    sym_coeff: list[float] = Field(...)
    sym_cs_coeff: list[float] = Field(...)
    cs_bounds: list[float] = Field(...)


class ExprExpand(BaseModel):
    expr: str = Field(...)


class ExprSimplify(BaseModel):
    expr: str = Field(...)


class ExprSolve(BaseModel):
    expr: str = Field(...)


class SolveNonlin(BaseModel):
    exprs: list[str] = Field(...)
    sym: str = Field(...)


class DiffExpr(BaseModel):
    expr: str = Field(...)
    sym: str = Field(...)


class LimExpr(BaseModel):
    expr: str = Field(...)
    sym: str = Field(...)
    lim: float = Field(...)


class GroebnerExpr(BaseModel):
    exprs: list[str] = Field(...)
