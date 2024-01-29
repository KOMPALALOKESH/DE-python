from datetime import datetime
from dateutil.relativedelta import relativedelta

class User:
    def __init__(self, name, date_of_birth):
        self.__name = name
        self.__date_of_birth = datetime.strptime(date_of_birth, "%Y-%M-%d")

    def get_age(self):
        age = relativedelta(datetime.today(), self.__date_of_birth).years
        return f'{self.__name}, your age is {age}.'
