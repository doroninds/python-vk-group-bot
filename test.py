from enum import Enum
from database import DataMapper, Db, Datasource
from commander import Commander
from datetime import datetime

print('datetime.datetime.today().weekday()', datetime.datetime.today().weekday())

days = { 0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}
week = { 'понедельник': 0, 'вторник': 1 , 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5 , 'воскресенье': 6 }


print('days', days[datetime.today().weekday()])
print('week', week[days[datetime.datetime.today().weekday()]])

# datasource = Datasource(Db())


# commander = Commander('!команды')


# class Action(Enum):
#     TEST = 1


# print(Action['TEST'])
    

# action_name = datasource.get_action_by_command(commander.cmd())
# print('action_name', action_name)
# tasks = commander.get_task_by_action(action_name)
# print('tasks', tasks, 'tasks.datasource', tasks['datasource'])


# rows = datasource.query_by_method(tasks['datasource'])
 
# print('rows', rows)


# commands = DataMapper.get_help(rows)

# print('commands', commands)