from RecordController import RecordController
from RecordView import RecordView
import mysql.connector
mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="algonquin")
mycursor = mysqldb.cursor()

"""
    Main class
"""
if __name__ == "__main__":
    db_name = "travel"
    print("Chamini Savindya Demuni")  # Print the student name

    """
        Database connection
    """
    if (mysqldb):
        print("Connection successfull")
        mycursor.execute("show databases")
        list = mycursor.fetchall()
        if(db_name,) in list:
            print("database already exists")
        else:
            mycursor.execute("Create database travel")
    else:
        print("Connection unsuccessfull")

    recordController = RecordController()
    while True:
        option = RecordView.menu_option()
        RecordView.choose_option(recordController, option)