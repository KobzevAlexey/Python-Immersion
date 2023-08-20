class Archive:
    """Создайте класс Архив, который хранит пару свойств. Например, число и строку."""
    _string_archive = []
    _number_archive = []

    def __init__(self, string, number):
        """Инициализация класса"""
        self.string = string
        self.number = number
        self._string_archive.append(string)
        self._number_archive.append(number)

    def __str__(self):
        """Метод вывода на печать __str__"""
        return f'строки: {" | ".join(self._string_archive)}, числа: {" | ".join(map(str, self._number_archive))}'

    def __repr__(self):
        """Метод вывода на печать __repr__"""
        return f'Archive("{self.string}", {self.number})'


Archive('one', 1)
Archive('two', 2)
ar = Archive('three', 3)
print(ar)
print(ar.__repr__())
print(f'{ar = }')


class Archive2:
    _string_archive = []
    _number_archive = []

    def __new__(cls, *args, **kwargs):
        if cls._string_archive:
            inst = super().__new__(cls)
            inst.archive = cls._string_archive.copy()
            return inst
        else:
            return super().__new__(cls)

    def __init__(self, string, number):
        self.string = string
        self.number = number
        self._string_archive.append(string)
        self._number_archive.append(number)

    def __str__(self):
        return f'строки: {" | ".join(self._string_archive)}, числа: {" | ".join(map(str, self._number_archive))}'


Archive2('one', 1)
Archive2('two', 2)
Archive2('four', 4)
ar2 = Archive2('tree', 3)
print(ar2)
print(ar2.archive)
