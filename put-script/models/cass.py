from sqlalchemy import Column, Integer, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship

from database import Base

class Cass(Base):
    __tablename__ = "casses"

    id = Column(Integer, primary_key=True, index=True)
    num_cass = Column(Integer, nullable=False)
    total_money = Column(Numeric, nullable=False)
    available = Column(Boolean, nullable=False, default=True)
    shop_id = Column(Integer, ForeignKey('shops.id'), nullable=False)

    receipts = relationship('Receipt', back_populates='cass')
    shop = relationship('Shop', back_populates='casses')

    def __repr__(self):
        return f"<Cass(id={self.id}, num_cass='{self.num_cass}', available={self.available})>"
