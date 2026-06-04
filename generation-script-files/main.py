from tools import DataToGen, GenFunc
from pathlib import Path
import csv

# Перемещаемся на уровень выше, чтобы попасть в папку data/
script_dir = Path(__file__).parent
project_root = script_dir.parent
data_dir = project_root / "data"
data_dir.mkdir(parents=True, exist_ok=True)

count_shop = DataToGen.COUNT_SHOP()
category_items = DataToGen.CATEGORY_ITEMS
categories = list(category_items.keys())

# Начинаем перебирать магазины
for shop_num in range(1, count_shop + 1):

    count_cass = DataToGen.COUNT_CASS()
    # Начинаем перебирать кассы
    for cash_num in range(1, count_cass + 1):

        count_row_in_checks = DataToGen.COUNT_CHECKS()
        # Сгенерировали название csv файла с путем складирования
        file_path = data_dir / f"{shop_num}_{cash_num}.csv"

        # Начинаем создание и запись csv файла
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=DataToGen.FIELD_NAMES)
            writer.writeheader()

            # Заполняем каждую строчку чека
            for _ in range(0, count_row_in_checks):
                n = DataToGen.COUNT_ITEM_TYPE_IN_ONE_CHECS()
                doc_id = GenFunc.generate_doc_id()

                # Заполняем строчки кокретного чека со своим doc_id
                for _ in range(0, n):
                    category = GenFunc.get_category(categories)
                    amount = GenFunc.get_amount()
                    writer.writerow(GenFunc.generate_row(
                        doc_id=doc_id,
                        items=category_items[category],
                        category=category,
                        amount=amount
                    ))