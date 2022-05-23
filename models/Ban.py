from models.Base import Base


class BanModel(Base):

    def __init__(self) -> None:
        Base.__init__(self=self, table_name='bans', primary_key='user_id',
                      schema=self.__schema(), timestamp=True, sync=True)

    def create_ban(self, user_id, reason):
        Base.create(self, ['user_id', 'reason'], [
                    f"'{user_id}'", reason])

    def __schema(self):

        return {
            'user_id': Base.schema_type(type=int, nullable=False),
            'group_id': Base.schema_type(int),
            'reason': Base.schema_type(str),
        }
