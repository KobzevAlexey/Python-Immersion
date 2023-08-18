from typing import Any


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}'


class Mammal(Animal):
    def __init__(self, name, age, voice, hair):
        super().__init__(name, age)
        self.voice = voice
        self.hair = hair

    def get_info(self):
        return f'{super().get_info()}, Voice: {self.voice}, Hair: {self.hair}'


class Bird(Animal):
    def __init__(self, name, age, colour, voice):
        super().__init__(name, age)
        self.colour = colour
        self.voice = voice

    def get_info(self):
        return f'{super().get_info()}, Colour: {self.colour}, Voice: {self.voice}'


class Fish(Animal):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def get_info(self):
        return f'{super().get_info()}, Colour: {self.colour}'


class AnimalFabric:

    def __new__(cls, animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal, Any]:
        try:
            animal = animal_type(*args, **kwargs)
            return animal
        except Exception as exc:
            print(f'{exc.__class__.__name__} {exc}')
            return Animal('Cadaver', 1000)

    @staticmethod
    def main():
        dog = AnimalFabric(Mammal, name='Fido', age=5, voice='Woof!', hair='Pale, long')
        fish = AnimalFabric(Fish, name='Vanda', age=1, colour='Rainbow')
        bird = AnimalFabric(Bird, name='Carl', age=8, colour='Black', voice='CRAW!')
        unidentified = AnimalFabric(Animal, name='Fail-Tester', age=100)

        print(dog.get_info(), '\n')
        print(fish.get_info(), '\n')
        print(bird.get_info(), '\n')
        print(unidentified.get_info(), '\n')


if __name__ == '__main__':
    AnimalFabric.main()
