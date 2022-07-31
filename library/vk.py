from vk_api import VkApi


class VkBotMessanger:
    def __init__(self, vk_api: VkApi) -> None:
        self.__vk_api = vk_api

    def user_info(self, user_id, fields = 'about,screen_name,nickname') -> None:
        params = {'user_ids': user_id, 'fields': fields }
        data = self.__vk_api.method('users.get', params)
        return data[0]

    def send_message(self, peer_id, text=None, attachment=None, params = {}) -> None:

        try:
            message = {'peer_id': peer_id, 'random_id': 0,
                       'message': text, 'attachment': attachment, **params}

            self.__vk_api.method('messages.send', message)

        except Exception as e:
            print('[Exception] VkBotMessanger.send_message', e)

    def removeChatUser(self, peer_id, user_id) -> None:
        try:
            chat_id = peer_id - 2000000000
            data = {'chat_id': chat_id, 'user_id': user_id}
            self.__vk_api.method('messages.removeChatUser', data)
        except Exception as e:
            print('[Exception] VkBotMessanger.removeChatUser', e)

    def delete_message(self, group_id, peer_id, messages_ids, cmids) -> None:
        data = {'group_id': group_id, 'delete_for_all': 1,
                'peer_id': peer_id, 'cmids': cmids}
        self.__vk_api.method('messages.delete', data)


    def batchRemoveChatUsers(self, peer_id, userIds) -> None:
        for user_id in userIds:
            self.removeChatUser(peer_id, user_id)

    def chat_members(self, peer_id) -> None:
        try:
            data = self.__vk_api.method(
                'messages.getConversationMembers', {'peer_id': peer_id})
            
            userIdx = []
            for item in data['items']:
                userIdx.append(item['member_id'])

            return userIdx

        except Exception as e:
            print('[Exception] VkBotMessanger.send_message', e)
