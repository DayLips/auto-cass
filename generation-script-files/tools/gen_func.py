import string, random

class GenFunc:
    
    # Функция генерации doc_id
    @staticmethod
    def generate_doc_id(length=8):
        alphabet = string.ascii_uppercase + string.digits
        return ''.join(random.choices(alphabet, k=length))
    
    # Функция выбора случайно категории
    @staticmethod
    def get_category(categories: list[str]):
        return random.choice(categories)
    
    # Функция генерации случайного кол-ва товара от 1 до 4
    @staticmethod
    def get_amount():
        return random.randint(1, 4)

    # Функция строки в для csv файла
    @staticmethod
    def generate_row(doc_id: str, items: list[str], category: str, amount: int):
        pred_discount = random.randint(0, 80)
        return {
            'doc_id': doc_id,
            'item': random.choice(items),
            'category': category,
            'amount': amount,
            'price': round(random.uniform(50, 5000), 2),
            'discount': pred_discount if pred_discount > 30 else 0
        }
