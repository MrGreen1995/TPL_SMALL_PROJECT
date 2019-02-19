## CITIZEN CLASS ##

class Citizen(object):
    def __init__(self, ssn, name, address):
        self.__ssn = ssn
        self.__name = name
        self.__address = address

    ## getter and setters for citizen ssn
    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, value):
        self.__ssn = value

    ## getter and setters for citizen name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string!!!")
        self.__name = value

    ## getter and setters for citizen address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string!!!")
        self.__address = value
