# Time Calculator / Калькулятор Времени

[English](#english) | [Русский](#russian)

---

## English

Web application based on **FastAPI**, designed for performing arithmetic operations with time in a convenient format (hours, minutes, seconds).

### Features

- Addition and subtraction of time intervals (e.g., `1h 30m + 45m`).
- Multiplication and division of time by a number (e.g., `1h 20m * 2`).
- Input/output format: `1h 30m 22s`.
- Web interface in the style of a mobile calculator.

### Tech Stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn.
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS).
- **Testing:** Pytest / Unit tests.

### Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd python-time-calculator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   # venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Open in browser:**
   Go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Usage

- Use `h`, `m`, `s` buttons (labeled as `ч`, `м`, `с` in UI) to enter time units.
- Enter numbers using the numeric keypad.
- Press `=` to get the result.
- `←` (or `C`) button clears the input.

### Testing

To run the calculation logic tests, execute:
```bash
python test_calc.py
```

---

## Russian

Веб-приложение на базе **FastAPI**, предназначенное для выполнения арифметических операций со временем в удобном формате (часы, минуты, секунды).

### Функциональные возможности

- Сложение и вычитание временных промежутков (например, `1ч 30м + 45м`).
- Умножение и деление времени на число (например, `1ч 20м * 2`).
- Формат ввода/вывода: `1ч 30м 20с`.
- Веб-интерфейс в стиле мобильного калькулятора.

### Технологический стек

- **Backend:** Python 3.10+, FastAPI, Uvicorn.
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS).
- **Тестирование:** Pytest / Unit-тесты.

### Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone <url-вашего-репозитория>
   cd python-time-calculator
   ```

2. **Создайте виртуальное окружение и активируйте его:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для macOS/Linux
   # venv\Scripts\activate  # Для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите приложение:**
   ```bash
   python run.py
   ```

5. **Откройте браузер:**
   Перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Использование

- Используйте кнопки `ч`, `м`, `с` для ввода единиц времени.
- Вводите числа с помощью цифровой клавиатуры.
- Нажимайте `=`, чтобы получить результат.
- Кнопка `←` (или `C`) очищает ввод.

### Тестирование

Для запуска тестов логики расчетов выполните:
```bash
python test_calc.py
```

## Project Structure / Структура проекта

- `app/main.py` — основной файл FastAPI приложения.
- `app/calculator.py` — логика парсинга и расчетов.
- `app/static/` — статические файлы (CSS, JS).
- `app/templates/` — HTML шаблоны.
- `run.py` — скрипт для запуска сервера.
- `test_calc.py` — юнит-тесты.
