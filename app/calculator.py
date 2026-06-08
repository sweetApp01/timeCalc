import re

class TimeCalculator:
    @staticmethod
    def parse_time(time_str: str) -> int:
        """Парсит строку вида '1ч 30м 22с' в общее количество секунд."""
        if not time_str or time_str.strip() == "":
            return 0
        
        hours = 0
        minutes = 0
        seconds = 0
        
        h_match = re.search(r'(\d+)ч', time_str)
        m_match = re.search(r'(\d+)м', time_str)
        s_match = re.search(r'(\d+)с', time_str)
        
        if h_match:
            hours = int(h_match.group(1))
        if m_match:
            minutes = int(m_match.group(1))
        if s_match:
            seconds = int(s_match.group(1))
            
        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def format_time(total_seconds: int) -> str:
        """Преобразует общее количество секунд в формат '1ч 30м 22с'."""
        if total_seconds < 0:
            total_seconds = 0
            
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        parts = []
        if hours > 0:
            parts.append(f"{hours}ч")
        if minutes > 0:
            parts.append(f"{minutes}м")
        if seconds > 0 or not parts:
            parts.append(f"{seconds}с")
            
        return " ".join(parts)

    def calculate(self, time1_str: str, operator: str, operand2: str) -> str:
        """
        Выполняет расчет. 
        operand2 может быть строкой времени (для + и -) или числом (для * и /).
        """
        t1 = self.parse_time(time1_str)
        
        if operator in ['+', '-']:
            t2 = self.parse_time(operand2)
            if operator == '+':
                result = t1 + t2
            else:
                result = max(0, t1 - t2)
        elif operator in ['*', '/']:
            try:
                val = float(operand2)
                if operator == '*':
                    result = int(t1 * val)
                else:
                    if val == 0:
                        return "Ошибка: деление на ноль"
                    result = int(t1 / val)
            except ValueError:
                return "Ошибка: неверное число"
        else:
            return "Ошибка: неверная операция"
            
        return self.format_time(result)
