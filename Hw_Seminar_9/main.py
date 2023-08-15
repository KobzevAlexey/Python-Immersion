# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


from random import choice, randint as ri
import csv
import json


def csv_reader(path: str = 'abc.csv') -> list[tuple]:
    result = []
    with open(path, 'r', encoding='UTF-8') as file:
        reader = csv.reader(file, dialect='excel', delimiter=';')
        for row in reader:
            if row:
                result.append(tuple(map(float, row)))
    return result


def json_writer(result: dict, path: str = 'result.json'):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def deco_abs(func):
    abc_list = csv_reader()

    def inner():
        result = {}
        for abc in abc_list:
            roots = func(abc)
            a, b, c = abc
            result[f'{a=}, {b=}, {c=}'] = roots
        return result

    return inner


def deco_json_writer(func):
    def inner():
        roots = func()
        json_writer(roots)
        return roots

    return inner


def generate_abc(count: int = 100):
    final_abc = []
    for _ in range(count):
        final_abc.append((choice([*range(-100, 0), *range(1, 101)]), ri(-100, 100), ri(-100, 100)))
    with open('abc.csv', 'w', encoding='UTF-8') as file:
        csv.writer(file, dialect='excel', delimiter=';').writerows(final_abc)


@deco_json_writer
@deco_abs
def quadro_solution(abc: tuple[int, int, int]) -> tuple:
    a, b, c = abc
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif discriminant == 0:
        return round(-b / (2 * a), 2),
    else:
        return None,


generate_abc(1000)
print(quadro_solution())
