from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class ReceiptBase(BaseModel):
    doc_id: str = Field(..., min_length=9, max_length=8, description="Indetifier chec")
    cass_id: int = Field(..., gt=0, description="ID Cass")
    total_price: Decimal = Field(..., gt=Decimal('0.00'), description="Total prcie chec")

class ReceiptCreate(ReceiptBase):
    ...
