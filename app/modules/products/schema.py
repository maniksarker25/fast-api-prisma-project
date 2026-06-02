from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateProductSchema(BaseModel):
    title: str = Field(min_length=3, max_length=123)
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class UpdateProductSchema(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=123)
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)


class ProductQuerySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: str
    price: float
    stock: int
    slug: str
    createdAt: datetime
    updatedAt: datetime
