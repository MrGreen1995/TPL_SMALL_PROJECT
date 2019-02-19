## Product Class ##

class Product(object):
    def __init__(self, productCode, name, description, price, points):
        self.__productCode = productCode
        self.__name = name
        self.__description = description
        self.__price = price
        self.__points = points

    @property
    def productCode(self):
        return self.__productCode

    @productCode.setter
    def productCode(self, value):
        self.__productCode = value

    ###
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string!!!")
        self.__name = value

    ###
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string!!!")
        self.__description = value

    ###
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__description = value

    ###
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value
