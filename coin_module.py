# This program uses the coin class by importing it as module
import private

def main():
    # create an object of the Coin class
    coin = private.Coin()

    # Toss the coin
    input('Hit the enter key to toss coin ')
    coin.toss()

    # Check fo the side of the coin
    input('Hit the s key to check for the side of the coin ')
    print('The side of the coin after the flip is ', coin.get_side())

# Call the main function
main()
# Calling the main function
main()
