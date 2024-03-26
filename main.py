from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.database.manage_database import create_tables, delete_tables
from backend.api.routes.Functions.routes import router as functions_router
from backend.api.routes.Math_Module_API.routes import router as math_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    lifespan async function
    """

    await delete_tables()
    print("DB dropped")
    await create_tables()
    print("DB created")
    yield
    print("Turn off")

app = FastAPI(lifespan=lifespan)

app.include_router(functions_router, tags=["DB_Functions"], prefix="/db_functions")
app.include_router(math_router, tags=["Math_Functions"], prefix="/math_functions")
