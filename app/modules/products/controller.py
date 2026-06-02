from app.core.responses.api_response import send_response
from app.modules.products import service
from app.modules.products.mapper import to_product_list, to_product_schema
from app.modules.products.schema import CreateProductSchema, UpdateProductSchema


async def get_products():
    products = await service.get_all_products()
    return send_response(
        status_code=200,
        success=True,
        message="Products retrieved successfully",
        data=products,
    )


async def get_product(product_id: str):
    product = await service.get_product_by_id(product_id)
    return send_response(
        status_code=200,
        success=True,
        message="Product retrieved successfully",
        data=to_product_schema(product)
    )


async def create_product(body: CreateProductSchema):
    product = await service.create_product(body)
    return send_response(
        status_code=201,
        success=True,
        message="Product created successfully",
        data=to_product_schema(product)
    )


async def update_product(product_id: str, body: UpdateProductSchema):
    product = await service.update_product(product_id, body)
    return send_response(
        status_code=200,
        success=True,
        message="Product updated successfully",
        data=to_product_schema(product)
    )


async def delete_product(product_id: str):
    await service.delete_product(product_id)
    return send_response(
        status_code=200,
        success=True,
        message="Product deleted successfully"
    )
