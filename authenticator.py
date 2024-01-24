from data_handler import DataHandler


class Authenticator:
    def __init__(self):
        self.data_handler = DataHandler()

    def authenticate(self, card_no, pin):
        """Authenticate card number and PIN."""
        customer_data = self.data_handler.fetch_data(card_no)
        if customer_data and customer_data[0][6] == pin:
            return True
        else:
            print("Invalid card number or PIN.")
            return False

    def fetch_balance(self, user_no):
        """Fetch account balance based on the card number."""
        customer_data = self.data_handler.fetch_data(user_no)
        if customer_data:
            return customer_data[0][7]
        else:
            print("Invalid card number.")
            return None

    def update_balance(self, acc_no, new_balance):
        """Update account balance based on the card number."""
        try:
            previous_balance = self.fetch_balance(acc_no)
            self.data_handler.update_balance_query(acc_no, new_balance)
            total_balance = self.fetch_balance(acc_no)

            print(f"Previous Balance: {previous_balance}")
            print("Balance updated successfully.")
            print(f"Total Balance: {total_balance}")
        except Exception as err:
            print(f"Failed to update balance: {err}")

    def get_account_info(self, acc_no):
        """Get account information based on the account number."""
        account_info = self.data_handler.fetch_account_info(acc_no)
        return account_info

    def change_pin(self, card_no, new_pin):
        """Change PIN for the given card number."""
        try:
            self.data_handler.change_pin_query(card_no, new_pin)
            print("PIN changed successfully.")
        except Exception as err:
            print(f"Failed to change PIN: {err}")
