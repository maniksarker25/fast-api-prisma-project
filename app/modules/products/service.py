from slugify import slugify

from app.config.prisma import db
from app.modules.products.exceptions import (
    ProductAlreadyExistsException,
    ProductNotFoundException,
)
from app.modules.products.schema import CreateProductSchema, UpdateProductSchema


async def get_all_products():
    return await db.product.find_many(order={"createdAt": "desc"})


async def get_product_by_id(product_id: str):
    product = await db.product.find_unique(where={"id": product_id})
    if not product:
        raise ProductNotFoundException()
    return product


async def create_product(data: CreateProductSchema):
    slug = slugify(data.title)

    existing = await db.product.find_unique(where={"slug": slug})
    if existing:
        raise ProductAlreadyExistsException()

    return await db.product.create(
        data={
            "title": data.title,
            "description": data.description,
            "price": data.price,
            "stock": data.stock,
            "slug": slug,
        }
    )


async def update_product(product_id: str, data: UpdateProductSchema):
    product = await db.product.find_unique(where={"id": product_id})
    if not product:
        raise ProductNotFoundException()

    update_data = data.model_dump(exclude_none=True)

    if "title" in update_data:
        new_slug = slugify(update_data["title"])
        existing = await db.product.find_unique(where={"slug": new_slug})
        if existing and existing.id != product_id:
            raise ProductAlreadyExistsException()
        update_data["slug"] = new_slug

    return await db.product.update(where={"id": product_id}, data=update_data)


async def delete_product(product_id: str):
    product = await db.product.find_unique(where={"id": product_id})
    if not product:
        raise ProductNotFoundException()
    return await db.product.delete(where={"id": product_id})
