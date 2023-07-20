# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

from collections import Counter

friends = {}

while True:
    friend_name = input('Укажите имя друга или введите "exit": ')
    if friend_name == 'exit':
        break
    item = input('Какие вещи он взял?: ').split()
    friends[friend_name] = item

common_set = set()

for i in friends.values():
    common_set.update(i)

print(f"Все вещи: {', '.join(common_set)}.")

unique_set = set()

for i in friends:
    temp = set(friends[i])
    for j in friends:
        if j == i:
            continue
        temp -= set(friends[j])
    if temp:
        print(f"{', '.join(temp)} есть только у {i}")
        unique_set.update(temp)

except_things = Counter(sum([list(i) for i in friends.values()], start=[]))
for i in except_things:
    if except_things[i] == len(friends) - 1:
        for j in friends:
            if i not in friends[j]:
                print(f"{j} не взял {i}.")
