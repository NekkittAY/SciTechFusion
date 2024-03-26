from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .models import BaseModel


engine = create_async_engine(
    "sqlite+aiosqlite:///Functions.db"
)

async_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    """
    Create all tables of database async function
    """
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def delete_tables():
    """
    Delete all tables of database async function
    """
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
