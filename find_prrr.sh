#!/bin/bash
echo "=== Поиск файла prrr ==="

# Возможные места
SEARCH_PATHS=(
    "$HOME/vladi/prrr"
    "$HOME/vladi/prrr.png"
    "$HOME/vladi/prrr.jpg"
    "vladi/prrr"
    "vladi/prrr.png"
    "vladi/prrr.jpg"
    "./vladi/prrr"
    "./prrr"
    "prrr"
)

for path in "${SEARCH_PATHS[@]}"; do
    if [ -f "$path" ]; then
        echo "✅ Найден файл: $path"
        echo "   Размер: $(ls -lh "$path" | awk '{print $5}')"
        echo "   Тип: $(file -b "$path")"
        
        # Копируем в examples
        mkdir -p examples
        cp "$path" examples/postgresql_result.png
        echo "📁 Скопирован в: examples/postgresql_result.png"
        exit 0
    fi
done

echo "❌ Файл prrr не найден"
echo ""
echo "Поиск всех файлов с 'pr' в домашней директории:"
find ~/ -name "*pr*" -type f 2>/dev/null | head -10
