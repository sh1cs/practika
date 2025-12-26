import sys
import os

# Добавляем путь к проекту
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from app.db.db import SessionLocal, create_all_tables
from app.db.crud import create_category, create_book

print("=== Тест подключения и создания данных ===")

# Создаем таблицы
create_all_tables()
print("1. Таблицы созданы")

# Создаем сессию БД
db = SessionLocal()

try:
    # Создаем категорию
    print("2. Создаю категорию...")
    cat1 = create_category(db, name='Test Category')
    print(f"   Категория создана: {cat1.name}")
    
    # Создаем книгу
    print("3. Создаю книгу...")
    book1 = create_book(db, title='Test Book', desc='Test Description', price=100.0, cat_id=cat1.id)
    print(f"   Книга создана: {book1.title}")
    
    print("=== Тест завершен успешно ===")
    
except Exception as e:
    print(f"Ошибка: {e}")
    import traceback
    traceback.print_exc()
    db.rollback()
finally:
    db.close()
