from models.Base import Base


class ContentModel(Base):

    def __init__(self) -> None:
        Base.__init__(self, 'contents', 'key')

    def find_by_command_id(self, p_key, command_id):
        return self.findone([{ 'field': 'key', 'value': p_key}, { 'field': 'command_id', 'value': command_id}], ['created_at', 'DESC'])

    def find_contents(self, where_options):
        contents = self.findall(where_options)
        text = ''
        for content in contents:
            text += f"{content.get('key')} - {content.get('text')}\n"
        return text

    def create_or_update_content(self, fields, data):
        print('fields', fields)
        fields.append('created_at')
        fields.append('updated_at')
        data.append('CURRENT_TIMESTAMP')
        data.append('CURRENT_TIMESTAMP')
        print('fields', fields)
        self.create(fields, data)

    def update_content(self, where_options, update):

        print('update', update)
 
        self.update(where_options, update)