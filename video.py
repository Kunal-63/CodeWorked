# import mysql.connector as con
# import csv
# mydb = con.connect(host="localhost", user="root", passwd="root", database="airport_school")
# cur = mydb.cursor()
# cur.execute("show tables")
# tables = cur.fetchall()
# for i in tables:
#     cur.execute(f"select * from {i[0]}")
#     f = open(f'DATA/{i[0]}.csv','w',newline='\n')
#     writer1 = csv.writer(f)
#     writer1.writerows(cur.fetchall())
#     f.close()
# mydb.close()


import mysql.connector as con
import csv
mydb = con.connect(host="localhost", user="root", passwd="root", database="airport_school_new")
cur = mydb.cursor()
