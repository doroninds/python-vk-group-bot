from enum import Enum
from database import DataMapper, Db, Datasource
from commander import Commander

datasource = Datasource(Db())


commander = Commander('!команды')


class Action(Enum):
    TEST = 1


print(Action['TEST'])
    

action_name = datasource.get_action_by_command(commander.cmd())
print('action_name', action_name)
tasks = commander.get_task_by_action(action_name)
print('tasks', tasks, 'tasks.datasource', tasks['datasource'])


rows = datasource.query_by_method(tasks['datasource'])
 
print('rows', rows)


commands = DataMapper.get_help(rows)

print('commands', commands)