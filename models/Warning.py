from datetime import datetime
from datetime import datetime
from models.Base import Base
import time


class WarningModel(Base):
    __primary_key = 'user_id'
    __table_name = 'warnings'

    __expired_by = 7 * 24 * 60 * 60  # days * hours * minutes * seconds

    def __init__(self) -> None:
        Base.__init__(self, self.__table_name, self.__primary_key)

    def create_warn(self, user_id, reason):
        Base.create(self, ['user_id', 'reason', 'expired_at'], [
                    f"'{user_id}'", reason, f"'{self.__default_expiredat()}'"])

    def delete_warn(self, user_id):
        sql = f"DELETE FROM {self.__table_name} WHERE user_id = {user_id} and created_at = (SELECT max(created_at) FROM {self.__table_name} WHERE user_id = {user_id});"
        Base.query(self, sql)

    def __default_expiredat(self):
        tmp = int(time.time() + self.__expired_by)
        date =  datetime.utcfromtimestamp(tmp)
        return f'{date}'

    def __current_datetime(self):
        tmp = int(time.time())
        date =  datetime.utcfromtimestamp(tmp)
        return f'{date}'

    def find_user_warn(self, user_id):
  
        warns = Base.findall(self, [{'field': 'user_id', 'value': user_id }, { 'field': 'expired_at', 'operator': '>', 'value': f"{self.__current_datetime()}"}])
        text = ''
        i = 1
        for warn in warns:
            text += f"Предупреждение #{i}\nПричина: {warn.get('reason')}\nДата: {warn.get('created_at')} GMT+0\nИстекает: {warn.get('expired_at')} GMT+0\n"
            i += 1
        return text
