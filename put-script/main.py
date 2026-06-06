from pathlib import Path

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
        data_dir = Path(__file__).parent.parent / "data"
        csv_files = [f.name for f in data_dir.glob("*.csv")]
        for name_csv in csv_files:
            if worker.read_csv(name_csv=name_csv):
                print(f"Чеки из {name_csv} добавлены в таблицу Receipts") if worker.add_receipts() else print(f"Чеки из {name_csv} не удалось добавить!!!")
                print(f"Позиции чеков из {name_csv} добавлены в таблицу ReceiptProducts") if worker.add_receipt_products() else print(f"Позиции чеков из {name_csv} не удалось добавить!!!")

        if data_dir.exists() and data_dir.is_dir():
            for file in data_dir.iterdir():
                if file.is_file():
                    file.unlink()
            print(f"Папка {data_dir} очищена")
        else:
            print(f"Папка {data_dir} не существует")
    finally:
        db.close()


if __name__ == '__main__':
    main()