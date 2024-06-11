from ast import Delete
# from distutils.cmd import Command
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox
import mysql.connector as con
from PIL import Image,ImageTk
# from playsound import playsound
# from gtts import gTTS
# from tkVideoPlayer import TkinterVideo
import csv
import time
from tkhtmlview import HTMLLabel
import webbrowser


root=Tk()
root.state('zoomed')
mydb = con.connect(host="localhost",user="root",password="root",database="airport_school_new", autocommit=False)
cur = mydb.cursor()

def pending_paid_report():

    RadioVar2 = IntVar()

    Pending = Radiobutton(root, text = "Pending", variable = RadioVar2, value=0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    Paid = Radiobutton(root, text = "Paid", variable = RadioVar2, value=1, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')


    Pending.place(x=100,y=150)
    Paid.place(x=100,y=200)


    wrapper2=Frame(root,bg="lightpink",height=500 ,width=270,relief=RIDGE,borderwidth=2)
    wrapper2.place(x=300,y=30)


    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()

    

    C1 = Checkbutton(wrapper2, text = "APR JUN FEES", variable = CheckVar1,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C2 = Checkbutton(wrapper2, text = "JUL SEP FEES", variable = CheckVar2,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C3 = Checkbutton(wrapper2, text = "OCT DEC FEES", variable = CheckVar3,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C4 = Checkbutton(wrapper2, text = "JAN MAR FEES", variable = CheckVar4,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C5 = Checkbutton(wrapper2, text = "OTHERS", variable = CheckVar5,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C6 = Checkbutton(wrapper2, text = "ADMISSION FEE", variable = CheckVar6,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C7 = Checkbutton(wrapper2, text = "ICARD", variable = CheckVar7,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C8 = Checkbutton(wrapper2, text = "TERM 1", variable = CheckVar8,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C9 = Checkbutton(wrapper2, text = "TERM 2", variable = CheckVar9,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')


    C1.place(x=0,y=0)
    C2.place(x=0,y=45)
    C3.place(x=0,y=90)
    C4.place(x=0,y=135)
    C5.place(x=0,y=180)
    C6.place(x=0,y=225)
    C7.place(x=0,y=270)
    C8.place(x=0,y=315)
    C9.place(x=0,y=360)



    FEES_STD_LABEL=Label(root,text="STD : ",font=('Arial', 13),bg="lightpink")
    FEES_STD_LABEL.place(x=620,y=150)
    std_options = ["-","NUR","JR.KG","SR.KG","1", "2", "3", "4", "5","6","7","8","9","10","12 COMM","12 SCI","11 COMM","11 SCI"]  
    std_var = StringVar()
    std_var.set(std_options[0])  
    FEES_STD_ENTRY = OptionMenu(root, std_var, *std_options)
    FEES_STD_ENTRY.config(font=("Arial", 13))
    FEES_STD_ENTRY.place(x=700,y=150)


    FEES_DIV_LABEL=Label(root,text="DIV : ",font=('Arial', 13),bg="lightpink")
    FEES_DIV_LABEL.place(x=620,y=200)

    div_options = ["-","A", "B", "C", "D"]  
    div_var = StringVar()
    div_var.set(div_options[0])  
    FEES_DIV_ENTRY = OptionMenu(root, div_var, *div_options)
    FEES_DIV_ENTRY.config(font=("Arial", 13))
    FEES_DIV_ENTRY.place(x=700,y=200)



    reciept_num_label=Label(root, text="RECIEPT no :",font=('Orator Std',12, 'bold'), bg='lightpink')
    reciept_num_label.place(x=900, y=150)
    reciept_num_label=Label(root, text=">=",font=('Orator Std',12, 'bold'), bg='lightpink')
    reciept_num_label.place(x=1020, y=150)
    reciept_num_var=IntVar()
    reciept_num_entry=Entry(root,font=('Orator Std',10, 'bold'), textvariable=reciept_num_var, width=10)
    reciept_num_entry.place(x=1050, y=150)


    reciept_num_label2=Label(root, text="<=",font=('Orator Std',12, 'bold'), bg='lightpink')
    reciept_num_label2.place(x=1180, y=150)
    reciept_num_var2=IntVar()
    reciept_num_entry2=Entry(root,font=('Orator Std',10, 'bold'), textvariable=reciept_num_var2, width=10)
    reciept_num_entry2.place(x=1210, y=150)


    date_num_label=Label(root, text="Date no :",font=('Orator Std',12, 'bold'), bg='lightpink')
    date_num_label.place(x=900, y=200)
    date_num_label=Label(root, text=">=",font=('Orator Std',12, 'bold'), bg='lightpink')
    date_num_label.place(x=1020, y=200)
    date_num_entry=DateEntry(root,selectmode="day",date_pattern="dd-mm-y",font=("ariel", 10),width=10)
    date_num_entry.place(x=1050, y=200)


    date_num_label2=Label(root, text="<=",font=('Orator Std',12, 'bold'), bg='lightpink')
    date_num_label2.place(x=1180, y=200)
    date_num_entry2=DateEntry(root,selectmode="day",date_pattern="dd-mm-y",font=("ariel", 10),width=10)
    date_num_entry2.place(x=1210, y=200)

    def bind_radio_buttons():
        Pending.config(command=disable_widgets)
        Paid.config(command=enable_widgets)

    def disable_widgets():
        reciept_num_var.set("")
        reciept_num_entry.config(state="disabled")
        reciept_num_var2.set("")
        reciept_num_entry2.config(state="disabled")
        date_num_entry.config(state="disabled")
        date_num_entry2.config(state="disabled")

    def enable_widgets():
        reciept_num_entry.config(state="normal")
        reciept_num_entry2.config(state="normal")
        date_num_entry.config(state="normal")
        date_num_entry2.config(state="normal")


    def pending_paid_report_submit():
        status = RadioVar2.get()
        fees_criteria = {
            "c1": CheckVar1.get(),
            "c2": CheckVar2.get(),
            "c3": CheckVar3.get(),
            "c4": CheckVar4.get(),
            "c5": CheckVar5.get(),
            "c6": CheckVar6.get(),
            "c7": CheckVar7.get(),
            "C8": CheckVar8.get(),
            "C9": CheckVar9.get()
        }
        std = std_var.get()
        div = div_var.get()
        receipt_from = reciept_num_var.get()
        receipt_to = reciept_num_var2.get()
        date_from = date_num_entry.get_date().strftime('%d-%m-%Y')
        date_to = date_num_entry2.get_date().strftime('%d-%m-%Y')

        query_conditions = []
        if std != "-":
            query_conditions.append(f"STD = '{std}'")
        if div != "-":
            query_conditions.append(f"div1 = '{div}'")
        if receipt_from and receipt_to:
            query_conditions.append(f"RECEIPT_NO BETWEEN {receipt_from} AND {receipt_to}")
        if date_from and date_to:
            query_conditions.append(f"STR_TO_DATE(DATE1, '%d-%m-%Y') BETWEEN STR_TO_DATE('{date_from}', '%d-%m-%Y') AND STR_TO_DATE('{date_to}', '%d-%m-%Y')")

        fees_conditions = []
        for key, value in fees_criteria.items():
            if value == 1:
                fees_conditions.append(f"{key} = {value}")

        # Initialize the query variable
        query = ""
        file_name = ""

        if status == 1:  # Pending report
            file_name = "pending_report.csv"
            query = "SELECT * FROM gr_check WHERE "
            for key, value in fees_criteria.items():
                if value == 1:
                    query += f"{key} = 0 AND "
            query = query[:-5]  # Remove the last "AND"
            disable_widgets()
        elif status == 2:  # Paid report
            file_name = "paid_report.csv"
            query = "SELECT * FROM gr_check WHERE "
            for key, value in fees_criteria.items():
                if value == 1:
                    query += f"{key} = 1 AND "
            query = query[:-5]  # Remove the last "AND"
            enable_widgets()

        if query_conditions:
            query += " AND " + " AND ".join(query_conditions)
        if fees_conditions:
            query += " AND " + " AND ".join(fees_conditions)

        # Print the query and criteria for debugging purposes
        print(f"Status: {'Pending' if status == 1 else 'Paid'}")
        print(f"Standard: {std}")
        print(f"Division: {div}")
        print(f"Receipt Number Range: {receipt_from} - {receipt_to}")
        print(f"Date Range: {date_from} - {date_to}")
        print(f"Fees Criteria: {fees_criteria}")
        print(f"Query Conditions: {query_conditions}")
        print(f"Fees Conditions: {fees_conditions}")
        print(f"Constructed Query: {query}")

    # Call the function to bind the radio buttons
    bind_radio_buttons()

    SAVE_BTN=Button(root,text="SUBMIT",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=pending_paid_report_submit)
    SAVE_BTN.place(x=550,y=650)

pending_paid_report()

root.mainloop()