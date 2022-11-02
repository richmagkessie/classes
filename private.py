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
# def main():
#     # create an object of the Coin class
#     coin = Coin()
#
#     # Toss the coin
#     input('Hit the enter key to toss coin ')
#     coin.toss()
#
#     # Check fo the side of the coin
#     input('Hit the s key to check for the side of the coin ')
#     print('The side of the coin after the flip is ', coin.get_side())
#
# # Call the main function
# main()
