

from commander import Commander
from library.vk import VkBotMessanger
from models.Command import CommandModel
from models.Content import ContentModel


# models
command_datasource = CommandModel()
content_datasource = ContentModel()


class TaskManager:
    def __init__(self, bot_messanger: VkBotMessanger) -> None:
        self.__bot_messanger = bot_messanger

    def process_command(self, commander: Commander):

        text = None
        attachment = None

        if (commander.is_command):
            command = command_datasource.findbypk(commander.cmd)

            if (command == None):
                self.__bot_messanger.send_message(
                    commander.peer_id, 'Команда не найдена или отключена (')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('get_command')):
                text = command.get('text')
                attachment = command.get('attachment')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('find_commands')):
                text = command_datasource.find_commands()

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('get_content')):
                key = command_datasource.get_custom_key(
                    command, commander) or commander.value
                content = content_datasource.find_by_command_id(
                    key, command.get('id'))
                if (content):
                    text = content.get('text')
                    attachment = content.get('attachment')
                else:
                    text = command.get('text')
                    attachment = command.get('attachment')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('create_content')):
                key = commander.from_id
                command_id = command.get('bind_id') or command.get('id')
                content_datasource.create_or_update_content(['key', 'text', 'command_id'], [
                                                            f"'{key}'", f"'{commander.data}'", f"'{command_id}'"])
                text = command.get('text')
                attachment = command.get('attachment')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('find_contents')):
                text = content_datasource.find_contents(
                    {'field': 'command_id', 'value': command.get('id')})

            if (command.get('action_type') == 0):
                self.__bot_messanger.send_message(
                    commander.peer_id, 'Команда не найдена или отключена (')

        self.__bot_messanger.send_message(commander.peer_id, text, attachment)
