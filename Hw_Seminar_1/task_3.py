# ✔Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
ATTEMPTS = 10
user_num = int(input('Какое число загадал компьютер? >>> '))

while True:
    if user_num == num:
        print('Правильно! Возьми с полки пирожок.')
        break
    elif ATTEMPTS == 1:
        print('Попытки кончились')
        break
    elif user_num > num:
        ATTEMPTS -= 1
        print(f'Меньше. Осталось {ATTEMPTS} попыток.')
        user_num = int(input('Какое число загадал компьютер? >>> '))
    elif user_num < num:
        ATTEMPTS -= 1
        print(f'Больше. Осталось {ATTEMPTS} попыток.')
        user_num = int(input('Какое число загадал компьютер? >>> '))
