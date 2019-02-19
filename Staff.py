## Staff class ##
from Citizen import Citizen


class Staff(Citizen):
    def __init__(self, jobId, jobTitle, salary, ssn, name, address):
        self.__jobId = jobId
        self.__jobTitle = jobTitle
        self.__salary = salary
        super().__init__(ssn, name, address)


    @property
    def jobId(self):
        return self.__jobId

    @jobId.setter
    def jobId(self, value):
        self.__jobId = value

    @property
    def jobTitle(self):
        return self.__jobTitle

    @jobTitle.setter
    def jobTitle(self, value):
        self.__jobTitle=value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        self.__salary = value
