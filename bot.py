from commander import Commander
import traceback
import settings
import vk_api
# Импортируем методы longpoll бота
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from library.vk import VkBotMessanger
from task_manager import TaskManager


class MyVkLongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print('error', e)
                bot_messanger.send_message(
                    settings.DEFAULT_PEER_ID, settings.ALERT_MESSAGE)


# инициализация vk api
vk = vk_api.VkApi(token=settings.VK_API_TOKEN)
session = vk.get_api()

# инициализация longpoll бота
botLongpoll = MyVkLongPoll(vk=vk, group_id=settings.VK_BOT_GROUP_ID)

bot_messanger = VkBotMessanger(vk)
task_manager = TaskManager(bot_messanger)


# Слушаем longpoll(Сообщения)
for event in botLongpoll.listen():
    try:
            if(event.message.text == ''):
                continue

            if(event.message.text[0] != '!'):
                continue

            print('event', event)

            if event.type == VkBotEventType.MESSAGE_NEW:
                commander = Commander(event)
                task_manager.process_command(commander)
    except Exception:
            traceback.print_exc()
