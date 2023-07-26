# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хэшируем, используйте его строковое представление.


def my_func(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if isinstance(key, str):
            my_dict[key] = value
        else:
            my_dict[str(key)] = value
    return my_dict


print(my_func(name='Vasya', form='human', planet='Earth', age=18, skills='drinks a bottle of vodka in a gulp'))
