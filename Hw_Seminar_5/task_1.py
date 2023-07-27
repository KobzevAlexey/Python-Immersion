# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def split_path(filepath):
    path, filename = os.path.split(filepath)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension


absolute_filepath = input('Укажите абсолютный путь до файла: ')
path, filename, extension = split_path(absolute_filepath)
print("Путь к файлу:", path)
print("Имя файла:", filename)
print("Расширение:", extension)

