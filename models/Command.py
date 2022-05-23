from commander import Commander
import helpers
from models.Base import Base


class CommandModel(Base):

    ACTION_TYPES = {'get_command': 1, 'find_commands': 2,
                    'get_content': 3, 'find_contents': 4, 'add_content': 5, 'update_content': 6, 'user_warn': 7, 'create_warn': 8, 'delete_warn': 9, 'create_ban': 10, 'profile': 11}

    def __init__(self) -> None:
        Base.__init__(self, table_name='commands', primary_key='name',
                      schema=None, timestamp=False, sync=False)

    def find_commands(self):
        commands = self.findall(None, ['sort', 'ASC'])
        text = ''
        for command in commands:
            text += f"{command.get('icon')}{command.get('name')} - {command.get('help')}\n"
        return text

    def get_custom_key(self, command, commander: Commander):

        if (command.get('custom_key')):

            if (command.get('custom_key') == 'current_day_of_week'):
                key = helpers.current_week_day()
                return key

            if (command.get('custom_key') == 'from_reply_id'):
                key = commander.from_reply_id
                return key

        return None
