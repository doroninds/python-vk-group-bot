from action import ActionType
from commander import Commander
import traceback
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
botLongpoll = VkBotLongPoll(vk=vk, group_id=config.group_id, wait=20)


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

        mapper = DataMapper.mapping_by_action_type(task, data)
  
        if (mapper and mapper['type'] == 'attachment'):
          attachment = mapper['data']

        if (mapper and mapper['type'] == 'message'):
          message = mapper['data']

      if (task['vk_api']):
        if (task['vk_api'] == 'send_message'):
          self.__vk_api.send_message(peer_id, message, attachment)

app = App(vk_api, datasource)
# Слушаем longpoll(Сообщения)

for event in botLongpoll.listen():
    message = BotEvent(event)
    try:
     
      if(event.message.text == ''):
        continue
      if(event.message.text[0] != '!'):
        continue

      if message.type == VkBotEventType.MESSAGE_NEW:

        commander = Commander(message.text, message.from_id, message.reply_from_id)
        action_type = datasource.get_action_type_by_command(commander.cmd())

        # Если тип события существует - формируем задачу
        if (action_type and action_type > 0):
            task = commander.get_task_by_action(action_type)
            app.process_task(task, message.peer_id)
          
    except Exception:
      traceback.print_exc()
      obj = { 'peer_id': message.peer_id, 'random_id': 0, 'message': config.expection_error_message }
      vk.method('messages.send', obj)