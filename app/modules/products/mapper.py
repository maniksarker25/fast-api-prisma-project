from prisma.models import Product

from app.modules.products.schema import ProductQuerySchema


def to_product_schema(product: Product) -> ProductQuerySchema:
    return ProductQuerySchema.model_validate(product)


def to_product_list(products: list[Product]) -> list[ProductQuerySchema]:
    return [to_product_schema(p) for p in products]
