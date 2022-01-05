from commander import Commander
import config
import vk_api
from database import DataMapper, Datasource, Db
# Импортируем методы longpoll бота
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Импортируем вспомогательные классы для работы с ботом и vk api
from vk import BotEvent, VkBotExtension


# инициализация vk api
vk = vk_api.VkApi(token=config.token)
session = vk.get_api()

# инициализация longpoll бота
botLongpoll = VkBotLongPoll(vk=vk, group_id=config.group_id)


# Инициализации БД и DataSource
datasource = Datasource(Db())
vk_api = VkBotExtension(vk)


class App:
  def __init__(self, _vk_api: VkBotExtension, _datasource: Datasource) -> None:
      self.__vk_api = _vk_api
      self.__datasource = _datasource

  def process_task(self, task, peer_id):
      message = None
      attachment = None
      if (task['message']):
          message = task['message']

      if (task['datasource']):
        data = self.__datasource.query_by_task(task)
        mapper = DataMapper.mapping_by_action_type(task['action_type'], data)
        print('mapper', mapper)

        if (mapper['type'] == 'attachment'):
          attachment = mapper['data']

        if (mapper['type'] == 'message'):
          message = mapper['data']

      if (task['vk_api']):
        print('message', message)
        print('attachment', attachment)
        self.__vk_api.send_message(peer_id, message, attachment)

app = App(vk_api, datasource)
# Слушаем longpoll(Сообщения)
for event in botLongpoll.listen():
    bot_event = BotEvent(event)
    if(event.message.text == ''):
      continue
    if bot_event.type == VkBotEventType.MESSAGE_NEW:
      commander = Commander(bot_event.text)
      action_type = datasource.get_action_type_by_command(commander.cmd())
      if (action_type and action_type > 0):
            peer_id = bot_event.peer_id
            task = commander.get_task_by_action(action_type)
            app.process_task(task, peer_id)

           
