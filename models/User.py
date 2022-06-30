from datetime import datetime
from helpers import current_datetime
from models.Base import Base


class UserModel(Base):

    add_reputation_words = '+ жиза плюс 👍🏻'
    remove_reputation_words = '- минус осуждаю 👎🏻'

    __table_name = 'users'

    def __init__(self) -> None:
        Base.__init__(self, table_name=self.__table_name, primary_key='user_id',
                      schema=self.__schema(), timestamp=True, sync=True)

    def __schema(self):
        return {
            'user_id': Base.schema_type(type=int, nullable=False),
            'username': Base.schema_type(str),
            'group_id': Base.schema_type(int),
            'level': Base.schema_type(type=int, default_value=0),
            'editor': Base.schema_type(type=bool, default_value=0),
            'moderator': Base.schema_type(type=bool, default_value=0),
            'role': Base.schema_type(str),
            'nickname': Base.schema_type(str),
            'bio': Base.schema_type(str),
            'photo': Base.schema_type(str),
            'birthday': Base.schema_type(str),
            'reputation': Base.schema_type(type=int, default_value=0),
            'total_message': Base.schema_type(type=int, default_value=0),
            'last_message': Base.schema_type('DATETIME'),
        }

    def add_reputation(self, user_id):
        SQL = f'UPDATE {self.__table_name} SET reputation = reputation + 1 WHERE user_id = {user_id}'
        Base.query(self, SQL)

    def remove_reputation(self, user_id):
        SQL = f'UPDATE {self.__table_name} SET reputation = reputation - 1 WHERE user_id = {user_id}'
        Base.query(self, SQL)

    def get_user_ids_map(self):
        rows = self.findall()

        map = {}
        for row in rows:
            map[row.get('user_id')] = row

        return map

    def createByUserInfo(self, user_id, data):
        self.create(['user_id', 'username', 'nickname'], [
                    f'{user_id}', f"'{data.get('screen_name')}'", f"'{data.get('nickname')}'"])

    def update_nickname(self, user_id, nickname):
        user = self.findbypk(user_id)
        social_nickname = f"[id{user.get('user_id')}|{nickname}]"
        self.update([{'field': 'user_id', 'value': user_id }], {'nickname': social_nickname })


    def update_user_messages(self, user_id):
        self.update([{'field': 'user_id', 'value': user_id }], {'last_message': current_datetime()  })
        SQL = f'UPDATE {self.__table_name} SET total_message = total_message + 1 WHERE user_id = {user_id}'
        Base.query(self, SQL)


    def get_user_stats(self, memberIdx):
        rows = self.findall(None, ['total_message', 'DESC'])

        text = 'Статистика беседы (кол-во сообщений):\n'

        rowNum = 1
        for row in rows:
            if (row.get('user_id') in memberIdx):
                text += f"{rowNum}. {row.get('nickname') or row.get('username')}: {row.get('total_message')}\n"
                rowNum += 1
      

       
        return text

    def get_silent_users(self, memberIdx):
        rows = self.findall([{ 'field': 'total_message', 'value': 57 }])

        text = 'Молчуны беседы:\n'

        stat = ''
        rowNum = 1
        for row in rows:
            if (row.get('user_id') in memberIdx):
                stat += f"{rowNum}. {row.get('nickname') or row.get('username')}: Молчит с {row.get('created_at')}\n"
                rowNum += 1

        if (stat):
            return text + stat

        return None