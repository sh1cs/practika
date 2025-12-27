import psycopg2
from psycopg2 import sql
import sys

def setup_database():
    print("=== Настройка базы данных PostgreSQL ===")
    
    # Параметры подключения
    db_params = {
        'database': 'postgres',  # Подключаемся к системной базе
        'user': 'postgres',
        'password': 'password',  # Измените на ваш пароль
        'host': 'localhost',
        'port': '5432'
    }
    
    try:
        # Подключаемся к PostgreSQL
        print("1. Подключаюсь к PostgreSQL...")
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Создаем базу данных если её нет
        print("2. Создаю базу данных 'bookstore'...")
        try:
            cursor.execute("CREATE DATABASE bookstore")
            print("   ✓ База данных создана")
        except psycopg2.errors.DuplicateDatabase:
            print("   ✓ База данных уже существует")
        
        # Подключаемся к новой базе
        db_params['database'] = 'bookstore'
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Удаляем старые таблицы
        print("3. Удаляю старые таблицы...")
        cursor.execute("DROP TABLE IF EXISTS books CASCADE")
        cursor.execute("DROP TABLE IF EXISTS categories CASCADE")
        print("   ✓ Старые таблицы удалены")
        
        # Создаем таблицу categories
        print("4. Создаю таблицу 'categories'...")
        cursor.execute("""
            CREATE TABLE categories (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) UNIQUE NOT NULL
            )
        """)
        print("   ✓ Таблица 'categories' создана")
        
        # Создаем таблицу books
        print("5. Создаю таблицу 'books'...")
        cursor.execute("""
            CREATE TABLE books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                price DECIMAL(10, 2) NOT NULL,
                url TEXT NOT NULL,
                category_id INTEGER REFERENCES categories(id) NOT NULL
            )
        """)
        print("   ✓ Таблица 'books' создана")
        
        # Проверяем таблицы
        print("6. Проверяю созданные таблицы...")
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()
        print(f"   ✓ Созданные таблицы: {[t[0] for t in tables]}")
        
        cursor.close()
        conn.close()
        
        print("\n=== Настройка базы данных завершена успешно! ===")
        
    except Exception as e:
        print(f"\n✗ Ошибка: {e}")
        print("\nУбедитесь что:")
        print("1. PostgreSQL установлен и запущен")
        print("2. Пароль пользователя postgres правильный")
        sys.exit(1)

if __name__ == "__main__":
    setup_database()