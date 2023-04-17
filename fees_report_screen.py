from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox
import mysql.connector as con
import csv

mydb = con.connect(host="localhost",user="root",password="Mouse@2010",database="airport_school")
cur = mydb.cursor()



root = Tk()


MENU_FRAME=Frame(root,relief=RIDGE,bg="lightgrey",height=100,width=1550,borderwidth=5)
MENU_FRAME.place(x=0,y=0)

#---------------------------------------------------------------------------------------------------------

MENU_FRAME2=Frame(root,relief=RIDGE,bg="lightgrey",height=700,width=100,borderwidth=1)
MENU_FRAME2.place(x=0,y=100)


#---------------------------------------------------------------------------------------------------------


MAIN_FRAME=Frame(root,relief=RIDGE,bg="white",height=600,width=1320,borderwidth=4,background="lightpink") 
MAIN_FRAME.place(x=150,y=150)



RadioVar2 = IntVar()

Pending = Radiobutton(MAIN_FRAME, text = "Pending", variable = RadioVar2, value=1, height=2,font=('Arial', 30),bg="lightpink",activebackground='lightpink')
Paid = Radiobutton(MAIN_FRAME, text = "Paid", variable = RadioVar2, value=2, height=2,font=('Arial', 30),bg="lightpink",activebackground='lightpink')


Pending.place(x=100,y=150)
Paid.place(x=100,y=250)



wrapper2=Frame(MAIN_FRAME,bg="lightpink",height=500,width=350,relief=RIDGE,borderwidth=2)
wrapper2.place(x=500,y=70)


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()

C1 = Checkbutton(wrapper2, text = "APR JUN FEES", variable = CheckVar1,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C2 = Checkbutton(wrapper2, text = "JUL SEP FEES", variable = CheckVar2,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C3 = Checkbutton(wrapper2, text = "OCT DEC FEES", variable = CheckVar3,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C4 = Checkbutton(wrapper2, text = "JAN MAR FEES", variable = CheckVar4,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C5 = Checkbutton(wrapper2, text = "OTHERS", variable = CheckVar5,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C6 = Checkbutton(wrapper2, text = "ADMISSION", variable = CheckVar6,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C7 = Checkbutton(wrapper2, text = "ICARD", variable = CheckVar7,onvalue = 1, offvalue = 0, height=2,font=('Arial', 20),bg="lightpink",activebackground='lightpink')
C8 = Checkbutton(wrapper2, text = "LATE FEES", variable = CheckVar8, onvalue = 1 , offvalue = 0, height=2, font=('Arial',20),bg="lightpink",activebackground='lightpink')

C1.place(x=0,y=0)
C2.place(x=0,y=70)
C3.place(x=0,y=140)
C4.place(x=0,y=210)
C5.place(x=0,y=280)
C6.place(x=0,y=350)
C7.place(x=0,y=420)
C8.place(x=0,y=490)
pending_lst = []
paid_lst = []
def pending_paid_report():
    cur.execute("select * from gr_check")
    gr_check = cur.fetchall()
    if(RadioVar2.get() == 1):
        pending_lst.append(CheckVar1.get())
        pending_lst.append(CheckVar2.get())
        pending_lst.append(CheckVar3.get())
        pending_lst.append(CheckVar4.get())
        pending_lst.append(CheckVar5.get())
        pending_lst.append(CheckVar6.get())
        pending_lst.append(CheckVar7.get())
        pending_lst.append(CheckVar8.get())
        f1 = open("pending_report.csv", "w",newline="\n")
        writer1 = csv.writer(f1)
        for i in gr_check:
            print(i)
        data = []
        data.append(i[0])
        if(pending_lst[0] == 1):
            if(i[1] == 0):
                data.append(i[1])
        if(pending_lst[1] == 1):
            if(i[2] == 0):
                data.append(i[2])
        if(pending_lst[2] == 1):
            if(i[3] == 0):
                data.append(i[3])
        if(pending_lst[3] == 1):
            if(i[4] == 0):
                data.append(i[4])
        if(pending_lst[4] == 1):
            if(i[5] == 0):
                data.append(i[5])
        if(pending_lst[5] == 1):
            if(i[6] == 0):
                data.append(i[6])
        writer1.writerow(data)
        
    if(RadioVar2.get() == 2):
        paid_lst.append(CheckVar1.get())
        paid_lst.append(CheckVar2.get())
        paid_lst.append(CheckVar3.get())
        paid_lst.append(CheckVar4.get())
        paid_lst.append(CheckVar5.get())
        paid_lst.append(CheckVar6.get())
        paid_lst.append(CheckVar7.get())
        paid_lst.append(CheckVar8.get())
        f1 = open("paid_report.csv", "w",newline="\n")
        writer1 = csv.writer(f1)
        for i in gr_check:
            print(i)
            data = []
            data.append(i[0])
            if(paid_lst[0] == 1):
                if(i[1] == 1):
                    data.append(i[1])
            if(paid_lst[1] == 1):
                if(i[2] == 1):
                    data.append(i[2])
            if(paid_lst[2] == 1):
                if(i[3] == 1):
                    data.append(i[3])
            if(paid_lst[3] == 1):
                if(i[4] == 1):
                    data.append(i[4])
            if(paid_lst[4] == 1):
                if(i[5] == 1):
                    data.append(i[5])
            if(paid_lst[5] == 1):
                if(i[6] == 1):
                    data.append(i[6])
            writer1.writerow(data)
            
        
        
        


    



SAVE_BTN=Button(MAIN_FRAME,text="SUBMIT",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=pending_paid_report)
SAVE_BTN.place(x=1050,y=500)

root.mainloop()