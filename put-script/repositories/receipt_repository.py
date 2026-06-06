from sqlalchemy.orm import Session

from models import Receipt
from schemas import ReceiptCreate

class ReceiptRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: ReceiptCreate) -> bool:
        try:
            db_receipt = Receipt(**data.model_dump())
            self.db.add(db_receipt)
            self.db.commit()
            self.db.refresh(db_receipt)
            return True
        except Exception as e:
            print(e)
            return False 