import mysql.connector as con
import csv

mydb = con.connect(host="localhost",user="root",password="root",database="airport_school")
cur = mydb.cursor()

f = open('VIDEOS/book_accession.csv','r')
data = csv.reader(f)

for i in data:
    try: 
        i[0] = int(i[0])
        i[-1] = int(i[-1])
        cur.execute("insert into book_accession values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",i)
        mydb.commit()
    except:
        pass

