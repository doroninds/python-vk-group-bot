from commander import Commander
import settings
import vk_api

# Импортируем методы longpoll бота
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from library.vk import VkBotMessanger
from task_manager import TaskManager

class LongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print('[Exception] BotLongPoll.listen', e)

# инициализация vk api
vk = vk_api.VkApi(token=settings.VK_API_TOKEN)

# инициализация longpoll бота
botLongpoll = LongPoll(vk=vk, group_id=settings.VK_BOT_GROUP_ID)

bot_messanger = VkBotMessanger(vk)
task_manager = TaskManager(bot_messanger)

print('Bot started')
# Слушаем longpoll(Сообщения)
for event in botLongpoll.listen():
    try:
            if event.type == VkBotEventType.MESSAGE_NEW:
                commander = Commander(event)
                if (commander.is_command):
                    task_manager.process_command(commander)
                else:
                    task_manager.process_text(commander)
    except Exception as e:
        print('[Exception] event listen', e)
