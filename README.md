# AI Diploma Project

## Как запустить (локально в VS Code)
1) Установите Python 3.10+
2) (Рекомендуется) создайте окружение и установите зависимости:
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   git checkout -b feature/m1-project-structure
3) Запуск CLI:
   ```bash
   python -m src.cli
   ```

## Структура
- `src/core.py` — логика (items, validate, stats)
- `src/parsers.py` — парсинг/нормализация
- `src/storage.py` — JSON, состояние, экспорт/импорт
- `src/cli.py` — запуск и команды
- `colab/` — ноутбуки lesson_XX / hw_XX
- `data/` — локальные данные (в проде лучше БД/volume)

## команды
venv/Scripts/activate
git switch main

git switch feature/lesson-15-data-utils
python -m src.main

## если что-то уже поменял в ветке
git add .
git commit -m "save progress"
git checkout main
git pull origin main
git checkout -b feature/new-lesson

git add .
git commit -m "save current progress"
git checkout main

## если надо удалить ветки и создать заново
## удаление ветки не изменяет main
git branch
git checkout main
git pull origin main
git branch -D feature/lesson-14-strings
git branch -D feature/lesson-15-data-utils
git branch -D feature/lesson-16-file-utils
git push origin --delete feature/lesson-14-strings
git push origin --delete feature/lesson-15-data-utils
git push origin --delete feature/lesson-16-file-utils
git checkout -b feature/new-lesson
git push -u origin feature/new-lesson