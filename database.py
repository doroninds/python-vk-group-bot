import sqlite3
from sqlite3 import Connection
from action import ActionType
import config

class Db:
    def __init__(self) -> None:
        self.__connection: Connection = sqlite3.connect(config.database)

    def query(self, sql, is_one: bool = False):
        cursor = self.__connection.cursor()
        cursor.execute(sql)
        if (is_one):
            return cursor.fetchone()
        else:
            return cursor.fetchall()


class Datasource:
    def __init__(self, db: Db) -> None:
        self.__db = db

    def get_command(self, command_name: str):
        sql = f'select * from commands where name = "{command_name}"'
        row = self.__db.query(sql, is_one=True)
        return row

    def get_content(self, content_key: str, action_type: int):
        print('content_key', content_key, 'action_type', action_type)
        sql = f'select key, action_type, text, attachment from contents where action_type = {action_type} and key = \'{content_key}\''
        row = self.__db.query(sql, is_one=True)
        print('get_content row', row)
        return row

    def get_action_type_by_command(self, command_name: str) -> str:
        sql = f'select action_type from commands where name = "{command_name}"'
        row = self.__db.query(sql, is_one=True)
        if (row):
            return row[0]
        else:
            return ''

    def find_commands(self):
        sql = f'select action_type, name, help from commands order by action_type asc'
        rows = self.__db.query(sql, is_one=False)
        return rows
    
    def query_by_task(self, task):
        if (task['datasource'] == 'find_commands'):
            return self.find_commands()
        if (task['datasource'] == 'get_content'):
            return self.get_content(task['content_key'], task['action_type'])


class DataMapper(object):
    @staticmethod
    def get_help(rows: list):
        commands = ['Список комманд бота:']
        for row in rows:
            commands.append(f'\n[{row[0]}] {row[1]} - {row[2]}')
        return ''.join(commands)

    def get_guide(row: list):
        guide = ''
        if (row[3]):
            guide= row[3]

        return guide

    @staticmethod
    def mapping_by_action_type(action_type, data):
        mapper = { 'data': None, 'type': None }
        if (action_type == ActionType.HELP.value):
            help = DataMapper.get_help(data)
            mapper.update(data = help)
            mapper.update(type = 'message')
            return mapper
            
        if (action_type == ActionType.GUIDE.value):
            
            if (data):
                guide = DataMapper.get_guide(data)
                mapper.update(data = guide)
                mapper.update(type = 'attachment')
            else:
                mapper.update(data = 'Гайд не найден')
                mapper.update(type = 'message')
            return mapper

        if (action_type == ActionType.LEVELING.value):
            
            if (data):
                guide = DataMapper.get_guide(data)
                mapper.update(data = guide)
                mapper.update(type = 'attachment')
            else:
                mapper.update(data = 'Гайд не найден')
                mapper.update(type = 'message')
            return mapper

        return mapper