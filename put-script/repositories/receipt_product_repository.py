from sqlalchemy.orm import Session

from models import ReceiptProduct
from schemas import ReceiptProductCreate

class ReceiptProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: ReceiptProductCreate) -> bool:
        try:
            db_receipt_product = ReceiptProduct(**data.model_dump())
            self.db.add(db_receipt_product)
            self.db.commit()
            self.db.refresh(db_receipt_product)
            return True
        except Exception as e:
            print(e)
            return False 