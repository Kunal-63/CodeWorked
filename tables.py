import mysql.connector as con
mydb = con.connect(host="localhost", user="root", passwd="Mouse@2010", database="airport_school1")
cur = mydb.cursor()

cur.execute("create table if not exists academic_detail(gr_no int primary key, name varchar(255),active1 bool,left1 bool,aai1 bool,inactive_date varchar(15),add_date varchar(15),add_year int,add_std varchar(15),curr_date varchar(15),curr_year int,curr_std varchar(15),division varchar(5),roll_no int,inactive_reason varchar(50),left_reason varchar(50),progress varchar(50),presence int,out_of int,lc_book varchar(10),lc_no int,lc_date varchar(15),lc_remark varchar(75),lc_copy varchar(75))")

cur.execute("create table if not exists bonafide(no int primary key, name varchar(50), father_name varchar(50), surname varchar(50), curr_std varchar(50), curr_year int,gr_no varchar(50),BIRTH_DATE VARCHAR(50),BIRTH_DATE_in_words varchar(50),address1 varchar(50),address2 varchar(50))")

cur.execute("create table if not exists exmp_fees(std varchar(15),ADMISSION_FEE INT,ICARD INT,APR_JUN_TUTION INT,APR_JUN_ATITVITY INT, LATE_FEES INT,JUL_SEP_TUTION INT,JUL_SEP_ACTIVITY INT,OCT_DEC_TUTION INT,OCT_DEC_ACTIVITY INT,JAN_MAR_TUTION INT,JAN_MAR_ACTIVITY INT,OTHERS1 INT)")

cur.execute("create table if not exists fee_details(GR_NO INT PRIMARY KEY, c1 varchar(50),c2 varchar(50),c3 varchar(50),c4 varchar(50),c5 varchar(50),c6 varchar(50),c7 varchar(50))")

cur.execute("create table if not exists fee_tran(RECEIPT_NO INT PRIMARY KEY,c1 bool,c2 bool,c3 bool,c4 bool,c5 bool,c6 bool,c7 bool)")

cur.execute("create table if not exists gr_check(GR_NO INT PRIMARY KEY,c1 bool,c2 bool,c3 bool,c4 bool,c5 bool,c6 bool,c7 bool)")

cur.execute("create table if not exists gr_details(GR_NO INT PRIMARY KEY,FORM_NO VARCHAR(20),ENQUIRY_NO VARCHAR(20),UID VARCHAR(20),SURNAME VARCHAR(20),NAME VARCHAR(20),FATHER VARCHAR(20),MOTHER VARCHAR(20),SEX VARCHAR(20),BIRTH_DATE VARCHAR(20),CATEGORY VARCHAR(20),RELIGION VARCHAR(20),BIRTH_PLACE VARCHAR(30),PREVIOUS_SCH VARCHAR(50),CASTE VARCHAR(20),BIRTH_TALUKA VARCHAR(20),SUB_CASTE VARCHAR(20), STATE1 VARCHAR(20), MINORITY BOOL,RTE BOOL)")

cur.execute("create table if not exists other_detail(gr_no int primary key, name varchar(255),bnk_ac_holder varchar(50),scholar_cat varchar(50),transport varchar(50),bnk_name varchar(50),presch_type varchar(50),blood_grp varchar(50),bnk_ac_name varchar(50),remark varchar(50),bnk_branch varchar(50),student_email varchar(200),ifsc_code varchar(50),mobile_no varchar(50),suid varchar(50),adhar_cardno varchar(50),address1 varchar(200),address2 varchar(200),area varchar(50),city varchar(50),district varchar(50),pincode int,phone_no varchar(500))")

cur.execute("create table if not exists pending_fee_detail(GR_NO INT PRIMARY KEY, ADMISSION_FEE INT,ICARD INT,APR_JUN_TUTION INT,APR_JUN_ATITVITY INT, LATE_FEES INT,JUL_SEP_TUTION INT,JUL_SEP_ACTIVITY INT,OCT_DEC_TUTION INT,OCT_DEC_ACTIVITY INT,JAN_MAR_TUTION INT,JAN_MAR_ACTIVITY INT,OTHERS INT)")

cur.execute("create table if not exists std_fees(STD VARCHAR(15),ADMISSION_FEE INT,ICARD INT,APR_JUN_TUTION INT,APR_JUN_ATITVITY INT, LATE_FEES INT,JUL_SEP_TUTION INT,JUL_SEP_ACTIVITY INT,OCT_DEC_TUTION INT,OCT_DEC_ACTIVITY INT,JAN_MAR_TUTION INT,JAN_MAR_ACTIVITY INT,OTHERS1 INT)")

cur.execute("create table if not exists tran_details(RECEIPT_NO INT PRIMARY KEY,DEPT VARCHAR(20),GR_NO INT,DATE1 VARCHAR(15),NAME VARCHAR(50),RECEIPT_BOOK VARCHAR(20),STD VARCHAR(20),div1 varchar(5),total1 int,late_fees int,exemption_fees int,grand_total int,paymode varchar(20),bank varchar(20),cheque_no varchar(20),cheque_date varchar(20),c1 bool,c2 bool,c3 bool, c4 bool,c5 bool,c6 bool,c7 bool)")

mydb.commit()