from authenticator import Authenticator


class ATMOperation:

    def __init__(self):
        self.auth = Authenticator()

    def withdraw(self, card_no, pin):
        """Withdraw functionality"""
        if self.auth.authenticate(card_no, pin):
            balance = self.auth.fetch_balance(card_no)
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= balance - 10000:
                remaining_balance = balance - amount
                self.auth.update_balance(card_no, remaining_balance)
                return True
            else:
                print("Insufficient balance.")
        return False

    def deposit(self, acc_no):
        """Deposit functionality"""
        acc_info = self.auth.get_account_info(acc_no)
        if acc_info:
            denomination_500 = int(input("Enter the number of 500 Rs notes to deposit: ")) * 500
            denomination_200 = int(input("Enter the number of 200 Rs notes to deposit: ")) * 200
            denomination_100 = int(input("Enter the number of 100 Rs notes to deposit: ")) * 100
            denomination_50 = int(input("Enter the number of 50 Rs notes to deposit: ")) * 50

            deposit_amount = denomination_500 + denomination_200 + denomination_100 + denomination_50
            self.auth.update_balance(acc_no, acc_info["balance"] + deposit_amount)
            return True
        else:
            print("Account not found.")
            return False

    def change_pin(self, card_no, current_pin):
        """Change PIN functionality"""
        if self.auth.authenticate(card_no, current_pin):
            new_pin = input("Enter your new 4 digit PIN: ")
            self.auth.change_pin(card_no, new_pin)
            print("PIN changed successfully.")
            return True
        else:
            print("Invalid PIN.")
            return False
