from sqlalchemy.orm import Session
from typing import List

from models import Shop
from schemas import ShopCreate

class ShopRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_count(self) -> int:
        return self.db.query(Shop).count()
    
    def get_all(self) -> List[Shop]:
        return self.db.query(Shop).all()
    
    def get_by_num(self, num_shop: int) -> Shop:
        return (
            self.db.query(Shop)
            .filter(Shop.num_shop == num_shop)
            .first()
        )
    
    def create(self, data: ShopCreate) -> bool:
        try:
            db_category = Shop(**data.model_dump())
            self.db.add(db_category)
            self.db.commit()
            self.db.refresh(db_category)
            return True
        except Exception as e:
            print(e)
            return False