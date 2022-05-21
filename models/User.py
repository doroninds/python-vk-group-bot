from models.Base import Base


class UserModel(Base):
    __primary_key = 'id'

    def __schema() -> object:
        return {
           "group_id": int,
            "id": int,
            "level": int,
            "editor": bool,
            "moderator": bool,
        }
    def __init__(self) -> None:
        Base.__init__(self, 'users', self.__primary_key)

    def find_admins(self):
  
        users = Base.findall(self, [{ 'field': 'level', 'operator': '>', 'value': '0'}])
        text = ''
        for user in users:
            text += f"{user.get('role')}: {user.get('nickname')}\n"
        return text
