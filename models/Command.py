import enum
from commander import Commander
import helpers
from models.Base import Base


class CommandType(enum.Enum):
    UNKNOWN = 0
    GET_COMMAND = 1
    FIND_COMMANDS = 2
    GET_CONTENT = 3
    FIND_CONTENTS = 4
    ADD_CONTENT = 5
    UPDATE_CONTENT = 6
    USER_WARN = 7
    CREATE_WARN = 8
    DELETE_WARN = 9
    CREATE_BAN = 10
    PROFILE = 11
    UPDATE_NICKNAME = 12
    UPDATE_BIO = 13


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
