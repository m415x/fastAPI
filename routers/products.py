from fastapi import APIRouter


router = APIRouter(
    prefix="/products", tags=["products"], responses={404: {"message": "No encontrado"}}
)


product_list = ["prod1", "prod2", "prod3", "prod4", "prod5"]


@router.get("/")
async def products():  # type: ignore
    return product_list


@router.get("/{id}")
async def products(id: int):
    return product_list[id]
