import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="airport_school_new")
cur = mydb.cursor()

cur.execute("SELECT * FROM std_fees")
std_fees = cur.fetchall()

cur.execute("select gr_no,curr_std from academic_detail")
academic_detail = cur.fetchall()

for i in academic_detail:
    gr_no = i[0]
    curr_std = i[1]
    for j in std_fees:
        if curr_std == j[0]:
            cur.execute("update pending_fee_detail set ICARD=%s, APR_JUN_TUTION=%s, APR_JUN_ATITVITY=%s, JUL_SEP_TUTION=%s, JUL_SEP_ACTIVITY=%s, OCT_DEC_TUTION=%s,OCT_DEC_ACTIVITY=%s, JAN_MAR_TUTION=%s, JAN_MAR_ACTIVITY=%s where gr_no = %s",(j[2],j[3],j[4],j[6],j[7],j[8],j[9],j[10],j[11],gr_no))
            mydb.commit()
            break
        else:
            continue
    else:
        print("No such standard fees found for",curr_std)
        continue


    
