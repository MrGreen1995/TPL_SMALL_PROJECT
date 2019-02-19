## Created by ODILJON MARDONOV ##
## Store class definition ##
from StoreChain import StoreChain


class Store(StoreChain):
    def __init__(self, id, telephone, name, address):
        self.__id = id
        self.__telephone = telephone
        super().__init__(name, address)

    ## getter and setters for store id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    ## getter and setters for store telephone
    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, value):
        self.__telephone = value

    # def display(self):
    #     print('VALUES ', self.__id, self.__telephone, self.name, self.address)








