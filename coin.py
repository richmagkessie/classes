# tossing coins
# github: @richmagkessie
# email: kessierich.mag@gmail.com

# This program simulates coin flip
# simple classes and objects
import random
# class definition
class Coin:
    # the ini function initializes the sideup of the coin to 'heads'
    # the sideup data attribute is public
    def __init__(self):
        self.sideup = 'Heads'

    # method to flip coin
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # method to save the current side of the coin
    def get_side(self):
        return self.sideup

# main function
def main():
    # create an object of the Coin class
    coin = Coin()

    # Toss the coin
    input('Hit the enter key to toss coin ')
    coin.toss()

    # Check fo the side of the coin
    input('Hit the s key to check for the side of the coin ')
    print('The side of the coin after the flip is ', coin.get_side())

# Call the main function
main()
