## Store Chain class ##

class StoreChain(object):
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

## getter and setters for store chain name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string!!!")
        self.__name = value

## getter and setters for store chain address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string!!!")
        self.__address = value

    # def showInfoTest(self):
    #     print('Name ', self.__name)
    #     print('Address ', self.__address)
