

from action import ActionType
import config

class Commander:
    def __init__(self, text: str) -> None:
        self.__args = text.split()
        self.__cmd = self.__args[0]
        self.__content_key = " ".join(self.__args[1:])

    def cmd(self):
        return self.__cmd

    
    def get_task_by_action(self, action_type):
        task = { 'datasource': None, 'vk_api': None, 'action_type': action_type, 'message': None, 'content_key': None }
        if (action_type == ActionType.HELP.value):
            task.update(datasource = 'find_commands')
            task.update(vk_api = 'send_message')

        if (action_type == ActionType.EAT.value):
            task.update(vk_api = 'send_message')
            task.update(message = 'Ням-ням :3')

        if (action_type == ActionType.MAP.value):
            task.update(vk_api = 'send_message')
            task.update(message = config.map)

        if (action_type == ActionType.GUIDE.value):
            print('__content_key', self.__content_key)
            task.update(datasource = 'get_content')
            task.update(content_key = self.__content_key)
            task.update(vk_api = 'send_message')

        if (action_type == ActionType.LEVELING.value):
            task.update(datasource = 'get_content')
            task.update(content_key = self.__content_key)
            task.update(vk_api = 'send_message')

        if (action_type == ActionType.WORKSHEET.value):
            task.update(vk_api = 'send_message')
            task.update(message = config.in_developing)

        if (action_type == ActionType.FARMING.value):
            task.update(vk_api = 'send_message')
            task.update(message = config.in_developing)

        if (action_type == ActionType.BAR.value):
            task.update(vk_api = 'send_message')
            task.update(message = config.bar_link)

        if (action_type == ActionType.ALERT.value):
            task.update(vk_api = 'send_message')
            task.update(message = config.in_developing)

        return task


        

