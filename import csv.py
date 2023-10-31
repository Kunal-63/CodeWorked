import csv
import mysql.connector as con
mydb = con.connect(host="localhost",user="root",password="Mouse@2010",database="airport_school1")
cur = mydb.cursor()
f1 = open(r"C:\Users\SERVER\Downloads\OTHER_DETAIL.csv","r")
data = csv.reader(f1)
for i in data:
    cur.execute("insert into OTHER_DETAIL values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",i)
    mydb.commit()