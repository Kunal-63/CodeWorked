import mysql.connector as con
mydb = con.connect(host="localhost", user="root", passwd="Mouse@2010", database="airport_school")
cur = mydb.cursor()

cur.execute("create table if not exists academic_detail(gr_no int primary key, name varchar(255),active1 bool,left1 bool,aai1 bool,inactive_date varchar(15),add_date varchar(15),add_year int,add_std varchar(15),curr_date varchar(15),curr_year int,curr_std varchar(15),division varchar(5),roll_no int,inactive_reason varchar(50),left_reason varchar(50),progress varchar(50),presence int,out_of int,lc_book varchar(10),lc_no int,lc_date varchar(15),lc_remark varhcar(75),lc_copy varhcar(75))")

