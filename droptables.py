import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.db.db import engine
from app.db import models

# Удаляем все таблицы
print("Удаляю таблицы...")
models.Base.metadata.drop_all(bind=engine)
print("Таблицы удалены")

# Создаем заново
print("Создаю таблицы заново...")
models.Base.metadata.create_all(bind=engine)
print("Таблицы созданы")