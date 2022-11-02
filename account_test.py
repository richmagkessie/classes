# importing the account class as module
import account

# main function
def main():
    # Get the starting balance
    start_balance = float(input('Enter your starting balance '))

    # create instance of bankAccount
    account1 = account.BankAccount(start_balance)

    # Deposit customer's paycheck
    payment_received = float(input('How are you depositing today '))
    account1.deposit(payment_received)

    # Display balance
    print('Amount after deposit is $', format(account1.get_balance(), ',.2f'), sep='')

    # Get withdrawal note
    check = input('Do you wish to make a withdrawal? Enter y for Yes or n for No: ')
    if check == 'y' or check == 'Y':
        withdrawal_amount = float(input('How much is your withdrawal amount: '))
        account1.withdraw(withdrawal_amount)
    else:
        print('Your balance is $', account1.get_balance())


# call main function
main()
