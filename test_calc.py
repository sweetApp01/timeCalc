from app.calculator import TimeCalculator

def test_calculator():
    calc = TimeCalculator()
    
    # Тест парсинга
    assert calc.parse_time("1ч 30м 20с") == 3600 + 30*60 + 20
    assert calc.parse_time("10с") == 10
    assert calc.parse_time("2ч") == 7200
    
    # Тест форматирования
    assert calc.format_time(3661) == "1ч 1м 1с"
    assert calc.format_time(60) == "1м"
    assert calc.format_time(0) == "0с"
    
    # Тест операций
    assert calc.calculate("1ч", "+", "30м") == "1ч 30м"
    assert calc.calculate("1ч", "-", "30м") == "30м"
    assert calc.calculate("1ч", "*", "2") == "2ч"
    assert calc.calculate("1ч", "/", "2") == "30м"
    
    # Граничные случаи
    assert calc.calculate("10м", "-", "20м") == "0с" # Отрицательные не нужны
    assert calc.calculate("1ч", "/", "0") == "Ошибка: деление на ноль"
    
    print("Все тесты пройдены!")

if __name__ == "__main__":
    test_calculator()
