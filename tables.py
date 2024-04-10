import mysql.connector as con
def CreateTables(DatabaseName):
    mydb = con.connect(host="localhost", user="root", passwd="root", database=DatabaseName)
    cur = mydb.cursor()

    cur.execute("create table if not exists academic_detail(gr_no int primary key, name varchar(255),active1 bool,left1 bool,aai1 bool,inactive_date varchar(15),add_date varchar(15),add_year int,add_std varchar(15),curr_date varchar(15),curr_year int,curr_std varchar(15),division varchar(5),roll_no int,inactive_reason varchar(50),left_reason varchar(50),progress varchar(50),presence int,out_of int,lc_book varchar(10),lc_no int,lc_date varchar(15),lc_remark varchar(75),lc_copy varchar(75))")

    cur.execute("create table if not exists bonafide(no int primary key, name varchar(50), father_name varchar(50), surname varchar(50), curr_std varchar(50), curr_year int,gr_no varchar(50),BIRTH_DATE VARCHAR(50),BIRTH_DATE_in_words varchar(50),address1 varchar(50),address2 varchar(50))")

    cur.execute("create table if not exists exmp_fees(std varchar(15),ADMISSION_FEE INT,ICARD INT,APR_JUN_TUTION INT,APR_JUN_ATITVITY INT, LATE_FEES INT,JUL_SEP_TUTION INT,JUL_SEP_ACTIVITY INT,OCT_DEC_TUTION INT,OCT_DEC_ACTIVITY INT,JAN_MAR_TUTION INT,JAN_MAR_ACTIVITY INT,OTHERS1 INT)")

    cur.execute("create table if not exists fee_details(GR_NO INT PRIMARY KEY, c1 varchar(500),c2 varchar(500),c3 varchar(500),c4 varchar(500),c5 varchar(500),c6 varchar(500),c7 varchar(500))")

    cur.execute("create table if not exists fee_tran(RECEIPT_NO INT PRIMARY KEY,c1 bool,c2 bool,c3 bool,c4 bool,c5 bool,c6 bool,c7 bool)")

    cur.execute("create table if not exists gr_check(GR_NO INT PRIMARY KEY,c1 bool,c2 bool,c3 bool,c4 bool,c5 bool,c6 bool,c7 bool)")

    cur.execute("create table if not exists gr_details(GR_NO INT PRIMARY KEY,FORM_NO VARCHAR(700),ENQUIRY_NO VARCHAR(700),UID VARCHAR(700),SURNAME VARCHAR(700),NAME VARCHAR(700),FATHER VARCHAR(700),MOTHER VARCHAR(700),SEX VARCHAR(700),BIRTH_DATE VARCHAR(700),CATEGORY VARCHAR(700),RELIGION VARCHAR(700),BIRTH_PLACE VARCHAR(300),PREVIOUS_SCH VARCHAR(500),CASTE VARCHAR(200),BIRTH_TALUKA VARCHAR(200),SUB_CASTE VARCHAR(200), STATE1 VARCHAR(200), MINORITY BOOL,RTE BOOL)")

    cur.execute("create table if not exists other_detail(gr_no int primary key, name varchar(255),bnk_ac_holder varchar(500),scholar_cat varchar(500),transport varchar(500),bnk_name varchar(500),presch_type varchar(500),blood_grp varchar(500),bnk_ac_name varchar(500),remark varchar(500),bnk_branch varchar(050),student_email varchar(200),ifsc_code varchar(50),mobile_no varchar(50),suid varchar(50),adhar_cardno varchar(50),address1 varchar(200),address2 varchar(200),area varchar(50),city varchar(50),district varchar(50),pincode int,phone_no varchar(500))")

    cur.execute("create table if not exists pending_fee_detail(GR_NO INT PRIMARY KEY, ADMISSION_FEE INT,ICARD INT,APR_JUN_TUTION INT,APR_JUN_ATITVITY INT, LATE_FEES INT,JUL_SEP_TUTION INT,JUL_SEP_ACTIVITY INT,OCT_DEC_TUTION INT,OCT_DEC_ACTIVITY INT,JAN_MAR_TUTION INT,JAN_MAR_ACTIVITY INT,OTHERS INT)")

    cur.execute("create table if not exists std_fees(STD VARCHAR(15),ADMISSION_FEE INT,ICARD INT,APR_JUN_TUTION INT,APR_JUN_ATITVITY INT, LATE_FEES INT,JUL_SEP_TUTION INT,JUL_SEP_ACTIVITY INT,OCT_DEC_TUTION INT,OCT_DEC_ACTIVITY INT,JAN_MAR_TUTION INT,JAN_MAR_ACTIVITY INT,OTHERS1 INT)")

    cur.execute("create table if not exists tran_details(RECEIPT_NO INT PRIMARY KEY,DEPT VARCHAR(20),GR_NO INT,DATE1 VARCHAR(15),NAME VARCHAR(50),RECEIPT_BOOK VARCHAR(20),STD VARCHAR(20),div1 varchar(5),total1 int,late_fees int,exemption_fees int,grand_total int,paymode varchar(20),bank varchar(20),cheque_no varchar(20),cheque_date varchar(20),c1 bool,c2 bool,c3 bool, c4 bool,c5 bool,c6 bool,c7 bool)")
    
    cur.execute("create table if not exists issued(org varchar(200), gr_no int, mobile varchar(200), std varchar(200), roll_no int, name varchar(200), accession_no int primary key, book_name varchar(200), issuse_date varchar(200), issuse_remark varchar(200), return_date varchar(200), penalty_days varchar(200), penalty_rate varchar(200), penalty_amt varchar(200),return_remark varchar(200))")

    cur.execute("create table if not exists issued(org varchar(200), gr_no int , mobile varchar(200), std varchar(200), roll_no int, name varchar(200), accession_no int, book_name varchar(200), issuse_date varchar(200), issuse_remark varchar(200), return_date varchar(200), penalty_days varchar(200), penalty_rate varchar(200), penalty_amt varchar(200),return_remark varchar(200))")

    cur.execute("create table if not exists book_accession(accession_no int primary key, book_number varchar(255),book_title varchar(255), author varchar(255), publisher varchar(255), edition varchar(255), isbn varchar(255), category varchar(255),subject varchar(255), remark varchar(255), price int)")

    mydb.commit()