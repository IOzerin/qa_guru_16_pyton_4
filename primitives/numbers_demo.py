
from decimal import Decimal

# Переменная
a = 123

# Математические действия с переменными
a = a + 456
a = a - 456
a = a * 456
a = a / 456

# Возведение в степень
a = a ** 3

# Системы счисления
# Двоичная система счисления в начале обязательно ставить 0b (b - binary)
a = 0b0101
# Восьмиричная система счиления в начале числа ставим 0o
a = 0o1234567
# Шеснадцатиричная система счисления в начале числа ставим 0x
a = 0x1234567890abcdef


# Дробные числа записываются не через запятую, а через точку
a = 0.5
print(a)

a = 0.1 + 0.2
print(a)
# assert a == 0.3
# Код выдает ошибку так как в языках программирования используется плавающая запятая,
# в этом случае следует использовать специальный тип данных "decimal" (from decimal import Decimal)

# Округлять дробные числа можно с помощью следующей команды
# round(1.666666666, 2)
print(round(1.666666666, 2))
print(round(1.333333333, 2))
print(round(1.3659, 3))


# Для математических операций есть специальная библиотека "math"
import math

print(math.pi)

# Рандом
# Импортируем соответствующую библиотеку "random"
import random

# seed используется для генерации одних и тех же случайных данных,
# которые будут зависеть от написанного в скобках
random.seed("some word")

# randint выводит случайное целое число с заданным диапазоном, в данном случае диапазон от 0 до 100
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

# Библиотека для специфичных типов данных Faker
# from faker import Faker







