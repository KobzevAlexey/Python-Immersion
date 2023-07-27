# Создайте функцию генератор чисел Фибоначчи


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_numbers = fibonacci()
n = int(input('Укажите сколько чисел вывести на экран: '))
numbers = [str(next(fib_numbers)) for _ in range(n)]
print(', '.join(numbers))
