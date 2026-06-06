from pydantic import BaseModel, Field
from typing import Optional

from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=20, description="Product name")
    description: Optional[str] = Field(None, min_length=5, max_length=200, description="Description product")
    category_id: int = Field(..., description="Category id")

class ProductCreate(ProductBase):
    ...