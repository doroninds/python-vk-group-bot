

from vk_api.bot_longpoll import VkBotMessageEvent

class Commander:
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
      id = self.from_id
      if (self.__event.message.get('reply_message') and self.__event.message['reply_message']['from_id']):
          id = self.__event.message['reply_message']['from_id']
      return id

    @property
    def random_id(self) -> int:
      return self.__event.message.random_id

    @property
    def args(self):
        return self.__event.message.text.split()

    @property
    def cmd(self) -> str:
        if (self.args[0]):
          return str(self.args[0]).lower()
        else:
          return ''
       

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
      if (not self.__event.message.text):
        return False

      if (self.__event.message.text[0] != '!'):
        return False

      return True

    @property
    def text(self) -> str:
      return self.__event.message.text

    @property
    def attachments(self) -> str:
      return self.__event.message.attachments

    @property
    def conversation_message_id(self) -> int:
      return self.__event.message.conversation_message_id

    @property
    def group_id(self) -> int:
      return self.__event.group_id

    @property
    def message_id(self) -> int:
      return self.__event.message.id
