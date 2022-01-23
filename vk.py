from vk_api import VkApi

# Импортируем методы longpoll бота
from vk_api.bot_longpoll import VkBotEventType, VkBotMessageEvent

class VkBotExtension:

  def __init__(self, vk: VkApi) -> None:
      self.__vk = vk
  
  def send_message(self, peer_id, message = None, attachment = None) -> None:
      obj = { 'peer_id': peer_id, 'random_id': 0 }

      if (message):
        obj['message'] = message
        
      if (attachment):
        obj['attachment'] = attachment

      self.__vk.method('messages.send', obj)

class BotEvent:
  def __init__(self, event: VkBotMessageEvent) -> None:
      self.__peer_id = event.message.peer_id
      self.__text = event.message.text
      self.__type = event.type

  @property
  def peer_id(self) -> int:
      return self.__peer_id

  @property
  def text(self) -> str:
      return self.__text

  @property
  def type(self) -> VkBotEventType:
      return self.__type