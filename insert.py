import mysql.connector as con
import csv
mydb = con.connect(host="localhost", user="root", password="root", database="airport_school")
cur = mydb.cursor()

f1 =open("std_fees.csv","r")

reader = csv.reader(f1)

for row in reader:
    cur.execute("insert into std_fees values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
mydb.commit()