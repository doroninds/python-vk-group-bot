from drivers.sqlite import SqliteDatasource, sqlite_connection

class Base(SqliteDatasource):

    def __init__(self, table_name, primary_key: None) -> None:
        self.__table_name = table_name
        self.__primary_key = primary_key
        SqliteDatasource.__init__(self, sqlite_connection)

    def findbypk(self, value):
        "Find by primary key"
        return SqliteDatasource.fetchone(self, self.__table_name, None, { 'field': self.__primary_key, 'value': value })

    def findone(self, where_options = None, sort = None):
        return SqliteDatasource.fetchone(self, self.__table_name, None, where_options, sort)

    def findall(self, where_options = None, sort = None):
        return SqliteDatasource.fetchall(self, self.__table_name, None, where_options, sort)

    def create(self, fields, data):
        print('SqliteDatasource', self.__table_name, fields, data)
        return SqliteDatasource.insert(self, self.__table_name, fields, data)

    def update(self, where_options, update_options):
        print('SqliteDatasource', self.__table_name, where_options, update_options)
        return SqliteDatasource.update(self, self.__table_name, where_options, update_options)