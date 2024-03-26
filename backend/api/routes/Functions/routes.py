from fastapi import APIRouter, Depends, status
from .models import FunctionsUpdate, FunctionsData
from .manage_table import FunctionTable


router = APIRouter()


@router.post("/", summary="Insert data in Functions table",
             description="Insert data in Functions table",
             response_description="The created data",
             status_code=status.HTTP_201_CREATED)
async def function_insert_data(data: FunctionsUpdate = Depends()) -> dict:
    data_id = await FunctionTable.insert_data(data)
    return {"id": data_id}


@router.get("/", summary="Select all from Functions table",
            description="Select all from Functions table",
            response_description="All data in table",
            status_code=status.HTTP_200_OK)
async def functions_show_data() -> list[FunctionsData]:
    data = await FunctionTable.show_data()
    return data


@router.patch("/{data_id}", summary="Update table by id",
              description="Update table by id",
              response_description="The single data",
              status_code=status.HTTP_200_OK)
async def functions_update_data(data_id: int,
                                update_data: FunctionsUpdate = Depends()) -> dict:
    data_id = await FunctionTable.update_data(data_id, update_data)
    return {"id": data_id}


@router.delete("/{data_id}", summary="Delete the example by id",
               description="Delete the example by id",
               response_description="HTTP 200 STATUS")
async def functions_delete_data(data_id: int) -> dict:
    data_id = await FunctionTable.delete_data(data_id)
    return {"id": data_id}
