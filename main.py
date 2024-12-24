import math


def maclaurin_cosh(x: float, iterations: int = 10) -> float:
    """
    Вычисляет гиперболический косинус через ряд Маклорена (cosh(x)).

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


def maclaurin_ln1p(x: float, iterations: int = 10) -> float:
    """
    Вычисляет натуральный логарифм (ln(1+x)) через ряд Маклорена (ln(1+x)).

    Аргументы:
        x (float): значение (должно быть в диапазоне (-1, 1]).
        iterations (int): количество итераций для точности вычислений.

    Возвращаемое значение:
        float: значение ln(1+x).

    Исключения:
        ValueError: если x не в допустимом диапазоне или iterations <= 0.

    Пример:
        >>> maclaurin_ln1p(0.5)
        0.4054651081081644
    """
    if not (-1 < x <= 1):
        raise ValueError("x должен быть в диапазоне (-1, 1].")
    if iterations <= 0:
        raise ValueError("Количество итераций должно быть больше 0.")

    result = 0
    for n in range(1, iterations + 1):
        term = ((-1) ** (n + 1)) * (x ** n) / n
        result += term
    return result


def main_menu():
    """
    Главное меню программы для вычисления функций.
    """
    while True:
        print("\n--- Главное меню ---")
        print("1. Вычислить cosh(x)")
        print("2. Вычислить ln(1+x)")
        print("3. Выход")

        choice = input("Введите номер операции: ")
        if choice == "1":
            try:
                x = float(input("Введите x: "))
                result = maclaurin_cosh(x)
                print(f"Результат: cosh({x}) = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            try:
                x = float(input("Введите x (в диапазоне (-1, 1]): "))
                result = maclaurin_ln1p(x)
                print(f"Результат: ln(1+{x}) = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main_menu()