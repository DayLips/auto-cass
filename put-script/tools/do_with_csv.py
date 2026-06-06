from sqlalchemy.orm import Session
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict
import csv

from schemas import ReceiptCreate, ReceiptProductCreate
from repositories import ReceiptProductRepository, ReceiptRepository, ShopRepository, ProductRepository

class DoWithCSV:
    data_dir = Path(__file__).parent.parent.parent / "data"
    def __init__(self, db: Session):
        self.shop_repository = ShopRepository(db)
        self.receipt_repository = ReceiptRepository(db)
        self.product_repository = ProductRepository(db)
        self.receipt_product_repository = ReceiptProductRepository(db)

        self.csv_file = None
        self.shop_num: int = None
        self.cash_num: int = None
        self.cass_id: int = None
        self.checs_info: Dict[str, Decimal] = {}

    def read_csv(self, name_csv: str):
        csv_file = self.data_dir / name_csv

        if csv_file.exists():
            splited_name_csv = name_csv.split('_')
            self.shop_num = int(splited_name_csv[0])
            self.cash_num = int(splited_name_csv[1][0])

            with open(csv_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                self.csv_file = rows

                for row in rows:
                    doc_id = row['doc_id']
                    price = Decimal(str(row['price']))
                    amount = Decimal(str(row['amount']))
                    discount = Decimal(str(row['discount'])) / Decimal('100.0')
                    price_with_discount = price * (Decimal('1.0') - discount) * amount

                    if doc_id not in self.checs_info:
                        self.checs_info[doc_id] = price_with_discount
                    else:
                        self.checs_info[doc_id] += price_with_discount
                return True
        else:
            print(f"Файл {csv_file} не найден!!!")
            return False
        
    def add_receipts(self):
        shop = self.shop_repository.get_by_num(self.shop_num)
        if shop is not None:
            casses = shop.casses

            for cass in casses:
                if self.cash_num == cass.num_cass:
                    self.cass_id = cass.id
                    break

            if self.cass_id is None:
                return False
        
            for receipt in self.checs_info:
                receipt_data = ReceiptCreate(
                    cass_id=self.cass_id,
                    doc_id=receipt,
                    total_price=self.checs_info[receipt].quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                )

                receipt_db = self.receipt_repository.create(receipt_data)
                if not receipt_db:
                    return False
            
            return True
        else:
            return False
        
    def add_receipt_products(self):
        for row in self.csv_file:
            doc_id = row['doc_id']
            product_name = row['item']
            category_name = row['category']
            amount = int(row['amount'])
            price = Decimal(row['price']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            discount = Decimal(row['discount']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            
            product = self.product_repository.get_by_name(product_name)
            if product is None:
                print('Продукт не найден')
                return False
            if product.category.name != category_name:
                print('Куплен продукт не из той категории)')
                return False
            
            product_id = product.id
            
            receipt = self.receipt_repository.get_receipt_on_cass_id_and_doc_id(cass_id=self.cass_id, doc_id=doc_id)
            if receipt is None:
                print('Чек не найден')
                return False
            
            receipt_id = receipt.id
            receipt_product_data = ReceiptProductCreate(
                amount=amount,
                discount=discount,
                price=price,
                product_id=product_id,
                receipt_id=receipt_id
            )

            receipt_product_db = self.receipt_product_repository.create(receipt_product_data)
            if not receipt_product_db:
                return False
            
        return True
