from helpers import days_from_datetime
from models.Base import Base

class RewardModel(Base):
    __table_name = 'rewards'
    def __init__(self) -> None:
        Base.__init__(self=self, table_name=self.__table_name, primary_key='user_id',
                      schema=self.__schema(), timestamp=True, sync=True)

    def remove_reward(self, user_id, name):
        sql = f"DELETE FROM {self.__table_name} WHERE user_id = {user_id} and name = '{name}';"
        Base.query(self, sql)

    def add_reward(self, user_id, name):
        Base.create(self, ['user_id', 'name'], [
                    f"'{user_id}'", f"'{name}'"])

    def user_rewards(self, user_id, nickname):

        rows = self.findall([{ 'field': 'user_id', 'value': user_id }])
        text = f'🏆 Награды {nickname}:\n'

        for row in rows:
          
            days = days_from_datetime(row.get('created_at'))
            text += '🎗 %(name)s' % row + f': {days} дня \n'
        return text

    def __schema(self):

        return {
            'user_id': Base.schema_type(type=int, nullable=False),
            'group_id': Base.schema_type(int),
            'name': Base.schema_type(str),
        }
