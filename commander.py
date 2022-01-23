

from action import ActionType
import config
from datetime import datetime


class Commander:
    def __init__(self, text: str, from_id: int, reply_from_id: int) -> None:
        self.__from_id = from_id
        self.__reply_from_id = reply_from_id
        self.__args = text.split()
        self.__cmd = self.__args[0]
        self.__content_key = " ".join(self.__args[1:])
        self.__segments = text.split("\n")
        self.__data = "\n".join(self.__segments[1:])

    def cmd(self):
        return self.__cmd

    def day_of_week(self, week_day: str) -> int:
        week = {'понедельник': 0, 'вторник': 1, 'среда': 2,
                'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6}
        return week[week_day]

    def week_day(self, n: int) -> str:
        days = {0: 'понедельник', 1: 'вторник', 2: 'среда',
                3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}
        return days[n]

    def get_task_by_action(self, action_type):

        task = {'datasource': None, 'vk_api': None, 'action_type': action_type,
                'message': None, 'content_key': None, 'data': None}

        if (action_type == ActionType.HELP.value):
            task.update(datasource='find_commands')
            task.update(vk_api='send_message')

        if (action_type == ActionType.EAT.value):
            task.update(vk_api='send_message')
            task.update(message='Ням-ням :3')

        if (action_type == ActionType.MAP.value):
            task.update(vk_api='send_message')
            task.update(message=config.map)

        if (action_type == ActionType.GUIDE.value):
            task.update(datasource='get_content')
            task.update(content_key=self.__content_key)
            task.update(vk_api='send_message')

        if (action_type == ActionType.LEVELING.value):
            task.update(datasource='get_content')
            task.update(content_key=self.__content_key)
            task.update(vk_api='send_message')

        if (action_type == ActionType.WORKSHEET.value):
            task.update(datasource='get_content')
            task.update(content_key=f'{self.__from_id}')
            if (self.__reply_from_id):
                task.update(content_key=f'{self.__reply_from_id}')
            task.update(vk_api='send_message')


        if (action_type == ActionType.CREATE_WORKSHEET.value):
            task.update(vk_api='send_message')
            task.update(datasource='create_content')
            task.update(action_type=ActionType.WORKSHEET.value)
            task.update(content_key=f'{self.__from_id}')
            task.update(data=self.__data)
            task.update(message=config.create_worksheet_message)

        if (action_type == ActionType.FARMING.value):
            task.update(datasource='get_content')
            task.update(vk_api='send_message')
            task.update(content_key=self.__content_key)

        if (action_type == ActionType.FARMING_TODAY.value):
            current_day = datetime.today().weekday()
            day = self.week_day(current_day)

            task.update(datasource='get_content')
            task.update(vk_api='send_message')
            task.update(content_key=day)

        if (action_type == ActionType.BAR.value):
            task.update(vk_api='send_message')
            task.update(message=config.bar_link)

        if (action_type == ActionType.ALERT.value):
            task.update(datasource='get_content')
            task.update(vk_api='send_message')
            task.update(content_key=self.__cmd)
      
        if (action_type == ActionType.CHECK.value):
            task.update(vk_api='send_message')
            task.update(message=config.check_message)

        return task
