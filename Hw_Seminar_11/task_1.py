import time
from getpass import getuser


class MyString(str):

    def __new__(cls, *args, **kwargs):
        """Создайте класс Моя Строка,
        где: будут доступны все возможности str
        дополнительно хранятся имя автора строки и время создания
        (time.time)"""
        instance = super().__new__(cls, *args, **kwargs)
        instance.name = getuser()
        instance.log = time.ctime()
        return instance


my_str = MyString('text')
print(f'Сама строка(объект): "{my_str}", имя автора: "{my_str.name}", дата/время: "{my_str.log}"')
