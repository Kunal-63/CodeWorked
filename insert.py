import mysql.connector as con
import csv
mydb = con.connect(host="localhost", user="root", password="root", database="airport_school")
cur = mydb.cursor()

f1 =open(r"C:\Users\Admin\Documents\Received Files\book_accession.csv","r")

reader = csv.reader(f1)

for row in reader:
    print(row)
    try:
        cur.execute("insert into book_accession values(%s, %s)", row)
    except:
        pass
mydb.commit()