import mysql.connector as con
import csv 

mydb = con.connect(host="localhost", user="root", passwd="root", database="airport_school_new")
cursor = mydb.cursor()

with open(r"D:\ZETA CORE 2023-24\BACKUP\gr_details.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cursor.execute("insert into gr_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
        mydb.commit()

