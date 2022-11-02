# This program holds data about mobile phones
# github: @richmagkessie
# email: kessierich.mag@gmail.com

# phone class definition
class Phone:
    # initializing the attributes
    def __init__(self, manu, price, model_num):
        self.__manufacturer = manu
        self.__retail_price = price
        self.__model_num = model_num

    # method to reset manufacturer
    def set_man(self, manu):
        self.__manufacturer = manu

    # method to reset price
    def set_price(self, price):
        self.__retail_price = price

    # method to reset model_num
    def set_mod(self):
        self.__model_num = model_num

    # method to return manufacturer
    def get_man(self):
        return self.__manufacturer

    # method to return retail_price
    def get_retail(self):
        return self.__retail_price

    # return model_num
    def get_mod(self):
        return self.__model_num
