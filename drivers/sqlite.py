import sqlite3
from sqlite3 import Connection
import settings

# Инициализируем соединение с sqlite
sqlite_connection = sqlite3.connect(settings.DATABASE, check_same_thread=False)

class SqliteDatasource:

    def __init__(self, connection: Connection) -> None:
        self.__connection: Connection = connection
        self.__connection.row_factory = self.__dict_factory
        self.__query = ''

    def fetchone(self, table_name, fields, where_options = None, sort: list = None):
        cursor = self.__connection.cursor()
        sql = self.__query_builder(table_name, fields, where_options, sort)
        cursor.execute(sql)
        return cursor.fetchone()

    def fetchall(self, table_name, fields, where_options = None, sort: list = None):
        cursor = self.__connection.cursor()
        sql = self.__query_builder(table_name, fields, where_options, sort)
        cursor.execute(sql)
        return cursor.fetchall()
    
    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


    def insert(self, table_name, fields, data):
        cursor = self.__connection.cursor()
        columns = ', '.join(fields)
        values = ', '.join(data)
        sql = f'INSERT INTO {table_name} ({columns}) VALUES ({values})'
        cursor.execute(sql)
        
        self.__connection.commit()

    def query(self, sql):
        cursor = self.__connection.cursor()
        cursor.execute(sql)
        self.__connection.commit()

    def delete(self, table_name, fields, data):
        cursor = self.__connection.cursor()
        columns = ', '.join(fields)
        values = ', '.join(data)
        sql = f'INSERT INTO {table_name} ({columns}) VALUES ({values})'
        cursor.execute(sql)
        
        self.__connection.commit()

    def update(self, table_name, where_options, update_options):
        cursor = self.__connection.cursor()

        # empty sql statement
        self.__clear()
        self.__query += f'UPDATE {table_name}'
        self.__set(update_options)
        self.__where(where_options)
        sql = self.__get()
        self.__clear()

        cursor.execute(sql)
        self.__connection.commit()
        

    def __query_builder(self, table_name, fields, where_options = None, sort: list = None):
        sql = self.__select(table_name, fields).__where(where_options).__order_by(sort).__get()
        return sql

    def __select(self, table_name, fields = '*'):
        self.__query = f'SELECT * FROM {table_name} as t'
        return self

    def __order_by(self, sort: list = None):
        if (sort == None):
            return self
        
        field = sort[0]
        direction = sort[1] or 'ASC'
        self.__query += f' ORDER BY {field} {direction}'
        return self

    def __get(self):
        return self.__query

    def __clear(self):
         self.__query = ''

    def __set(self, set_options: list):
        self.__query += f' SET'
        for i, set_option in enumerate(set_options):
            next_option = ','
            is_last = set_options.__len__() == i + 1

            if (is_last):
                next_option = ''

            self.__query += f" {set_option.get('field')} = \"{set_option.get('value')}\" {next_option}"
      
        return self

    def __where(self, where_options: list = None):
        
        if (where_options == None):
            return self

        if isinstance(where_options, list) == False:
            operator = where_options.get('operator') or '='
            self.__query += f" WHERE {where_options.get('field')} {operator} \"{where_options.get('value')}\""
            return self

        self.__query += f' WHERE'
        for i, where_option in enumerate(where_options):
            operator = where_option.get('operator') or '='
            next_where = 'AND'
            is_last_where = where_options.__len__() == i + 1
            
            if (is_last_where):
                next_where = ''
            self.__query += f" {where_option.get('field')} {operator} \"{where_option.get('value')}\" {next_where}"

        return self 