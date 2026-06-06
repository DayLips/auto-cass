from sqlalchemy.orm import Session
from typing import Optional

from models import Receipt
from schemas import ReceiptCreate

class ReceiptRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_receipt_on_cass_id_and_doc_id(self, cass_id: int, doc_id: int) -> Optional[Receipt]:
        return (
            self.db.query(Receipt)
            .filter(Receipt.cass_id == cass_id, Receipt.doc_id == doc_id)
            .first()
        )

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