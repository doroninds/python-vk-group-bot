from commander import Commander
from helpers import current_week_of_day
from models.Base import Base


class CommandModel(Base):

    ACTION_TYPES = { 'get_command': 1, 'find_commands': 2, 'get_content': 3, 'find_contents': 4, 'create_content': 5 }

    def __init__(self, table_name = 'commands', p_key = 'name') -> None:
        Base.__init__(self, table_name, p_key)

    
    def find_commands(self):
        commands = self.findall()
        text = ''
        for command in commands:
            text += f"{command.get('name')} - {command.get('help')}\n"
        return text

    def get_custom_key(self, command, commander: Commander):

        if (command.get('custom_key')):
            
            if (command.get('custom_key') == 'current_day_of_week'):
                key = current_week_of_day()
                return key

            if (command.get('custom_key') == 'from_reply_id'):
                key = commander.from_reply_id
                return key

        return None
