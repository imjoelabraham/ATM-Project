import mysql.connector


class DataHandler:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='yoHackM3',
                port='3306',
                database='atmproject',
            )
            self.cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print(f"Database Connection Error: {err}")

    def fetch_data(self, user_no):
        try:
            self.cursor.execute(f'SELECT * FROM customer_data where acc_no = {user_no} OR card_no '
                                f'= {user_no}')
            data = self.cursor.fetchall()
            return data

        except mysql.connector.Error as err:
            print(f"Data Fetch Error: {err}")
            return None

    def fetch_account_info(self, acc_no):
        try:
            self.cursor.execute(f'SELECT * FROM customer_data where acc_no = {acc_no}')
            account_info = self.cursor.fetchall()

            if account_info:
                return {
                    "acc_no": account_info[0][0],
                    "balance": account_info[0][7],
                }
            else:
                return None

        except mysql.connector.Error as err:
            print(f"Account Info Fetch Error: {err}")
            return None

    def update_balance_query(self, user_no, new_balance):
        try:
            update_query = (f'UPDATE customer_data SET balance = {new_balance} where acc_no = {user_no} OR card_no '
                            f'= {user_no}')
            self.cursor.execute(update_query)
            self.conn.commit()

        except mysql.connector.Error as err:
            self.conn.rollback()
            raise err

    def change_pin_query(self, card_no, new_pin):
        try:
            update_query = f'UPDATE customer_data SET pin = {new_pin} where card_no = {card_no}'
            self.cursor.execute(update_query)
            self.conn.commit()

        except mysql.connector.Error as err:
            self.conn.rollback()
            raise err

    def close_connections(self):
        if self.cursor is not None:
            self.cursor.close()

        if self.conn is not None:
            self.conn.close()
