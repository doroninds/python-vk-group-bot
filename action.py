from enum import Enum


class ActionType(Enum):
    NONE = 0  # отсутствует
    HELP = 1  # команды
    MAP = 2  # карта
    EAT = 3  # покормить
    GUIDE = 4  # гайды
    LEVELING = 5  # прокачка
    FARMING = 6  # что можно фармить
    BAR = 7  # ссылка на другую группу
    ALERT = 8  # ЧС
    WORKSHEET = 9  # анкета
    FARMING_TODAY = 10  # что можно фармить
