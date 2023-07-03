import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "harsh",
    password = "Rogerharsh89#",
    database = "mydatabase"
)

while True:
    p = int(input("Do You want to Exit (0 to exit)"))
    if (p == 0):
        break
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE if not exists teacher(Name VARCHAR(24), Rollno INT(255), Dept VARCHAR(200));")
    a = input("Enter Name of student(0 to end ) :")
    b = int(input("Enter Roll no :"))
    c = input("Enter Dept of student :")    
    sql = "INSERT INTO teacher (Name , Rollno , Dept) VALUES (%s , %s , %s)"
    val = (a , b , c)
    mycursor.execute(sql , val)
    print("Value inserted !")

