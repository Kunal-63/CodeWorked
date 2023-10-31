import mysql.connector as con
import csv

mydb = con.connect(host="localhost",user="root",password="Mouse@2010",database="airport_school1")
cur = mydb.cursor()

f1 = open(r"rte1.csv", 'r')

abc = csv.reader(f1)

for i in abc:
    cur.execute("update pending_fee_detail set apr_jun_tution=0,APR_JUN_ATITVITY=0,jul_sep_tution=0,jul_sep_activity=0,oct_dec_tution=0,oct_dec_activity=0,jan_mar_tution=0,jan_mar_activity=0,icard=0 where gr_no={}".format(int(i[0])))
    mydb.commit()