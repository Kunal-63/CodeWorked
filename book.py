import csv
import mysql.connector as con
mydb = con.connect(host="localhost",user="root",password="Mouse@2010",database="airport_school1")
cur = mydb.cursor()

f1 = open(r"C:\Users\Kunal Adwani\OneDrive\Desktop\accession.csv","r")
reader = csv.reader(f1)
for i in reader:
    cur.execute("insert into book_accession values(%s, %s)",i)
    mydb.commit()
f1.close()
