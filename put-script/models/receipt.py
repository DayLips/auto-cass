from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    doc_id = Column(String(16), index=True, nullable=True)
    cass_id = Column(Integer, ForeignKey("casses.id"), nullable=False)
    total_price = Column(Numeric, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    cass = relationship('Cass', back_populates='receipts')
    receipt_products = relationship("ReceiptProduct", back_populates='receipt')

    def __repr__(self):
        return f"<Receipt(id={self.id}, doc_id='{self.doc_id}', created_at={self.created_at})>"