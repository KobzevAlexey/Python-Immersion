import os
import string
import random


def create_random_files(quantity: int):
    file_ext = ['txt', 'jpg', 'mov', 'mp3']
    directory = 'trash'
    os.makedirs(directory, exist_ok=True)
    for _ in range(quantity):
        name = os.path.join('trash', ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(file_ext))
        with open(name, 'w', encoding='utf-8') as file:
            file.write(name)


create_random_files(20)
