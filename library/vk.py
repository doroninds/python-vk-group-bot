from vk_api import VkApi

class VkBotMessanger:
  def __init__(self, vk_api: VkApi) -> None:
      self.__vk_api = vk_api   
  
  def send_message(self, peer_id, text = None, attachment = None) -> None:
      message = { 'peer_id': peer_id }

      message.update({ 'random_id': 0 })
      message.update({ 'message': text })
      message.update({ 'attachment': attachment })
    
      self.__vk_api.method('messages.send', message)