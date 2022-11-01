# This program uses private variable
import random
class Coin:
    # The init method
    def __init__(self):
        # private sideup
        self.__sideup = 'Heads'

    # the toss method
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # the getside method
    def get_side(self):
        return self.__sideup
# main function
def main():
    # creating an instance of the class
    my_coin = Coin()

    # tossing the object coin
    my_coin.toss()

    # getting the state of the coin
    my_coin.get_side()

# Calling the main function
main()
