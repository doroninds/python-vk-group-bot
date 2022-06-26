

from vk_api.bot_longpoll import VkBotMessageEvent


class Commander:

    __cmd = ''
    __is_command_set = False
    __is_command = False

    def __init__(self, message_event: VkBotMessageEvent) -> None:
        self.__event = message_event

    @property
    def peer_id(self) -> int:
        return self.__event.message.peer_id

    @property
    def from_id(self) -> int:
        return self.__event.message.from_id

    @property
    def from_reply_id(self) -> int:
        id = None
        if (self.__event.message.get('reply_message') and self.__event.message['reply_message']['from_id']):
            id = self.__event.message['reply_message']['from_id']
        return id

    @property
    def from_reply_or_from_id(self) -> int:
        id = self.from_id
        if (self.from_reply_id):
            id = self.from_reply_id
        return id

    @property
    def random_id(self) -> int:
        return self.__event.message.random_id

    @property
    def args(self):
        return self.__event.message.text.split()

    @property
    def cmd(self) -> str:
        if (self.__cmd):
            return self.__cmd
        if (self.args[0]):
            self.__cmd = str(self.args[0]).lower()
        return self.__cmd

    @property
    def data(self):
        return self.__event.message.text[len(self.cmd):]

    @property
    def line_args(self):
        return self.__event.message.text.split('\n')

    @property
    def value(self):
        return " ".join(self.args[1:])

    @property
    def is_command(self) -> str:
        if (self.__is_command_set == True):
            return self.__is_command

        if (self.__event.message.text and self.__event.message.text[0] == '!'):
            self.__is_command = True

        self.__is_command_set = True

        return self.__is_command

    @property
    def text(self) -> str:
        return self.__event.message.text

    @property
    def attachments(self) -> str:
        return self.__event.message.attachments

    @property
    def get_photo_link(self) -> str:
        if (len(self.attachments)):
            attachment = self.attachments[0]
            if (attachment['type'] == 'photo'):
                photo = attachment['photo']
                link = f"photo{photo['owner_id']}_{photo['id']}_{photo['access_key']}"
                return link
        return None
   
    @property
    def get_photos_links(self) -> str:
        links = ''
        if (len(self.attachments)):

            for attachment in self.attachments:
                if (attachment['type'] == 'photo'):
                    photo = attachment['photo']
                    link = f"photo{photo['owner_id']}_{photo['id']}_{photo['access_key']}"
                    links += link + ','
        return links

    @property
    def conversation_message_id(self) -> int:
        return self.__event.message.conversation_message_id

    @property
    def group_id(self) -> int:
        return self.__event.group_id

    @property
    def message_id(self) -> int:
        return self.__event.message.id

    @cmd.setter
    def cmd(self, val):
        self.__cmd = val

    @is_command.setter
    def is_command(self, val):
        self.__is_command_set = True
        self.__is_command = val
