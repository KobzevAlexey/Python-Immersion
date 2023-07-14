# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction as F
import math

str_1 = input('Введите первую дробь: ')
str_2 = input('Введите вторую дробь: ')

numerator1, denominator1 = map(int, str_1.split('/'))
numerator2, denominator2 = map(int, str_2.split('/'))

# Умножение
mul_result = numerator1 * numerator2, denominator1 * denominator2
mul_result = mul_result[0] // math.gcd(mul_result[0], mul_result[1]), mul_result[1] // math.gcd(mul_result[0],
                                                                                                mul_result[1])

# Сложение
add_result = numerator1 * denominator2 + numerator2 * denominator1, denominator1 * denominator2
add_result = add_result[0] // math.gcd(add_result[0], add_result[1]), add_result[1] // math.gcd(add_result[0],
                                                                                                add_result[1])

print(f"Результат умножения: {mul_result[0]}/{mul_result[1]}")
print(f"Результат сложения: {add_result[0]}/{add_result[1]}")

# Fractions для проверки
fraction1 = F(str_1)
fraction2 = F(str_2)

print(fraction1 * fraction2)
print(fraction1 + fraction2)

