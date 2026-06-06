from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base

class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    num_shop = Column(Integer, nullable=False, unique=True)
    descriprion = Column(Text)

    casses = relationship("Cass", back_populates='shop')

    def __repr__(self):
        return f"<Shop(id={self.id}, num_shop='{self.num_shop}', name={self.name})>"