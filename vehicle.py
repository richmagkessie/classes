# This program demonstrates the Car class
import auto

def main():
    # object of Car class
    car = auto.Car('GWagon', 2029, 4454, 344534, 4)

    # Display the the object's details
    print('Number of doors:', car.get_doors())
    print('Make: ', car.get_make())
    print('Model:', car.get_model())
    print('Price:', car.get_price())

# call the main function
main()
