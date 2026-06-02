from app.modules.products import service
from app.modules.products.mapper import to_product_list, to_product_schema
from app.modules.products.schema import CreateProductSchema, UpdateProductSchema


async def get_products():
    products = await service.get_all_products()
    return {
        "success": True,
        "data": to_product_list(products),
        "total": len(products),
    }


async def get_product(product_id: str):
    product = await service.get_product_by_id(product_id)
    return {"success": True, "data": to_product_schema(product)}


async def create_product(body: CreateProductSchema):
    product = await service.create_product(body)
    return {"success": True, "data": to_product_schema(product)}


async def update_product(product_id: str, body: UpdateProductSchema):
    product = await service.update_product(product_id, body)
    return {"success": True, "data": to_product_schema(product)}


async def delete_product(product_id: str):
    await service.delete_product(product_id)
    return {"success": True, "message": "Product deleted successfully"}
