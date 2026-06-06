from pydantic import BaseModel, Field
from typing import Optional

class ShopBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=20, description="Shop name")
    num_shop: int = Field(..., gt=0, description="Num shop")
    description: Optional[str] = Field(None, min_length=5, max_length=200, description="Shop product")

class ShopCreate(ShopBase):
    ...

class ShopResponse(ShopBase):
    id: int = Field(..., description='ID Shop')

    class Config:
        from_attributes = True

class ShopListResponse(BaseModel):
    shops: list[ShopResponse]