from sqlalchemy.orm import Session
from typing import List

from models import Cass
from schemas import CassCreate

class CassRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_count(self) -> int:
        return self.db.query(Cass).count()
    
    def get_all(self) -> List[Cass]:
        return self.db.query(Cass).all()
    
    def get_by_shop_id_and_num_cass(self, shop_id: int, num_cass: int) -> Cass:
        return (
            self.db.query(Cass)
            .filter(Cass.shop_id == shop_id, Cass.num_cass == num_cass)
            .first()
        )
    
    def create(self, data: CassCreate) -> bool:
        try:
            db_cass = Cass(**data.model_dump())
            self.db.add(db_cass)
            self.db.commit()
            self.db.refresh(db_cass)
            return True
        except Exception as e:
            print(e)
            return False