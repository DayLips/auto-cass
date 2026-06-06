from sqlalchemy.orm import Session, joinedload
from typing import List, Optional

from models import Product
from schemas import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_count(self) -> int:
        return self.db.query(Product).count()
    
    def get_all(self) -> List[Product]:
        return self.db.query(Product).all()
    
    def get_by_name(self, name: str) -> Optional[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.name == name)
            .first()
        )
    
    def create(self, data: ProductCreate) -> bool:
        try:
            db_product = Product(**data.model_dump())
            self.db.add(db_product)
            self.db.commit()
            self.db.refresh(db_product)
            return True
        except Exception as e:
            print(e)
            return False