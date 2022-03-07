from models.Base import Base


class UserModel(Base):
    __primary_key = 'id'

    def __init__(self) -> None:
        Base.__init__(self, 'users', self.__primary_key)

