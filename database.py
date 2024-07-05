import mysql.connector    

mydatabase = mysql.connector.connect(host='localhost',user='root',password='',database='covid_19')

cursor = mydatabase.cursor(buffered=True)

print("Succesfully connected ")

def admin_login(check):
    try:
        cursor.execute("Select * from admin where username = %s and password = %s",check)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
    