from models.Base import Base

class BanModel(Base):
    __primary_key = 'user_id'
    __table_name = 'bans'

    def __init__(self) -> None:
        Base.__init__(self, self.__table_name, self.__primary_key)

    def create_ban(self, user_id, reason):
        Base.create(self, ['user_id', 'reason'], [
                    f"'{user_id}'", reason])
