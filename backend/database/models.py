from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    pass


class Functions(BaseModel):
    __tablename__ = "Functions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    formula: Mapped[str]
    description: Mapped[str | None]
    initial_cond: Mapped[str]
    boundary_cond: Mapped[str]
    number_of_args: Mapped[int | None]
    created_by: Mapped[str | None]
