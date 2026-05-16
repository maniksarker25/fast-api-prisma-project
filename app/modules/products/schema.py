from pydantic import BaseModel, Field
from typing import Optional

class CreateProductSchema(BaseModel):

    title: str = Field(min_length=3,max_length=123)
    description: str
    price : float
    stock: int


class UpdateProductSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price :Optional[float] = None
    stock: Optional[int] = None


class ProductQuerySchema(BaseModel):
    id : str
    title: str
    description:str
    price : float
    stock: int
    slug: str
