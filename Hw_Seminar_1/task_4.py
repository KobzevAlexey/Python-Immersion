from random import randint

ATTEMPTS = 10
MIN = 0
MAX = 1000
num = randint(MIN, MAX)

print(f'Загадайте число от {MIN} до {MAX}. А я попробую его угадать за {ATTEMPTS} попыток.')

while True:
    print(f'Вы загадали {num}?')
    answer = str(input('Введите yes, bigger или smaller >>> '))
    if answer == 'yes':
        print('Я угадал. Какой я молодец.')
        break
    elif ATTEMPTS == 1:
        print('У меня кончились попытки.')
        break
    elif answer == 'bigger':
        ATTEMPTS -= 1
        print(f'Осталось {ATTEMPTS} попыток.')
        MIN = num
        num = int(num + (MAX - num) / 2)

    elif answer == 'smaller':
        ATTEMPTS -= 1
        print(f'Осталось {ATTEMPTS} попыток.')
        MAX = num
        num = int(MAX - ((MAX - MIN) / 2))