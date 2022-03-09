from logging import exception
from vk_api import VkApi


class VkBotMessanger:
    def __init__(self, vk_api: VkApi) -> None:
        self.__vk_api = vk_api

    def send_message(self, peer_id, text=None, attachment=None) -> None:
    
        try:
            message = {'peer_id': peer_id, 'random_id': 0,
                   'message': text, 'attachment': attachment }

            self.__vk_api.method('messages.send', message)
        
        except Exception as e:
            print('[Exception] VkBotMessanger.send_message', e)

