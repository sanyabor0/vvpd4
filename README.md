# Проект: Вычисление функций с использованием рядов Маклорена

### 📜 **Описание проекта**
Этот проект реализует вычисление элементарных функций (гиперболический косинус и натуральный логарифм) с использованием разложения в ряды Маклорена. Также включена возможность работы с меню для выбора функции, ввода параметров и получения результата.

---

### 📋 **Реализованные функции**
- **Гиперболический косинус**:  
  Формула:  
  ![Формула ch(x)](https://latex.codecogs.com/png.image?\ch(x)%20=%201%20+%20\frac{x^2}{2!}%20+%20\frac{x^4}{4!}%20+%20...%20=%20\sum_{n=0}^{\infty}%20\frac{x^{2n}}{(2n)!})  
  Границы допустимых значений: `-∞ < x < +∞`.

- **Натуральный логарифм (ln(1 + x))**:  
  Формула:  
  ![Формула ln(1+x)](https://latex.codecogs.com/png.image?\ln(1%20+%20x)%20=%20x%20-%20\frac{x^2}{2}%20+%20\frac{x^3}{3}%20-%20...%20=%20\sum_{n=1}^{\infty}%20(-1)^{n+1}%20\frac{x^n}{n})  
  Границы допустимых значений: `-1 < x ≤ 1`.

---

### 🛠 **Установка и запуск**

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:ваш_пользователь/ваш_репозиторий.git
   cd ваш_репозиторий

	2.	Создайте виртуальное окружение и активируйте его:

python3 -m venv .venv
source .venv/bin/activate  # Для Linux/Mac
.venv\Scripts\activate     # Для Windows


	3.	Установите зависимости (если они есть):

pip install -r requirements.txt


	4.	Запустите проект:

python main.py

🔧 Инструкция по использованию
	1.	При запуске программы вам будет предложено выбрать одну из функций:
	•	1: Вычисление ch(x).
	•	2: Вычисление ln(1 + x).
	2.	Введите значение x, учитывая ограничения для каждой функции.
	3.	Результат вычислений будет выведен на экран.

📄 Примеры кода

Пример вызова функции ch(x):

from math import factorial

```def ch(x, n_terms=10):
    """Вычисление гиперболического косинуса через ряд Маклорена."""
    return sum((x ** (2 * n)) / factorial(2 * n) for n in range(n_terms))

print(ch(2))  # Пример вычисления ch(2)```

Пример вызова функции ln(1 + x):

```def ln_1_plus_x(x, n_terms=10):
    """Вычисление натурального логарифма через ряд Маклорена."""
    if not -1 < x <= 1:
        raise ValueError("x должен быть в пределах -1 < x ≤ 1")
    return sum(((-1) ** (n + 1)) * (x ** n) / n for n in range(1, n_terms + 1))

print(ln_1_plus_x(0.5))  # Пример вычисления ln(1 + 0.5)```

✅ Функциональность
	•	Реализация функции ch(x)
	•	Реализация функции ln(1 + x)
	•	Проверка граничных значений для x
	•	Меню для выбора функции
	•	Возможность ввода значения x с клавиатуры

📚 Документация

Каждая функция в коде содержит документацию в формате Docstring, описывающую:
	•	Краткое описание
	•	Подробное описание
	•	Аргументы
	•	Возвращаемое значение
	•	Исключения
	•	Примеры использования

📊 Формулы

Формулы для функций, реализованных в проекте:
	•	Гиперболический косинус:

	•	Натуральный логарифм:

🖼 Скриншоты

Пример работы программы:
(Добавьте сюда изображение экрана с выполнением программы, если нужно.)

🤝 Сотрудничество

Если вы работаете с напарником:
	1.	Форкните репозиторий.
	2.	Реализуйте свою часть функций.
	3.	Сделайте pull request для объединения изменений.

📜 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. файл LICENSE.

📝 Контакты

Автор: Ваше имя
GitHub: ваш_пользователь

Теперь весь код в `README.md` отображается корректно благодаря использованию тройных обратных кавычек (\`\`\`).
