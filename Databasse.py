import mysql.connector as sql
class myDatabase:
    def _init_(self):
        self.db = sql.connect(
            host="localhost",
            user="root",
            password="root",
            database="Employee"
        )
        self.cursor = self.db.cursor()
        self.createTable()
        
    def createTable(self):
        query = """
            CREATE TABLE IF NOT EXISTS STUDENTS(
                SAP_ID VARCHAR(10) PRIMARY KEY,
                NAME VARCHAR(255),
                ADDRESS VARCHAR(255),
                MARKS INT
            )
        """
        self.cursor.execute(query)
        self.db.commit()
        
    def insertData(self,sapid,name,address,marks):
        query = "INSERT INTO STUDENTS(SAP_ID,NAME,ADDRESS,MARKS) VALUES (%s,%s,%s,%s)"
        values = (sapid,name,address,marks)
        self.cursor.execute(query,values)
        self.db.commit()
        print("Record Inserted successfully")
    
    def modifyMarks(self,sapid,marks):
        query = "UPDATE STUDENTS SET MARKS = %s WHERE SAP_ID = %s"
        values = (marks,sapid)
        self.cursor.execute(query,values)
        self.db.commit()
        print("Record Updated Successfully")
    
    def deleteData(self,sapid):
        query = f"DELETE FROM STUDENTS WHERE SAP_ID = '{sapid}'"
        self.cursor.execute(query)
        self.db.commit()
        print("Record Deleted successfully")
    
    def showData(self):
        self.cursor.execute("SELECT * FROM STUDENTS")
        data = self.cursor.fetchall()
        for e in data:
            print(e)
        
        
studentData = myDatabase()

while(True):
    print("1. Insert Record")
    print("2. Show Record")
    print("3. Modify Record")
    print("4. Delete Record")
    ch = int(input("enter choice : "))
    
    if(ch==1):
        sapid = input("Enter your SAP ID : ")
        name = input("Enter your name : ")
        address = input("Enter your address : ")
        marks = int(input("Enter your marks : "))
        studentData.insertData(sapid, name, address, marks)
    elif(ch==2):
        studentData.showData()
    elif(ch==3):
       sapid = input("Enter your SAP ID : ") 
       marks = int(input("Enter your marks : "))
       studentData.modifyMarks(sapid, marks) 
    elif(ch==4):
       sapid = input("Enter your SAP ID : ") 
       studentData.deleteData(sapid)
    else:
        break