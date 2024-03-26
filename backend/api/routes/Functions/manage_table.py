from sqlalchemy import select, update
from backend.database.manage_database import async_session
from backend.database.models import Functions
from .models import FunctionsUpdate, FunctionsData


class FunctionTable:
    @classmethod
    async def insert_data(cls, data: FunctionsUpdate) -> int:
        async with async_session() as session:
            data = data.model_dump()
            new_data = Functions(**data)
            session.add(new_data)
            await session.commit()
            return new_data.id

    @classmethod
    async def show_data(cls) -> list[FunctionsData]:
        async with async_session() as session:
            table_data = select(Functions)
            result = await session.execute(table_data)
            data_content = result.scalars().all()
            data = [FunctionsData.model_validate(d) for d in data_content]
            return data

    @classmethod
    async def update_data(cls,
                          data_id: int,
                          update_data: FunctionsUpdate) -> int:
        async with async_session() as session:
            data = update(Functions).where(Functions.id == data_id).values(update_data.model_dump())
            await session.execute(data)
            await session.commit()
            return data_id

    @classmethod
    async def delete_data(cls, data_id: int) -> int:
        async with async_session() as session:
            table_data = select(Functions).where(Functions.id == data_id)
            data = await session.execute(table_data)
            data = data.scalar_one()
            await session.delete(data)
            await session.commit()
            return data_id
