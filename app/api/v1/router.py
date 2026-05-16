from fastapi import APIRouter

from app.modules.products.routes import (
    router as product_router
)

from app.modules.users.routes import (
    router as user_router
)

v1_router = APIRouter()


v1_router.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)

v1_router.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)