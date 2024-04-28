# Imporitng Connectors for Connecting Python MySQL Database
import mysql.connector as connector

# Class Name
class DataBaseConnector:
    # Constructor Method
    def __init__(self):
        self.mydb = connector.connect(
            host="localhost", user="root", password="Sk@tc#*2", database="python_test")
        query = 'CREATE TABLE IF NOT EXISTS customers(userid INT PRIMARY KEY, username VARCHAR(200), phone VARCHAR(12))'
        myCursor = self.mydb.cursor()
        myCursor.execute(query)
        # print("\"user_table\" Created in \"python_test\" Database")

    # Insert Method
    def insert_data(self, userid, username, phone):
        query = "INSERT INTO customers(userid, username, phone) VALUES({}, '{}', '{}')".format(
            userid, username, phone)
        print(query)
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()  # Commit only on with connections
        print("User Data Are Saved In Database.")

    # Fetching All Data In Database
    def fetch_data(self):
        query = "SELECT * FROM customers"
        fcur = self.mydb.cursor()
        fcur.execute(query)
        for row in fcur:
            print("User ID:", row[0])
            print("User Name:", row[1])
            print("User Phone:", row[2])
            print()

    # Deleting Data from Database (delete method)
    def delete_data(self, user_id):
        query = "DELETE FROM customers WHERE userid={}".format(user_id)
        # print(query)
        dcur = self.mydb.cursor()
        dcur.execute(query)
        self.mydb.commit()  # Data is Parmanently Deleted
        print("User", user_id, "is deleted.")

    # Update data from Database (update method)
    def update_data(self, user_id, new_username, new_phone):
        query = "UPDATE customers SET username='{}', phone='{}' WHERE userid={}".format(
            new_username, new_phone, user_id)
        # print(query)
        ucur = self.mydb.cursor()
        ucur.execute(query)
        self.mydb.commit()
        print("New Data is Update")
