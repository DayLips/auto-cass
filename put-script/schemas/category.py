from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=20, description="Category name")
    description: Optional[str] = Field(None, min_length=5, max_length=200, description="Description category")

class CategoryCreate(CategoryBase):
    ...

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='ID Category')

    class Config:
        from_attributes = True

class CategoryListResponse(BaseModel):
    categories: list[CategoryResponse]