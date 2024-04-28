from data_base_connector import DataBaseConnector

def main():

    # Class Objects
    DB_Connect = DataBaseConnector()

    while True:
        print("\n_*_*_*_*_*_*_WELCOM_*_*_*_*_*_*_\n")
        print("Press 1 to Insert new User Data.")
        print("Press 2 to Display all Records.")
        print("Press 3 to Delete Specific User Data.")
        print("Press 4 to Update Exiting User Data.")
        print("Press 5 to Exit the Program.")
        try:
            choice = int(input())
            if (choice == 1):
                # Inserting New Data
                uid = int(input("Enter user id: "))
                user_name = input("Enter user name: ")
                phone_number = input("Enter phone number: ")
                DB_Connect.insert_data(uid, user_name, phone_number)
            elif choice == 2:
                # Display all Records
                DB_Connect.fetch_data()
            elif choice == 3:
                # Delete User Data
                u_id = int(
                    input("Enter the user id which you want to delete: "))
                DB_Connect.delete_data(u_id)
            elif choice == 4:
                # Update Existing User Data
                uid = int(input("Enter the id of user: "))
                new_user_name = input("Enter new user name: ")
                new_phone_num = input("Enter new phone number: ")
                DB_Connect.update_data(uid, new_user_name, new_phone_num)
            elif choice == 5:
                break
            else:
                print("Invalid Number You Entered!, Pleas try Again..")
        except Exception as e:
            print(e)
            print("Invalid Details! Try again.")


if __name__ == "__main__":
    main()
