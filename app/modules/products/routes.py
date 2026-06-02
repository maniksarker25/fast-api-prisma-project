from fastapi import APIRouter

from app.modules.products import controller
from app.modules.products.schema import CreateProductSchema, UpdateProductSchema

router = APIRouter()


@router.get("/")
async def get_products():
    return await controller.get_products()


@router.post("/", status_code=201)
async def create_product(body: CreateProductSchema):
    return await controller.create_product(body)


@router.get("/{product_id}")
async def get_product(product_id: str):
    return await controller.get_product(product_id)


@router.put("/{product_id}")
async def update_product(product_id: str, body: UpdateProductSchema):
    return await controller.update_product(product_id, body)


@router.delete("/{product_id}", status_code=200)
async def delete_product(product_id: str):
    return await controller.delete_product(product_id)
