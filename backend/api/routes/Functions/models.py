from pydantic import BaseModel, Field, ConfigDict


class FunctionsUpdate(BaseModel):
    name: str = Field(...)
    formula: str = Field(...)
    description: str | None = Field(...)
    initial_cond: str = Field(...)
    boundary_cond: str = Field(...)
    number_of_args: int | None = Field(...)
    created_by: str | None = Field(...)


class FunctionsData(FunctionsUpdate):
    id: int
    model_config = ConfigDict(from_attributes=True)
