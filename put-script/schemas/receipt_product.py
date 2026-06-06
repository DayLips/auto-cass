from pydantic import BaseModel, Field
from decimal import Decimal

class ReceiptProductBase(BaseModel):
    receipt_id: int = Field(..., gt=0, description="ID Receipt")
    product_id: int = Field(..., gt=0, description="ID Product")
    amount: int = Field(..., gt=0, description="Count product in receipt")
    price: Decimal = Field(..., gt=Decimal('0.00'), description="Price one product")
    discount: Decimal = Field(..., description="Discount on position")

class ReceiptProductCreate(ReceiptProductBase):
    ...

class ReceiptProductResponse(ReceiptProductBase):
    id: int = Field(..., description='ID ReceiptProduct')

    class Config:
        from_attributes = True