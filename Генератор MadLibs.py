# Mad Libs Random Story Generator

from random import randint
import copy

story = (
    "Однажды мой {} мы с другом решили пойти {} на игру в{}." +
    "Мы действительно хотели посмотреть {} как играют {}." +
    "Итак, мы {} спустились в магазин {} и купили немного {}" +
    "Мы включились в игру, и это было очень весело." +
    "Мы съели немного {} {} и выпили немного {} {}." +
    "Мы отлично провели время! Мы планируем продолжить в следующем году!"
    )

# create a dictionary to lookup words by type
word_dict = {
    "Имя прилагательное":['жадный', 'грубый', 'грязный', 'сытный', 'резкий', 'вкусный'],
    "Названия города":['Чикаго', 'Нью-Йорк', 'Шарлотта', 'Индианаполис', 'Луисвилл', 'Денвер'],
    "Существительное":['люди', 'карта', 'музыка', 'собака', 'хомяк', 'мяч', 'хот-дог', 'салат'],
    "Глагол действия":['беги', 'падай', 'ползи', 'беги', 'плачь', 'смотри', 'плавай', 'прыгай', 'подпрыгивай'],
    "Спортивное существительное":['мяч', 'мельница', 'шайба', 'форма', 'шлем', 'табло', 'игрок'],
    "Место":['парк', 'пустыня', 'лес', 'магазин', 'ресторан', 'водопад']
    }

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0,cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('Имя прилагательное', local_dict),
        get_word('Спортивное существительное', local_dict),
        get_word('Названия города', local_dict),
        get_word('Существительное', local_dict),
        get_word('Существительное', local_dict),
        get_word('Глагол действия', local_dict),
        get_word('Существительное', local_dict),
        get_word('Место', local_dict),
        get_word('Существительное', local_dict),
        get_word('Имя прилагательное', local_dict),
        get_word('Существительное', local_dict),
        get_word('Имя прилагательное', local_dict),
        get_word('Существительное', local_dict),
        )

print("История 1:")
print(create_story())
print()
print("История 2:")
print(create_story())
