import datetime
import re

def day_of_week(week_day: str) -> int:
    week = {'понедельник': 0, 'вторник': 1, 'среда': 2,
            'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6}
    return week[week_day]


def week_day(num: int) -> str:
    days = {0: 'понедельник', 1: 'вторник', 2: 'среда',
            3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}
    return days[num]


def current_week_day():
    week_day_num = datetime.datetime.today().weekday()
    return week_day(week_day_num)

def list_get(list, i):
    try:
        return list[i]
    except IndexError:
        return None


def current_datetime():
    return f'{datetime.datetime.now()}'.split('.')[0]


def get_date_ago(days=3):
    date = datetime.datetime.today() - datetime.timedelta(days)
    print(date)
    return date

def get_number_from_string(str):
    num = int(re.search(r'\d+', str).group())
    return num


def days_from_datetime(from_datetime):
    from_date = datetime.datetime.strptime(from_datetime, "%Y-%m-%d %H:%M:%S")
    current_date = datetime.datetime.strptime(current_datetime(), "%Y-%m-%d %H:%M:%S")
    delta = datetime.date(current_date.year, current_date.month, current_date.day) - datetime.date(from_date.year, from_date.month, from_date.day)
    return delta.days