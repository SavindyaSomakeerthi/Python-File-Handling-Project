class RecordView:
    """
        Display menu
    """

    @staticmethod
    def menu_option():
        print("Options:")
        print("1. Display records")
        print("2. Save data to a new file")
        print("3. Create a new record")
        print("4. Edit a record")
        print("5. Delete a record")
        print("6. Search records")
        print("7. Search records from csv")
        print("8. Quit")
        option = input("enter your option: ")

        return option

    def choose_option(recordController, option):
        if option == '1':
            recordController.display_records()
        elif option == '2':
            recordController.write_records()
        elif option == '3':
            add_data = input("Enter the data (command sepearated): ").split(',')
            ref_no = recordController.create_record(add_data)
            recordController.read_data(ref_no)
        elif option == '4':
            index = input("Enter the id of the record that need to edit: ")
            edit_column = input("Enter the column you need to edit: ")
            edit_data = input("Enter the data: ")
            recordController.edit_record(index, edit_data, edit_column)
            recordController.read_data(index)
        elif option == '5':
            index = input("Enter the id of the record that need to delete: ")
            recordController.delete_record(int(index))
            recordController.read_data(index)
        elif option == '6':
            col1= input("What is the column 1: ")
            data1 = input("Enter the value of column 1: ")
            col2 = input("What is the  column 2: ")
            data2 = input("Enter the value of column 2: ")
            recordController.search_data(col1, data1, col2, data2)
        elif option == '7':
            quit()
        else:
            recordController.error_message()

    """
        Display error message
    """
    @staticmethod
    def error_message():
        print("Invalid option!")
