# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число: '))

print(hex(num))

hex_digits = '0123456789abcdef'
HEX = 16
result = ''

while num > 0:
    remainder = num % HEX
    result = hex_digits[remainder] + result
    num = num // HEX

print('0x' + result)


