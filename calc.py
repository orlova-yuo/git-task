# Автор: Юлия Орлова

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b

import math
def sqrt(x):
    """Вычисляет квадратный корень."""
    if x < 0:
        raise ValueError("Квадратный корень из отрицательного числа!")
    return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
