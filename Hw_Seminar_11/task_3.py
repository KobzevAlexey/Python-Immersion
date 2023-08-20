import time
from getpass import getuser


class MyString(str):
    """Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания
    (time.time)"""

    def __new__(cls, *args, **kwargs):
        """Создание класса"""
        instance = super().__new__(cls, *args, **kwargs)
        instance.name = getuser()
        instance.log = time.ctime()
        return instance

    def __repr__(self):
        """Метод вывода на печать __repr__"""
        return f'MyString("{self}")'


my_str = MyString('text')
print(f'Сама строка(объект): "{my_str}", имя автора: "{my_str.name}", дата/время: "{my_str.log}"')
print(f'{my_str = }')