import csv
import mysql.connector

mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="algonquin", database="travel")
mycursor1 = mysqldb.cursor()

class RecordController:

    def __init__(self):
        self.records = []
        self.ids = []

    """
        Read all data from dtatabase and assign to records[]
    """
    def declarationRecords(self):
        query = "SELECT * FROM travelq"
        mycursor1.execute(query)
        self.records = mycursor1.fetchall()

    """
        Read the id column 
    """
    def read_ids(self):
        query = "SELECT ref_number FROM travelq"
        mycursor1.execute(query)
        self.ids = mycursor1.fetchall()

    """
        Read the data from the database
    """
    def read_data(self, ref_no):
        try:
            query = "SELECT * FROM travelq WHERE ref_number = %s"
            mycursor1.execute(query, (ref_no,))
            result = mycursor1.fetchone()
            print(result)
        except Exception as e:
            """
                Print when sql query not works
            """
            print(e)

    """
        Search data from database using multiple columns
    """
    def search_data(self, column1, data1, column2, data2):
        max = 100;
        try:
            query = f"SELECT * FROM travelq WHERE {column1} =%s OR {column2} = %s"
            mycursor1.execute(query, (data1, data2))
            result = mycursor1.fetchall()
            for rs in result[:max]:
                print(rs)
        except Exception as e:
            """
                Print when record is not found
            """
            print(e)

    """
        Display the data 
    """
    def display_records(self, max_records=100):
        try:
            self.declarationRecords()
            for record in self.records[:max_records]:
                print(record)
        except Exception as e:
            print(e)

    """
        Write data into new file
    """
    def write_records(self):
        try:
            with open("C:/Users/Savindya/PycharmProjects/ResearchProject2/travelq_new.csv", 'w', newline='') as file:
                csv_writer = csv.writer(file)
                header = ["ref_number", "disclosure_group", "title_en", "title_fr", "name", "purpose_en", "purpose_fr",
                          "start_date", "end_date", "destination_en", "destination_fr", "airfare", "other_transport",
                          "lodging", "meal", "other_expenses", "total", "additional_comment_en",
                          "additional_comment_fr",
                          "owner_org", "owner_org_title"]
                csv_writer.writerow(header)
                for record in self.records:
                    csv_writer.writerow([getattr(record, field) for field in header])
            print("Data saved to travelq_new.csv")
        except Exception:
            print("Error saving data")

    """
        Create record
    """
    def create_record(self, create_record):
        try:
            insertSql = "INSERT INTO travelq VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor1.execute(insertSql,(create_record[0], create_record[1], create_record[2], create_record[3], create_record[4], create_record[5], create_record[6],
                             create_record[7], create_record[8], create_record[9], create_record[10], create_record[11], create_record[12], create_record[13],
                             create_record[14], create_record[15], create_record[16], create_record[17], create_record[18], create_record[19], create_record[20]) )
            ref_no = create_record[0]
            mysqldb.commit()
            print("Record added successfully")
        except Exception as e:
            print("Error adding data")
        return ref_no


    """
        Edit record
    """
    def edit_record(self, edit_id, edit_record, edit_col):
        try:
            altersql = f"UPDATE travelq SET {edit_col} = %s WHERE ref_number = %s"
            print(altersql)
            mycursor1.execute(altersql, (edit_record, edit_id))
            mysqldb.commit()
            print("Records edit Successfully")
        except Exception as e:
            print("Error editing data")

    """
        Delete record
    """
    def delete_record(self, delete_id):
        mysqldb.commit()
        print("Record delete successfully")



