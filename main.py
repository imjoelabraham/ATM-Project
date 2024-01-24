from art import logo
from authenticator import Authenticator
from atm_operations import ATMOperation
from data_handler import DataHandler

auth = Authenticator()
atm_operation = ATMOperation()
data_handler = DataHandler()

print(logo)

hasnt_exited = True

try:
    while hasnt_exited:
        print("""
        ~~~~~~~~~~~ Hello, Welcome to the ATM ~~~~~~~~~~~~
        
        What would you like to do?
        
        1. Withdraw
        2. Deposit
        3. Change Debit Card pin
        4. Exit
        
        ~~~~~~~~~~ A project by Joel ~~~~~~~~~~
        """)
        user_action = int(input('Type "1" or "2" or "3" or "4" to choose an option you would like to do: '))

        if user_action == 1:
            card_no_input = int(input("Please enter the 16-digit Debit card number: "))
            pin_input = int(input("Please enter your 4-digit PIN: "))

            if atm_operation.withdraw(card_no_input, pin_input):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed.")

        elif user_action == 2:
            acc_no_input = int(input("Please enter the account number: "))
            if atm_operation.deposit(acc_no_input):
                print("Deposit successful.")
            else:
                print("Deposit failed.")

        elif user_action == 3:
            card_no_input = int(input("Please enter the 16-digit Debit card number: "))
            current_pin_input = int(input("Please enter your current 4-digit PIN: "))

            if atm_operation.change_pin(card_no_input, current_pin_input):
                print("PIN change successful.")
            else:
                print("PIN change failed.")

        elif user_action == 4:
            print("Exiting the ATM. Thank you for using our services!")
            data_handler.close_connections()
            hasnt_exited = False

        else:
            print("Invalid choice. Please choose a valid option.")
except Exception as err:
    print(f"An error occurred: {err}")

finally:
    data_handler.close_connections()
