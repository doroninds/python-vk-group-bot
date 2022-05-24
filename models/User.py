from models.Base import Base


class UserModel(Base):
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
            'birthday': Base.schema_type(str),
            'reputation': Base.schema_type(type=int, default_value=0),
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
         self.create(['user_id', 'username', 'nickname'], [f'{user_id}', f"'{data.get('screen_name')}'", f"'{data.get('nickname')}'"])

    def profile(self, user_id):
        user = self.findbypk(user_id)

        text = f"""
        Это {user.get('nickname') or user.get('user_id')}
Должность: {user.get('role')}
В отношениях с [ник] (время отношений)

Репутация: ✨{user.get('reputation')}
Первое появление: {user.get('created_at')} (сколько времени прошло)

О СЕБЕ:
{user.get('bio')}

НАГРАДЫ:
🎗 [награда]
🎗 [награда] 
        """

        return text
