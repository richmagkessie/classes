# This program explains more about inheritance
# github: @richmagkessie
# email: kessierich.mag@gmail.com

# The automobile class gets and holds the general data
class AutoMobile:
    # the init method accepts arguments for the model, distance, price, make
    def __init__(self, model, make, price, distance):
        self.__model = model
        self.__make = make
        self.__price = price
        self.distance = distance

    # methods to set attributes
    def set_model(self, model):
        self.__model = model

    def set_make(self, make):
        self.__make = make

    def set_price(self, price):
        self.__price = price

    def set_distance(self, distance):
        self.__distance = distance

    # methods to get attributes
    def get_model(self, model):
        return self.__model

    def get_make(self, make):
        return self.__make

    def get_price(self, price):
        return self.__price

    def get_distance(self, distance):
        return self.__distance 
