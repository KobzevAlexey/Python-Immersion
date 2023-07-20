# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

# from pprint import pprint

camping_stuff = {'фонарик': 0.1, 'палатка': 2.4, 'котелок': 0.4, 'фляга': 1.17, 'спальник': 0.71, 'пила': 0.2,
                 'нож': 0.15, 'топор': 2.0, 'миска': 0.27, 'кружка': 0.07, 'чайник': 0.4, 'плитка': 2.07,
                 'термос': 1.22, 'МПЛ-50': 0.72, 'коврик': 0.36, 'аптечка': 0.05, 'термоодеяло': 0.1, 'ружьё': 3.6,
                 'патроны': 2.2, 'тушёнка': 2.0, 'гречка': 1.0, 'дождевик': 0.34, 'верёвка': 3.15, 'огниво': 0.07}

# pprint(camping_stuff)
# total_weight = sum(camping_stuff.values())
# print(total_weight)


my_combinations = []
backpack = float(input('Укажите вместимость рюкзака: '))
min_weight = 3

for i in range(len(camping_stuff)):
    my_combinations.extend(list(combinations(camping_stuff, i + 1)))

result = list(filter(lambda x: min_weight <= sum([camping_stuff[i] for i in x]) <= backpack, my_combinations))

print(f"\nВ рюкзак вместительностью {backpack} мы можем взять следующие вещи:\n")
for i in sorted(result, key=lambda x: sum([camping_stuff[i] for i in x]), reverse=False):
    print(f"{', '.join(i)} - суммарная масса: {sum([camping_stuff[j] for j in i])}")
