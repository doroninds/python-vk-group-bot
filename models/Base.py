from drivers.sqlite import SqliteDatasource, sqlite_connection


class Base(SqliteDatasource):
    def __init__(self, table_name, primary_key: None, schema, timestamp: False, sync) -> None:
        self.__table_name = table_name
        self.__primary_key = primary_key
        SqliteDatasource.__init__(self, sqlite_connection)
        if (schema and sync):
            ddl = self.__ddl(table_name, schema, timestamp)
            SqliteDatasource.query(self, ddl)

    def findbypk(self, value):
        "Find by primary key"
        return SqliteDatasource.fetchone(self, self.__table_name, None, {'field': self.__primary_key, 'value': value})

    def findone(self, where_options=None, sort=None):
        return SqliteDatasource.fetchone(self, self.__table_name, None, where_options, sort)

    def count(self, where_options=None, sort=None):
        return SqliteDatasource.count(self, self.__table_name, None, where_options, sort)

    def findall(self, where_options=None, sort=None):
        return SqliteDatasource.fetchall(self, self.__table_name, None, where_options, sort)

    def create(self, fields, data):
        return SqliteDatasource.insert(self, self.__table_name, fields, data)

    def update(self, where_options, update_options):
        return SqliteDatasource.update(self, self.__table_name, where_options, update_options)

    def query(self, sql):
        return SqliteDatasource.query(self, sql)

    def __ddl(self, table_name, fields, timestamp):
        DDL = f'CREATE TABLE  IF NOT EXISTS "{table_name}" (\n'

        for field in fields:
            DDL += f'{field} {fields.get(field)},\n'

        if (timestamp):
            DDL += 'created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,\n'
            DDL += 'updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,\n'

        DDL = DDL.rstrip(',\n')
        DDL += '\n);'
        return DDL

    @staticmethod
    def schema_type(type=str, nullable=True, primary_key=False, default_value=None):

        columnType = f'{type}'
        field = ''

        if (type == int):
            columnType = 'INTEGER'

        if (type == str):
            columnType = 'STRING'

        if (type == bool):
            columnType = 'BOOLEAN'

        field += columnType

        if (nullable == False):
            field += ' NOT NULL'

        if (primary_key):
            field += ' PRIMARY KEY'

        if (default_value != None):
            field += f' DEFAULT "{default_value}"'

        return field
