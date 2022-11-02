# This is my main function
import phones

import phones

# main function
def main():
    # get a list of cellphone objects
    phones = phone_lists()

    # display data in the phone list
    print('Data you entered: ')
    show_list(phones)

# list func
def phone_lists():
    # Empty lists []
    cell_list = []

    # Number of phones to add to list
    num_cells = int(input('Enter the number of cellphones you wish to add to list '))
    print('Enter data for cellphones')
    for phone in range(1, num_cells+1):
        print(f'For phone {phone} ')
        print('---------------')
        manu = input('Enter the manufacturer: ')
        price = float(input('Enter the price: '))
        mod = input('Enter the model number: ')
        print()

        # create an object of Phone
        phone = phones.Phone(manu, price, mod)

        # Add object to list
        cell_list.append(phone)

    # return list of phones add to list
    return cell_list

# This function displays the information for each phone in the list
def show_list(cell_list):
    for item in cell_list:
        print(item.get_man())
        print(item.get_retail())
        print(item.get_mod())
        print()


# call the main function
main()
