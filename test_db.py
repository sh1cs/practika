#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    print("✓ Подключение к PostgreSQL успешно")
    
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(f"✓ Версия PostgreSQL: {db_version[0]}")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"✗ Ошибка подключения: {e}")