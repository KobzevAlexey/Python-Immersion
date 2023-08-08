# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
# имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def rename_group(path: str = os.getcwd(),
                 new_name: str = '',
                 count: int = 1,
                 in_ext: str = '',
                 out_ext: str = '___',
                 limit: tuple = (0, 10)):
    counter = 1
    if os.path.isdir(path):
        for file in os.listdir(path):
            name, ext = file.rsplit('.', 1)
            if ext == in_ext or not in_ext:
                re_name = f'{name[limit[0]:limit[1]]}{new_name if new_name else ""}{counter:0>{count}}.{out_ext}'
                os.rename(os.path.join(path, file), os.path.join(path, re_name))
                counter += 1
        print(f'Было переименовано {counter - 1}')
    else:
        print('Это не директория!')


rename_group(path='trash', new_name='NEW', in_ext='mp3', out_ext='wav', count=3, limit=(3, 6))
