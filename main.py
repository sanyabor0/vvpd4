import math


def maclaurin_cosh(x: float, iterations: int = 10) -> float:
    """
    Вычисляет гиперболический косинус через ряд Маклорена.

    Аргументы:
        x (float): значение, для которого вычисляется гиперболический косинус.
        iterations (int): количество итераций для точности вычислений.

    Возвращаемое значение:
        float: значение гиперболического косинуса.

    Исключения:
        ValueError: если iterations <= 0.

    Пример:
        >>> maclaurin_cosh(1)
        1.5430806348152437
    """
    if iterations <= 0:
        raise ValueError("Количество итераций должно быть больше 0.")

    result = 0
    for n in range(iterations):
        term = (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result