from random import choice

_answers_count = {}


def quest(question, answers, try_count):
    count = try_count
    while try_count > 0:
        print(question)
        answer = input('Ваш ответ?  >>>  ')
        if answer in answers:
            _answers_count[question] = count - try_count + 1
            print(f'Бинго, ты отгадал за {count - try_count + 1} попыток!')
            break
        else:
            print('Ответ неверный!')
            try_count -= 1
    if not try_count:
        print("Попытки исчерпаны...")


def more_quests(iters):
    quests = {'Сколько ног у муравья': ['4', '5', '6'],
              'Какого цвета огнетушитель?': ['Красный', "Синий"],
              "Сколько лет тебе было в детстве?": [str(i) for i in range(19)],
              'Идут два крокодила, один зеленый, другой направо. Зачем мне холодильник, если я не курю?': ['Да',
                                                                                                           "Гладиолус",
                                                                                                           "ПеЖо"]}

    for i in range(iters):
        temp = choice(list(quests.keys()))
        quest(temp, quests[temp], 3)


def how_many_answers():
    print(*(f'Загадка {key[:10]}... была отгадана за {value} попыток' for key, value in _answers_count.items()),
          sep='\n')
