from models.Base import Base


class ContentModel(Base):

    def __init__(self) -> None:
        Base.__init__(self, table_name='contents', primary_key='key',
                      schema=self.__schema(), timestamp=True, sync=True)

    def __schema(self):

        return {
            'key': Base.schema_type(type=str, nullable=False),
            'text': Base.schema_type(str),
            'attachment': Base.schema_type(str),
            'command_id': Base.schema_type(int, nullable=False, default_value='0'),
        }

    def find_by_command_id(self, p_key, command_id):
        return self.findone([{'field': 'key', 'value': f'{p_key}'.lower()}, {'field': 'command_id', 'value': command_id}], ['created_at', 'DESC'])

    def find_contents(self, where_options):
        contents = self.findall(where_options)
        text = ''
        for content in contents:
            text += f"{content.get('key')} - {content.get('text')}\n"
        return text

    def create_or_update_content(self, fields, data):
        fields.append('created_at')
        fields.append('updated_at')
        data.append('CURRENT_TIMESTAMP')
        data.append('CURRENT_TIMESTAMP')
        self.create(fields, data)

    def update_content(self, where_options, update):
        self.update(where_options, update)
