# This program creates the bankAccount class
# github: @richmagkessie
# email: kessierich.mag@gmail.com

#class def
class BackAccount:
    def __init__(self, balance):
        self.__balance = balance

    # deposit method
    def deposit(self, amount):
        self.__balance += amount

    # withdraw method
    def withdraw(self, amount):
        if __balance >= amount:
            self.__balance -+ amount
        else:
            print('Error: Insufficient funds.')

    # get the balance
    def get_balance(self):
        return self.__balance
