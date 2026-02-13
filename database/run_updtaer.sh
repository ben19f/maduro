#!/bin/bash

# Путь к проекту
PROJECT_DIR="/home/madurian/mymaduroapp"

# Путь к виртуальному окружению
VENV_DIR="$PROJECT_DIR/.venv"

# Лог
LOG_FILE="/home/madurian/mymaduroapp/updater.log"

# Добавляем проект в PYTHONPATH
export PYTHONPATH="$PROJECT_DIR"

# Активируем виртуальное окружение
source "$VENV_DIR/bin/activate"

echo "=== updater started $(date) ===" >> "$LOG_FILE"

# Бесконечный цикл обновления БД
while true; do
    echo "--- Run at $(date) ---" >> "$LOG_FILE"

    python3 "$PROJECT_DIR/database/databse_updater.py" >> "$LOG_FILE" 2>&1

    # Ждём 10 минут
    sleep 300
done