## Customer class ##
from Citizen import Citizen


class Customer(Citizen):
    def __init__(self, id, purchasing_points, telephone, membership, ssn, name, address):
        self.__id = id
        self.__purchasingPoints = purchasing_points
        self.__telephone = telephone
        self.__membership = membership ###tis should be a list
        super().__init__(ssn, name, address)


    ## getter and setter for id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    ## getter and setter for purchasingPoints
    @property
    def purchasingPoints(self):
        return self.__purchasingPoints

    ####
    @purchasingPoints.setter
    def purchasingPoints(self, value):
        self.__purchasingPoints = value

    ## getter and setter for telephone
    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, value):
        self.__telephone = value

    ## getter and setter for membership ???
    @property
    def membership(self):
        return self.__membership

    @membership.setter
    def membership(self, value):
        self.__membership = value


