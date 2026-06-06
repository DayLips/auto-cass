from pydantic import BaseModel, Field
from decimal import Decimal

from .shop import ShopResponse

class CassBase(BaseModel):
    num_cass: int = Field(..., gt=0, description="Num cass")
    total_money: Decimal = Field(..., gt=Decimal('0.00'), description='Total money in cass')
    available: bool = Field(..., default=True, description="Available cass?")
    shop_id: int = Field(..., gt=0, description="Shop ID")

class CassCreate(CassBase):
    ...

class CassResponse(CassBase):
    id: int = Field(..., description='ID Cass')
    shop: ShopResponse = Field(..., description='Shop')

    class Config:
        from_attributes = True