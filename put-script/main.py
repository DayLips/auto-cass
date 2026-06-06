from database import init_db, SessionLocal
from tools import DoWithCSV, InfoTable

def main():
    init_db()

    db = SessionLocal()
    try:
        info_table = InfoTable(db)

        if not info_table.check_category():
            flag = info_table.create_data_in_category()
            if not flag:
                raise Exception("Не удалось создать данные в таблице Category")
        if not info_table.check_product():
            flag = info_table.create_data_in_product()
            if not flag:
                raise Exception("Не удалось создать данные в таблице Product")
        if not info_table.check_shop():
            flag = info_table.create_data_in_shop()
            if not flag:
                raise Exception("Не удалось создать данные в таблице Shop")
        if not info_table.check_cass():
            flag = info_table.create_data_in_cass()
            if not flag:
                raise Exception("Не удалось создать данные в таблице Cass")

        worker = DoWithCSV(db)
        name_csv = "1_2.csv"
        if worker.read_csv(name_csv=name_csv):
            print(f"Чеки из {name_csv} добавлены в таблицу Receipts") if worker.add_receipts() else print(f"Чеки из {name_csv} не удалось добавить!!!")
            print(f"Позиции чеков из {name_csv} добавлены в таблицу ReceiptProducts") if worker.add_receipt_products() else print(f"Позиции чеков из {name_csv} не удалось добавить!!!")
    finally:
        db.close()


if __name__ == '__main__':
    main()