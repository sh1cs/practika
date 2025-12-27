import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from app.db.db import engine, SessionLocal
from app.db import models
from app.db.crud import create_category, create_book, get_categories, get_books
from app import schemas

print("=== Тест подключения и создания данных ===")

# 1. Создаем таблицы
models.Base.metadata.create_all(bind=engine)
print("✓ Таблицы созданы")

# 2. Создаем тестовые данные
db: Session = SessionLocal()

try:
    print("\n2. Создаю категорию...")
    # Используем схему Pydantic
    category_data = schemas.CategoryCreate(title="Test Category")
    cat1 = create_category(db, category=category_data)
    print(f"   ✓ Категория создана: id={cat1.id}, title='{cat1.title}'")
    
    print("\n3. Создаю книгу...")
    # Создаем схему для книги
    book_data = schemas.BookCreate(
        title="Test Book",
        description="Test Description",
        price=9.99,
        url="http://example.com/test",
        category_id=cat1.id
    )
    book1 = create_book(db, book=book_data)
    print(f"   ✓ Книга создана: id={book1.id}, title='{book1.title}'")
    
    print("\n4. Проверяю чтение данных...")
    
    categories = get_categories(db)
    print(f"   ✓ Найдено категорий: {len(categories)}")
    
    books = get_books(db)
    print(f"   ✓ Найдено книг: {len(books)}")
    
    print("\n=== Тест завершен успешно ===")
    
except Exception as e:
    print(f"\n✗ Ошибка: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    db.close()
