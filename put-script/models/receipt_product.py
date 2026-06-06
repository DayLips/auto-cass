from sqlalchemy import Column, Integer, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship
from decimal import Decimal

from database import Base

class ReceiptProduct(Base):
    __tablename__ = "receipt_products"

    id = Column(Integer, primary_key=True, index=True)
    receipt_id = Column(Integer, ForeignKey('receipts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    amount = Column(Integer, nullable=False, default=1)
    price = Column(Numeric, nullable=False)
    discount = Column(Numeric, nullable=False, default=Decimal(0.00))

    receipt = relationship('Receipt', back_populates='receipt_products')
    product = relationship('Product', back_populates='receipt_products')

    def __repr__(self):
        return f"<ReceiptProduct(id={self.id}, receipt_id='{self.receipt_id}', product_id={self.product_id}, price={self.price})>"