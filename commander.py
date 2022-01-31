

from vk_api.bot_longpoll import VkBotMessageEvent

class Commander:
    def __init__(self, message_event: VkBotMessageEvent) -> None:
        self.__event = message_event
        # self.__bot_messsager = bot_messsager
        # self.__reply_from_id = bot_messsage.reply_from_id
        # self.__args = bot_messsage.text.split()
        # self.__cmd = self.__args[0]
        # self.__content_key = " ".join(self.__args[1:])
        # self.__segments = bot_messsage.text.split("\n")
        # self.__payload = "\n".join(self.__segments[1:])

    @property
    def peer_id(self) -> int:
      return self.__event.message.peer_id

    @property
    def from_id(self) -> int:
      return self.__event.message.from_id

    @property
    def from_reply_id(self) -> int:
      id = self.from_id
      print('self.__event.message', self.__event.message)
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
        return self.args[0].lower()

    @property
    def data(self):
        return self.__event.message.text[len(self.cmd):]

    @property
    def value(self):
        return " ".join(self.args[1:])

    @property
    def is_command(self) -> str:
      return self.cmd[0] == '!'
