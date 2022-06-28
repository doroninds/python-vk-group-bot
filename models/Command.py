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
    ADD_REWARD = 14
    REMOVE_REWARD = 15
    REWARDS = 16
    USER_STATS = 17

class CommandModel(Base):

    ACTION_TYPES = {'get_command': 1, 'find_commands': 2,
                    'get_content': 3, 'find_contents': 4, 'add_content': 5, 'update_content': 6, 'user_warn': 7, 'create_warn': 8, 'delete_warn': 9, 'create_ban': 10, 'profile': 11}

    def __init__(self) -> None:
        Base.__init__(self, table_name='commands', primary_key='name',
                      schema=self.__schema(), timestamp=True, sync=True)

    def __schema(self):

        return {
            'id': Base.schema_type(type=int, nullable=False),
            'name': Base.schema_type(str, nullable=False, primary_key=True),
            'action_type': Base.schema_type(int),
            'help': Base.schema_type(str),
            'admin_only':  Base.schema_type(bool, nullable=False, default_value='0'),
            'text': Base.schema_type(str),
            'attachment': Base.schema_type(str),
            'custom_key': Base.schema_type(str),
            'bind_id': Base.schema_type(int),
            'success': Base.schema_type(str),
            'fail': Base.schema_type(str),
            'sort': Base.schema_type(int, nullable=False, default_value='0'),
            'icon': Base.schema_type(str),
            'template': Base.schema_type(str),
            'alias': Base.schema_type(str),
        }

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
                key = commander.from_reply_or_from_id
                return key

        return None
