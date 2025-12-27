#!/bin/bash

echo "=== Настройка базы данных PostgreSQL ==="

# 1. Проверяем запущен ли PostgreSQL
echo "1. Проверяю статус PostgreSQL..."
sudo systemctl status postgresql --no-pager

# 2. Подключаемся к PostgreSQL
echo -e "\n2. Подключаюсь к PostgreSQL..."
sudo -u postgres psql << EOF

-- Посмотреть список баз данных
\l

-- Создать базу данных если её нет
CREATE DATABASE bookstore;

-- Подключиться к новой базе
\c bookstore

-- Посмотреть текущие таблицы
\dt

-- Удалить старые таблицы если они есть
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS categories CASCADE;

-- Создать таблицу categories
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL
);

-- Создать таблицу books
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    url TEXT NOT NULL,
    category_id INTEGER REFERENCES categories(id) NOT NULL
);

-- Проверить структуру таблиц
\d categories
\d books

-- Выйти
\q
EOF

echo -e "\n3. Настройка завершена!"