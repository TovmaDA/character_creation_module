from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def calculateSquareRoot(number) -> float:
    """Вычисляет квадратный корень."""
    if number <= 0:
        return
    else:
        return sqrt(number)


def calc(your_number) -> str:
    """Проверят что число не меньше или не равно 0, и выводит квадрат числа."""
    if your_number <= 0:
        return
    your_number = calculateSquareRoot(your_number)
    print(
        'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {your_number}'
    )


print(message)
calc(25.5)
