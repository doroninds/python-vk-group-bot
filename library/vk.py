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

    
    def ban(self, peer_id, user_id) -> None:
    
        try:
            chat_id = peer_id - 2000000000
            data = {'chat_id': chat_id, 'user_id': user_id }
            print('data', data)
            self.__vk_api.method('messages.removeChatUser', data)
        
        except Exception as e:
            print('[Exception] VkBotMessanger.send_message', e)
    
    def chat_members(self, peer_id) -> None:
        try:
            data = {'peer_id': peer_id }
            data = self.__vk_api.method('messages.getConversationMembers', data)
            print('data', data)
        
        except Exception as e:
            print('[Exception] VkBotMessanger.send_message', e)