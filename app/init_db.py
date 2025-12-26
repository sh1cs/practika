import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal, create_all_tables
from app.db.crud import create_category, create_book

def init_db():
    create_all_tables()
    
    db = SessionLocal()
    
    try:
        print("Создание категорий...")
        cat1 = create_category(db, name="Художественная литература")
        cat2 = create_category(db, name="Техническая литература")
        
        print(f"Создана категория: {cat1.name}")
        print(f"Создана категория: {cat2.name}")
        
        print("\nДобавление книг в категорию 'Художественная литература'...")
        
        books_cat1 = [
            ("Мастер и Маргарита", "Классический роман Михаила Булгакова", 550.50, "https://example.com/master"),
            ("1984", "Антиутопия Джорджа Оруэлла", 480.00, "https://example.com/1984"),
            ("Преступление и наказание", "Роман Фёдора Достоевского", 620.75, "https://example.com/crime"),
            ("Война и мир", "Роман Льва Толстого", 750.25, "https://example.com/war")
        ]
        
        for title, desc, price, url in books_cat1:
            book = create_book(db, title=title, desc=desc, price=price, cat_id=cat1.id, url=url)
            print(f"  Добавлена книга: {book.title}")
        
        print("\nДобавление книг в категорию 'Техническая литература'...")
        
        books_cat2 = [
            ("Чистый код", "Создание, анализ и рефакторинг", 1200.00, "https://example.com/clean"),
            ("Python. К вершинам мастерства", "Продвинутое программирование на Python", 950.25, "https://example.com/python"),
            ("Базы данных. Проектирование", "Основы проектирования баз данных", 780.50, "https://example.com/db"),
            ("Алгоритмы. Построение и анализ", "Фундаментальные алгоритмы", 1350.00, "")
        ]
        
        for title, desc, price, url in books_cat2:
            book = create_book(db, title=title, desc=desc, price=price, cat_id=cat2.id, url=url)
            print(f"  Добавлена книга: {book.title}")
        
        total_books = len(books_cat1) + len(books_cat2)
        print(f"\nВсего добавлено: 2 категории и {total_books} книг")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
