

from commander import Commander
from library.vk import VkBotMessanger
from models.Command import CommandModel
from models.Content import ContentModel
from models.User import UserModel
from models.Warning import WarningModel
from helpers import list_get
import traceback


# models
command_datasource = CommandModel()
content_datasource = ContentModel()
user_datasource = UserModel()
WarningDataSource = WarningModel()

class TaskManager:
    def __init__(self, bot_messanger: VkBotMessanger) -> None:
        self.__bot_messanger = bot_messanger

    def process_command(self, commander: Commander):
        
        text = None
        attachment = None
        is_user_admin = False

        user = user_datasource.findbypk(commander.from_id)

        if (user != None and user.get('is_admin') == True):
            is_user_admin = True

        if (commander.is_command):
            command = command_datasource.findbypk(commander.cmd)

            if (command == None):
                return

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

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('add_content')):
                key = commander.from_id
                command_id = command.get('bind_id') or command.get('id')
                content_datasource.create_or_update_content(['key', 'text', 'command_id'], [
                                                            f"'{key}'", f"'{commander.data}'", f"'{command_id}'"])
                text = command.get('text')
                attachment = command.get('attachment')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('create_content')):
  
                if (is_user_admin == False):
                    text = command.get('text')
                else:
                    try: 
                        upd_command = command_datasource.findbypk(commander.line_args[1].strip())
                        content_key = commander.line_args[2].strip()
                        content_text = None
                        content_attachment = None

                        if (list_get(commander.line_args, 4)):
                            content_text = list_get(commander.line_args, 4).strip()

                        if (list_get(commander.line_args, 3)):
                            content_attachment = list_get(commander.line_args, 3).strip()

                        update_options = []
                        if (content_text):
                            update_options.append({ 'field': 'text', 'value':  content_text })

                        if (content_attachment):
                            update_options.append({'field':  'attachment', 'value': content_attachment})


                        where_options = [{ 'field': 'command_id', 'value': upd_command.get('id')}, { 'field': 'key', 'value': content_key}]

                   
                        content_datasource.update(where_options, update_options)
                        text = command.get('success')
                    except:
                        traceback.print_exc()
                        text = command.get('fail')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('update_content')):
                user = user_datasource.findbypk(commander.from_id)

   
         
                if (command.get('admin_only') == True and user == None or user.get('is_admin') != True):
                    text = command.get('text')
                else:
                    try: 
                        upd_command = command_datasource.findbypk(commander.line_args[1].strip())
                        content_key = commander.line_args[2].strip()
                        content_text = None
                        content_attachment = None
                 
                        if (list_get(commander.line_args, 4)):
                            content_text = list_get(commander.line_args, 4).strip()

                        if (list_get(commander.line_args, 3)):
                            content_attachment = list_get(commander.line_args, 3).strip()

                        update_options = []

                        if (content_text):
                            update_options.append({ 'field': 'text', 'value':  content_text })

                        if (content_attachment):
                            update_options.append({'field':  'attachment', 'value': content_attachment})

                        where_options = [{ 'field': 'command_id', 'value': upd_command.get('id')}, { 'field': 'key', 'value': content_key}]

                   
                        content_datasource.update(where_options, update_options)
                        text = command.get('success')
                    except:
                        traceback.print_exc()
                        text = command.get('fail')
          
        
            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('find_contents')):
                text = content_datasource.find_contents(
                    {'field': 'command_id', 'value': command.get('id')})

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('create_warn')):
                if (is_user_admin == False):
                    text = command.get('text')
                else:
                    reason = f"'{commander.value}'"
                    user_id = command_datasource.get_custom_key(command, commander)
                
                    data = WarningDataSource.create_warn(user_id, reason)
                    text = command.get('success')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('delete_warn')):
                if (is_user_admin == False):
                    text = command.get('text')
                else:

                    user_id = command_datasource.get_custom_key(command, commander)
                
                    data = WarningDataSource.delete_warn(user_id)
                    text = command.get('success')

            if (command.get('action_type') == command_datasource.ACTION_TYPES.get('user_warn')):
                text = content_datasource.find_contents(
                    {'field': 'command_id', 'value': command.get('id')})

                user_id = command_datasource.get_custom_key(command, commander)
                data = WarningDataSource.find_user_warn(user_id)
                if (data):
                    text = data
                else:
                    text = command.get('text')

            if (command.get('action_type') == 0):
                return
                
        self.__bot_messanger.send_message(commander.peer_id, text, attachment)
