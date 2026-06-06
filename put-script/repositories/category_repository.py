from sqlalchemy.orm import Session
from typing import List

from models import Category
from schemas import CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_count(self) -> int:
        return self.db.query(Category).count()
    
    def get_all(self) -> List[Category]:
        return self.db.query(Category).all()
    
    def create(self, data: CategoryCreate) -> bool:
        try:
            db_category = Category(**data.model_dump())
            self.db.add(db_category)
            self.db.commit()
            self.db.refresh(db_category)
            return True
        except Exception as e:
            print(e)
            return False