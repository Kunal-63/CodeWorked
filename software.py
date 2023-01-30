from ast import Delete
from distutils.cmd import Command
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox
import mysql.connector as con
from PIL import Image,ImageTk
from playsound import playsound
#import pygame
from gtts import gTTS
# import os
# import sys
# import msvcrt
import time
from tkhtmlview import HTMLLabel
import webbrowser

mydb = con.connect(host="localhost",user="root",password="Mouse@2010",database="airport_school")
cur = mydb.cursor()

root=Tk()
root.state('zoomed')
# root.geometry("1500x800")
root.title("ZETA CORE")
photo = PhotoImage(file = r"ICONS\Zeta.png")
root.iconphoto(False, photo)


def GR_FUNCTION():
    MAIN_FRAME.configure(bg="lightblue")
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy()
    # text_Q1="GENERAL REGISTER"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\general register.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\general register.mp3")
    #pygame.mixer.music.play(loops=0)

    MAIN_FRAME_0=Frame(MAIN_FRAME,relief=RIDGE,bg="lightblue",height=550,width=1300,borderwidth=4)
    MAIN_FRAME_0.place(x=5,y=30)


    def gr_details():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()
        
        gr_details_BTN["state"]="active"
        academic_details_BTN["state"]="disabled"
        other_details_BTN["state"]="disabled"

        MAIN_FRAME_0.configure(bg="lightblue")

        photo_frame = Frame(MAIN_FRAME_0,height=155,width=155,borderwidth=4,relief=RIDGE)
        photo_frame.place(x=30,y=20)
        
        details_frame=Frame(MAIN_FRAME_0,height=150,width=1000,bg="lightblue",borderwidth=4,relief=RIDGE)
        details_frame.place(x=220,y=20)

        
        general_details_frame=Frame(MAIN_FRAME_0,height=360,width=800,bg="lightblue",borderwidth=4,relief=RIDGE)
        general_details_frame.place(x=220,y=175)

        gr_lbl=Label(details_frame,text="GR no :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        gr_lbl.place(x=23,y=20)
        gr_var=IntVar()
        gr_ent=Entry(details_frame,textvariable=gr_var)
        gr_ent.place(x=86,y=25)
        cur.execute("select gr_no from gr_details")
        data = cur.fetchall()
        gr_ent.delete(0,END)
        gr_ent.insert(0,int(data[-1][0])+1)


        form_no_lbl=Label(details_frame,text="Form No :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        form_no_lbl.place(x=240,y=20)
        form_no_var=IntVar()
        form_no_ent=Entry(details_frame,textvariable=form_no_var)
        form_no_ent.place(x=316,y=25)            

        enquiry_no_lbl=Label(details_frame,text="Enquiry No :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        enquiry_no_lbl.place(x=470,y=20)
        enquiry_no_var=IntVar()
        enquiry_no_ent=Entry(details_frame,textvariable=enquiry_no_var)
        enquiry_no_ent.place(x=559,y=25) 

        uid_lbl=Label(details_frame,text="UID :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        uid_lbl.place(x=720,y=20)
        uid_var=IntVar()
        uid_ent=Entry(details_frame,textvariable=uid_var)
        uid_ent.place(x=771,y=25) 

        name1_lbl=Label(details_frame,text="Name :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        name1_lbl.place(x=25,y=100)

        surname_lbl=Label(details_frame,text="Surname:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        surname_lbl.place(x=114,y=68)
        surname_var=StringVar()
        surname_ent=Entry(details_frame,text=surname_var)
        surname_ent.place(x=84,y=105)

        name_lbl=Label(details_frame,text="Name:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        name_lbl.place(x=350,y=68)
        name_var=StringVar()
        name_ent=Entry(details_frame,text=name_var)
        name_ent.place(x=314,y=105)

        father_lbl=Label(details_frame,text="Father:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        father_lbl.place(x=590,y=68)
        father_var=StringVar()
        father_ent=Entry(details_frame,text=father_var)
        father_ent.place(x=557,y=105)

        mother_lbl=Label(details_frame,text="Mother:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        mother_lbl.place(x=800,y=68)
        mother_var=StringVar()
        mother_ent=Entry(details_frame,text=mother_var)
        mother_ent.place(x=769,y=105)


        sex_lbl=Label(general_details_frame,text="Sex :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        sex_lbl.place(x=50,y=40)
        sex_var= StringVar()
        sex_combo = ttk.Combobox(general_details_frame,width=20,textvariable = sex_var)
        sex_combo['values'] = ('Male','Female')
        sex_combo.place(x=100,y=45)

        birth_date_lbl=Label(general_details_frame,text="Birth Date :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        birth_date_lbl.place(x=280,y=40)
        birth_date_ent=DateEntry(general_details_frame,selectmode="day",date_pattern="dd-mm-y",width=17)
        birth_date_ent.place(x=370,y=45)

        category_lbl=Label(general_details_frame,text="Category :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        category_lbl.place(x=575,y=40)
        category_var=StringVar()
        category_combo = ttk.Combobox(general_details_frame,width=17,textvariable = category_var)
        category_combo['values'] = ('SEBC','ST','GEN','SC')
        category_combo.place(x=655,y=45)

        religion_lbl=Label(general_details_frame,text="Religion :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        religion_lbl.place(x=24,y=105)
        religion_var=StringVar()
        religion_combo = ttk.Combobox(general_details_frame,width=20,textvariable = religion_var)
        religion_combo['values'] = ('Hindhu','Muslim','Jain','Sikh','Cristian')
        religion_combo.place(x=100,y=110)

        birth_place_lbl=Label(general_details_frame,text="Birth Place :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        birth_place_lbl.place(x=274,y=105)
        birth_place_var=StringVar()
        birth_place_ent=Entry(general_details_frame,text=birth_place_var)
        birth_place_ent.place(x=370,y=110)

        
        previous_school_lbl=Label(general_details_frame,text="Previous School :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        previous_school_lbl.place(x=530,y=105)
        previous_school_var=StringVar()
        previous_school_ent=Entry(general_details_frame,text=previous_school_var)
        previous_school_ent.place(x=655,y=110)

        caste_lbl=Label(general_details_frame,text="Caste :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        caste_lbl.place(x=42,y=170)
        caste_var=StringVar()
        caste_combo = ttk.Combobox(general_details_frame,textvariable = caste_var)
        caste_combo['values'] = ('Hindhu','Muslim','Jain','Sikh','Cristian')
        caste_combo.place(x=100,y=175)

        birth_taluka_lbl=Label(general_details_frame,text="Birth Taluka :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        birth_taluka_lbl.place(x=268,y=170)
        birth_taluka_var=StringVar()
        birth_taluka_ent=Entry(general_details_frame,text=birth_taluka_var)
        birth_taluka_ent.place(x=370,y=175)

        subcaste_lbl=Label(general_details_frame,text="Subcaste :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        subcaste_lbl.place(x=21,y=240)
        subcaste_var=StringVar()
        subcaste_combo = ttk.Combobox(general_details_frame,width=20,textvariable = subcaste_var)
        subcaste_combo['values'] = ('Hindhu','Muslim','Jain','Sikh','Cristian')
        subcaste_combo.place(x=100,y=245)

        state_lbl=Label(general_details_frame,text="State :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        state_lbl.place(x=310,y=240)
        state_var=StringVar()
        state_ent=Entry(general_details_frame,text=state_var)
        state_ent.place(x=370,y=245)

        minorityvalue=IntVar()
        minority_check=Checkbutton(general_details_frame,text="Minority",onvalue=1,offvalue=0,bg="lightblue",activebackground="black")
        minority_check.place(x=100,y=315)

        rtevalue=IntVar()
        rte_check=Checkbutton(general_details_frame,text="RTE",variable=rtevalue,onvalue=1,offvalue=0,bg="lightblue",activebackground="black")
        rte_check.place(x=250,y=315)

        def grsave():
            grlst=[]
            grlst.append(gr_ent.get())
            grlst.append(form_no_ent.get())
            grlst.append(enquiry_no_ent.get())
            grlst.append(uid_ent.get())
            grlst.append(surname_ent.get())
            grlst.append(name_ent.get())
            grlst.append(father_ent.get())
            grlst.append(mother_ent.get())
            grlst.append(sex_combo.get())
            grlst.append(birth_date_ent.get())
            grlst.append(category_combo.get())
            grlst.append(religion_combo.get())
            grlst.append(birth_place_ent.get())
            grlst.append(previous_school_ent.get())
            grlst.append(caste_combo.get())
            grlst.append(birth_taluka_ent.get())
            grlst.append(subcaste_combo.get())            
            grlst.append(state_ent.get())
            grlst.append(minorityvalue.get())
            grlst.append(rtevalue.get())
            cur.execute("insert into gr_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",grlst)
            mydb.commit()
            academic_details()
        save_next_button = Button(MAIN_FRAME_0,text="NEXT",font=("Arial",20),command=grsave)
        save_next_button.place(x=1100,y=470)

    global academic_details
    def academic_details():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()
    
        academic_details_BTN["state"]="active"
        gr_details_BTN["state"]="disabled"
        other_details_BTN["state"]="disabled"



        academic_frame1=Frame(MAIN_FRAME_0,height=541,width=645,bg="lightblue",borderwidth=4,relief=RIDGE)
        academic_frame1.place(x=0,y=0)

        #
        Gr_label = Label(academic_frame1, text="GR NO : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Gr_label.place(x=90, y=10)
        Gr_var=StringVar()
        Gr_entry= Entry(academic_frame1, textvariable=Gr_var, width=20)
        Gr_entry.place(x=150, y=10)
        cur.execute("select gr_no from gr_details")
        data = cur.fetchall()
        Gr_entry.insert(0,data[-1][0]) 

        #
        Name_label = Label(academic_frame1, text="Name : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Name_label.place(x=310, y=10)
        Name_var=StringVar()
        Name_entry=Entry(academic_frame1, textvariable=Name_var, width=20)
        Name_entry.place(x=370,y=10)
  
        activevalue=IntVar()
        active_check=Checkbutton(academic_frame1,text="Active",variable=activevalue,offvalue=0,onvalue=1,activebackground="lightblue",font=("Arieal",10,"bold"),bg="lightblue")
        active_check.place(x=75,y=50)

        leftvalue=IntVar()
        left_check=Checkbutton(academic_frame1,text="Left",variable=leftvalue,offvalue=0,onvalue=1,activebackground="lightblue",font=("Arieal",10,"bold"),bg="lightblue")
        left_check.place(x=200,y=50)

        aaivalue=IntVar()
        aai_check=Checkbutton(academic_frame1,text="AAI",variable=aaivalue,offvalue=0,onvalue=1,activebackground="lightblue",font=("Arieal",10,"bold"),bg="lightblue")
        aai_check.place(x=325,y=50)
        #
        in_active_date_lbl=Label(academic_frame1,text="InActive Date :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        in_active_date_lbl.place(x=50,y=100)
        in_active_date_ent=DateEntry(academic_frame1,selectmode="day",date_pattern="dd-mm-y")
        in_active_date_ent.place(x=160,y=105)
 
        date_lbl=Label(academic_frame1,text="Date",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        date_lbl.place(x=180,y=160)

        year_lbl=Label(academic_frame1,text="Year",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        year_lbl.place(x=280,y=160)

        standard=Label(academic_frame1,text="Standard",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        standard.place(x=370,y=160)

        #
        addmission_lbl=Label(academic_frame1,text="Addmission :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        addmission_lbl.place(x=50,y=200)
        addmission_date_ent=DateEntry(academic_frame1,selectmode="day",date_pattern="dd-mm-y")
        addmission_date_ent.place(x=150,y=205)
        addmission_year_var=IntVar()
        addmission_year_ent=Entry(academic_frame1,textvariable=addmission_year_var,width=10)
        addmission_year_ent.place(x=275,y=205)
        addmission_standard_var=StringVar()
        addmission_standard_ent=ttk.Combobox(academic_frame1,textvariable=addmission_standard_var,width=10)
        addmission_standard_ent['values']=['NUR','JR.KG','SR.KG','1','2','3','4','5','6','7','8','9','10','11 COMM','11 SCI','12 COMM','12 SCI']
        addmission_standard_ent.place(x=370,y=205) 

        current_lbl=Label(academic_frame1,text="Current :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        current_lbl.place(x=75,y=240)
        current_date_ent=DateEntry(academic_frame1,selectmode="day",date_pattern="dd-mm-y")
        current_date_ent.place(x=150,y=245)
        current_year_var=IntVar()
        current_year_ent=Entry(academic_frame1,textvariable=current_year_var,width=10)
        current_year_ent.place(x=275,y=245)
        current_standard_var=StringVar()
        current_standard_ent=ttk.Combobox(academic_frame1,textvariable=current_standard_var,width=10)
        current_standard_ent['values']=['NUR','JR.KG','SR.KG','1','2','3','4','5','6','7','8','9','10','11 COMM','11 SCI','12 COMM','12 SCI']
        current_standard_ent.place(x=370,y=245) 

        division_lbl=Label(academic_frame1,text="Division :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        division_lbl.place(x=75,y=340)
        division_var=StringVar()
        division_ent=ttk.Combobox(academic_frame1,textvariable=division_var,width=8)
        division_ent['values']=['A','B','C','D','E']
        division_ent.place(x=150,y=345)

        roll_no_lbl=Label(academic_frame1,text="Roll No :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        roll_no_lbl.place(x=250,y=340)
        roll_no_var=IntVar()
        roll_no_ent=Entry(academic_frame1 ,textvariable=roll_no_var,width=10)
        roll_no_ent.place(x=320,y=345)

        inactive_reason_lbl=Label(academic_frame1,text="InActive Reason :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        inactive_reason_lbl.place(x=22,y=400)
        inactive_reason_var=StringVar()
        inactive_reason_ent=Entry(academic_frame1,textvariable=inactive_reason_var,width=35)
        inactive_reason_ent.place(x=150,y=405)

        academic_frame2=Frame(MAIN_FRAME_0,height=541,width=645,bg="lightblue",borderwidth=4,relief=RIDGE)
        academic_frame2.place(x=646,y=0)
        left_reason_lbl=Label(academic_frame2,text="Left Reason :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        left_reason_lbl.place(x=50,y=50)
        left_reason_var=StringVar()
        left_reason_ent=Entry(academic_frame2,textvariable=left_reason_var,width=60)
        left_reason_ent.place(x=150,y=55)

        progress_lbl=Label(academic_frame2,text="Progress :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        progress_lbl.place(x=70,y=100)
        progress_var=StringVar()
        progress_ent=Entry(academic_frame2,textvariable=progress_var,width=60)
        progress_ent.place(x=150,y=105)

        presence_lbl=Label(academic_frame2,text="Presence :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        presence_lbl.place(x=65,y=150)
        presence_var=IntVar()
        presence_ent=Entry(academic_frame2,textvariable=presence_var,width=10)
        presence_ent.place(x=150,y=155)

        out_of_lbl=Label(academic_frame2,text="Out Of :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        out_of_lbl.place(x=230,y=150)
        out_of_var=IntVar()
        out_of_ent=Entry(academic_frame2,textvariable=out_of_var,width=10)
        out_of_ent.place(x=290,y=155)

        lc_lbl=Label(academic_frame2,text="LC Book/No/Date :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        lc_lbl.place(x=17,y=200)
        lc_book_var=StringVar()
        lc_book_ent=Entry(academic_frame2,textvariable=lc_book_var,width=10)
        lc_book_ent.place(x=150,y=205)
        lc_no_var=IntVar()
        lc_no_ent=Entry(academic_frame2,textvariable=lc_no_var,width=10)
        lc_no_ent.place(x=220,y=205)
        lc_date_ent=DateEntry(academic_frame2,selectmode="day",date_pattern="dd-mm-y")
        lc_date_ent.place(x=290,y=205)

        lc_remark_lbl=Label(academic_frame2,text="LC Remark :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        lc_remark_lbl.place(x=55,y=250)
        lc_remark_var=StringVar()
        lc_remark_ent=Entry(academic_frame2,textvariable=lc_remark_var,width=60)
        lc_remark_ent.place(x=150,y=255)

        lc_copy_lbl=Label(academic_frame2,text="LC Copy :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        lc_copy_lbl.place(x=70,y=300)
        lc_copy_var=StringVar()
        lc_copy_ent=Entry(academic_frame2,textvariable=lc_copy_var)
        lc_copy_ent.place(x=150,y=305)
        def academic_details_save():
            academic_details_lst=[]
            academic_details_lst.append(Gr_entry.get())#1
            academic_details_lst.append(Name_entry.get())#2
            academic_details_lst.append(activevalue.get())#3
            academic_details_lst.append(leftvalue.get())#4
            academic_details_lst.append(aaivalue.get())
            academic_details_lst.append(in_active_date_ent.get())#5
            academic_details_lst.append(addmission_date_ent.get())#6
            academic_details_lst.append(addmission_year_ent.get())#7
            academic_details_lst.append(addmission_standard_ent.get())#8
            academic_details_lst.append(current_date_ent.get())#9
            academic_details_lst.append(current_year_ent.get())#10
            academic_details_lst.append(current_standard_ent.get())#11
            academic_details_lst.append(division_ent.get())#12
            academic_details_lst.append(roll_no_ent.get())#13
            academic_details_lst.append(inactive_reason_ent.get())#14
            academic_details_lst.append(left_reason_ent.get())#15
            academic_details_lst.append(progress_ent.get())#16
            academic_details_lst.append(presence_ent.get())#17
            academic_details_lst.append(out_of_ent.get())#18
            academic_details_lst.append(lc_book_ent.get())#19
            academic_details_lst.append(lc_no_ent.get())#20
            academic_details_lst.append(lc_date_ent.get())#21
            academic_details_lst.append(lc_remark_ent.get())#22
            academic_details_lst.append(lc_copy_ent.get())#23
            cur.execute("insert into academic_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",academic_details_lst)
            
            if(aaivalue.get() == 0):
                cur.execute("select * from std_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("insert into pending_fee_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[Gr_entry.get(),data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12]])
            else:
                cur.execute("select * from exmp_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("insert into pending_fee_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[Gr_entry.get(),data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12]])
            cur.execute("insert into gr_check values({},0,0,0,0,0)".format(Gr_entry.get()))
            cur.execute("insert into fee_details values({},' ',' ',' ',' ',' ')".foramt(Gr_entry.get()))
            mydb.commit()
            other_details()
        save_next_button = Button(MAIN_FRAME_0,text="NEXT",font=("Arial",20),command=academic_details_save)
        save_next_button.place(x=1100,y=470)



    global other_details
    def other_details():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()

        other_details_BTN["state"]="active"   
        academic_details_BTN["state"]="disabled"
        gr_details_BTN["state"]="disabled"
        #
        Gr_label = Label(MAIN_FRAME_0, text="GR NO : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Gr_label.place(x=90, y=10)
        Gr_var=StringVar()
        Gr_entry= Entry(MAIN_FRAME_0, textvariable=Gr_var, width=40)
        Gr_entry.place(x=150, y=10)
        cur.execute("select gr_no from gr_details")
        data = cur.fetchall()
        Gr_entry.insert(0,data[-1][0]) 

        #
        Name_label = Label(MAIN_FRAME_0, text="Name : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Name_label.place(x=490, y=10)
        Name_var=StringVar()
        Name_entry=Entry(MAIN_FRAME_0, textvariable=Name_var, width=40)
        Name_entry.place(x=550,y=10)

        #
        Bank_holder=Label(MAIN_FRAME_0, text="Bank Acc. Holder : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Bank_holder.place(x=870,y=10)
        Bank_holder_var=StringVar()
        Bank_holder_entry = Entry(MAIN_FRAME_0, textvariable=Bank_holder_var, width=40)
        Bank_holder_entry.place(x=1000, y=10)

        #
        Scholarship_label = Label(MAIN_FRAME_0, text="Scholarship Category : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Scholarship_label.place(x=0, y=50)
        Scholarship_var=StringVar()
        Scholarship_entry = Entry(MAIN_FRAME_0, textvariable=Scholarship_var, width=40)
        Scholarship_entry.place(x=150, y=50)

        #
        Transport_label = Label(MAIN_FRAME_0, text="Transport : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue" )
        Transport_label.place(x=470, y=50)
        Transport_var=StringVar()
        Transport_entry=Entry(MAIN_FRAME_0, textvariable=Transport_var, width=40)
        Transport_entry.place(x=550, y=50)

        #
        bnk_name_label = Label(MAIN_FRAME_0, text="Bank Name : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        bnk_name_label.place(x=905, y=50)
        bnk_name_var=StringVar()
        bnk_name_entry=Entry(MAIN_FRAME_0, textvariable=bnk_name_label, width=40)
        bnk_name_entry.place(x=1000,y=50)

        #
        preschool_label=Label(MAIN_FRAME_0,text='PreSchool Type : ',font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        preschool_label.place(x=30, y=90)
        preschool_var=StringVar()
        preschool_entry=Entry(MAIN_FRAME_0, textvariable=preschool_var, width=40)
        preschool_entry.place(x=150, y=90)

        #
        blood_label = Label(MAIN_FRAME_0, text="Blood Group : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        blood_label.place(x=450, y=90)
        blood_var=StringVar()
        blood_entry= Entry(MAIN_FRAME_0, textvariable=blood_var,width=40)
        blood_entry.place(x=550, y=90)

        #
        bank_acc_no_label = Label(MAIN_FRAME_0, text="Bank Account No : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        bank_acc_no_label.place(x=870, y=90)
        bank_ac_no_var=StringVar()
        bank_ac_no_entry = Entry(MAIN_FRAME_0, textvariable=bank_ac_no_var,width=40)
        bank_ac_no_entry.place(x=1000, y=90)

        #
        Remark_label = Label(MAIN_FRAME_0, text="Remark : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Remark_label.place(x=80, y=130)
        Remark_var=StringVar()
        Remark_entry= Entry(MAIN_FRAME_0, textvariable=Remark_var,width=107)
        Remark_entry.place(x=150, y=130)

        #
        bank_branch_label = Label(MAIN_FRAME_0, text="Bank Branch : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        bank_branch_label.place(x=900, y=130)
        bank_branch_var=StringVar()
        bank_branch_entry= Entry(MAIN_FRAME_0, textvariable=bank_branch_var,width=40)
        bank_branch_entry.place(x=1000, y=130)

        #
        student_email_label = Label(MAIN_FRAME_0, text="Student Email : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        student_email_label.place(x=40, y=170)
        student_email_var=StringVar()
        student_email_entry= Entry(MAIN_FRAME_0, textvariable=student_email_var,width=107)
        student_email_entry.place(x=150, y=170)

        #
        IFSC_label = Label(MAIN_FRAME_0, text="IFSC Code : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        IFSC_label.place(x=910, y=170)
        IFSC_var=StringVar()
        IFSC_entry= Entry(MAIN_FRAME_0, textvariable=IFSC_var,width=40)
        IFSC_entry.place(x=1000, y=170)

        #
        Mobile_No_label = Label(MAIN_FRAME_0, text="Mobile No. : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Mobile_No_label.place(x=60, y=210)
        Mobile_No_var=StringVar()
        Mobile_No_entry= Entry(MAIN_FRAME_0, textvariable=Mobile_No_var,width=40)
        Mobile_No_entry.place(x=150, y=210)

        #
        SUID_label = Label(MAIN_FRAME_0, text="SUID : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        SUID_label.place(x=495, y=210)
        SUID_var=StringVar()
        SUID_entry= Entry(MAIN_FRAME_0, textvariable=SUID_var,width=40)
        SUID_entry.place(x=550, y=210)

        #
        Adhar_no_label = Label(MAIN_FRAME_0, text="Adhar Card No : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Adhar_no_label.place(x=885, y=210)
        Adhar_no_var=StringVar()
        Adhar_no_entry= Entry(MAIN_FRAME_0, textvariable=Adhar_no_var,width=40)
        Adhar_no_entry.place(x=1000, y=210)



        present_address_frame = LabelFrame(MAIN_FRAME_0, bg="lightblue", text="Present Address", width=1280, height=240,relief=RIDGE)
        present_address_frame.place(x=10, y=300)

        #
        Address_label = Label(present_address_frame, text="Address : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Address_label.place(x=70, y=10)
        Address_var=StringVar()
        Address_entry1= Entry(present_address_frame, textvariable=Address_var, width=107)
        Address_entry1.place(x=140, y=10)
        Address_entry2= Entry(present_address_frame, textvariable=Address_var, width=107)
        Address_entry2.place(x=140, y=50)

        #
        Area_label = Label(present_address_frame, text="Area : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Area_label.place(x=90, y=90)
        Area_var=StringVar()
        Area_entry= Entry(present_address_frame, textvariable=Area_var,width=40)
        Area_entry.place(x=140, y=90)

        #
        City_label = Label(present_address_frame, text="City : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        City_label.place(x=493, y=90)
        City_var=StringVar()
        City_entry= Entry(present_address_frame, textvariable=City_var,width=40)
        City_entry.place(x=540, y=90)

        #
        District_label = Label(present_address_frame, text="District : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        District_label.place(x=78, y=130)
        District_var=StringVar()
        District_entry= Entry(present_address_frame, textvariable=District_var,width=40)
        District_entry.place(x=140, y=130)


        Pincode_label = Label(present_address_frame, text="Pincode : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Pincode_label.place(x=465, y=130)
        Pincode_var=StringVar()
        Pincode_entry= Entry(present_address_frame, textvariable=Pincode_var,width=40)
        Pincode_entry.place(x=540, y=130)


        Phone_label = Label(present_address_frame, text="Phone No : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Phone_label.place(x=60, y=170)
        Phone_var=StringVar()
        Phone_entry= Entry(present_address_frame, textvariable=Phone_var,width=40)
        Phone_entry.place(x=140, y=170)

        def others_details1():
            others_details_list = []
            others_details_list.append(Gr_entry.get())#1
            others_details_list.append(Name_entry.get())#2
            others_details_list.append(Bank_holder_entry.get())#3
            others_details_list.append(Scholarship_entry.get())#4
            others_details_list.append(Transport_entry.get())#5
            others_details_list.append(bnk_name_entry.get())#6
            others_details_list.append(preschool_entry.get())#7
            others_details_list.append(blood_entry.get())#8
            others_details_list.append(bank_ac_no_entry.get())#9
            others_details_list.append(Remark_entry.get())#10
            others_details_list.append(bank_branch_entry.get())#11
            others_details_list.append(student_email_entry.get())#12
            others_details_list.append(IFSC_entry.get())#13
            others_details_list.append(Mobile_No_entry.get())#14
            others_details_list.append(SUID_entry.get())#15
            others_details_list.append(Adhar_no_entry.get())#16
            others_details_list.append(Address_entry1.get())#17
            others_details_list.append(Address_entry2.get())#18
            others_details_list.append(Area_entry.get())#19
            others_details_list.append(City_entry.get())#20
            others_details_list.append(District_entry.get())#21
            others_details_list.append(Pincode_entry.get())#22
            others_details_list.append(Phone_entry.get())#23
            cur.execute("insert into other_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",others_details_list)
            # cur.execute("select GRNO,NAME,CURRENT_STANDARD,DIVISON from academic_details")
            # aca_data = cur.fetchall()
            # cur.execute("insert into fee(GR,NAME,STD,DIVISON) values(%s,%s,%s,%s)",[aca_data[0][0],aca_data[0][1],aca_data[0][2],aca_data[0][3]])
            mydb.commit()
            gr_details()

        save_next_button = Button(MAIN_FRAME_0,text="SAVE",font=("Arial",20),command=others_details1)
        save_next_button.place(x=1100,y=470)

    def gr_details1():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()
        
        gr_details_BTN["state"]="active"
        academic_details_BTN["state"]="disabled"
        other_details_BTN["state"]="disabled"

        MAIN_FRAME_0.configure(bg="lightblue")

        photo_frame = Frame(MAIN_FRAME_0,height=155,width=155,borderwidth=4,relief=RIDGE)
        photo_frame.place(x=30,y=20)
        
        details_frame=Frame(MAIN_FRAME_0,height=150,width=1000,bg="lightblue",borderwidth=4,relief=RIDGE)
        details_frame.place(x=220,y=20)

        
        general_details_frame=Frame(MAIN_FRAME_0,height=360,width=800,bg="lightblue",borderwidth=4,relief=RIDGE)
        general_details_frame.place(x=220,y=175)

        gr_lbl=Label(details_frame,text="GR no :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        gr_lbl.place(x=23,y=20)
        gr_var=IntVar()
        gr_ent=Entry(details_frame,textvariable=gr_var)
        gr_ent.place(x=86,y=25)
        gr_ent.delete(0,END)
        cur.execute("select * from gr_details")
        grdata = cur.fetchall()
        gr_ent.insert(0,grdata[-1][0])
        data = cur.execute("select * from gr_details where gr_no={}".format(gr_ent.get()))
        data = cur.fetchall()
        global edit_gr_details
        edit_gr_details = data[0][0]


        form_no_lbl=Label(details_frame,text="Form No :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        form_no_lbl.place(x=240,y=20)
        form_no_var=IntVar()
        form_no_ent=Entry(details_frame,textvariable=form_no_var)
        form_no_ent.delete(0,END)
        form_no_ent.place(x=316,y=25)
        form_no_ent.insert(0,data[0][1])          
 
        enquiry_no_lbl=Label(details_frame,text="Enquiry No :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        enquiry_no_lbl.place(x=470,y=20)
        enquiry_no_var=IntVar()
        enquiry_no_ent=Entry(details_frame,textvariable=enquiry_no_var)
        enquiry_no_ent.delete(0,END)
        enquiry_no_ent.place(x=559,y=25) 
        enquiry_no_ent.insert(0,data[0][2])

        uid_lbl=Label(details_frame,text="UID :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        uid_lbl.place(x=720,y=20)
        uid_var=IntVar()
        uid_ent=Entry(details_frame,textvariable=uid_var)
        uid_ent.delete(0,END)
        uid_ent.place(x=771,y=25) 
        uid_ent.insert(0,data[0][3])

        name1_lbl=Label(details_frame,text="Name :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        name1_lbl.place(x=25,y=100)

        surname_lbl=Label(details_frame,text="Surname:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        surname_lbl.place(x=114,y=68)
        surname_var=StringVar()
        surname_ent=Entry(details_frame,text=surname_var)
        surname_ent.place(x=84,y=105)
        surname_ent.delete
        surname_ent.insert(0,data[0][4])

        name_lbl=Label(details_frame,text="Name:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        name_lbl.place(x=350,y=68)
        name_var=StringVar()
        name_ent=Entry(details_frame,text=name_var)
        name_ent.place(x=314,y=105)
        name_ent.delete(0,END)
        name_ent.insert(0,data[0][5])

        father_lbl=Label(details_frame,text="Father:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        father_lbl.place(x=590,y=68)
        father_var=StringVar()
        father_ent=Entry(details_frame,text=father_var)
        father_ent.place(x=557,y=105)
        father_ent.delete(0,END)
        father_ent.insert(0,data[0][6])

        mother_lbl=Label(details_frame,text="Mother:",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        mother_lbl.place(x=800,y=68)
        mother_var=StringVar()
        mother_ent=Entry(details_frame,text=mother_var)
        mother_ent.place(x=769,y=105)
        mother_ent.delete(0,END)
        mother_ent.insert(0,data[0][7])


        sex_lbl=Label(general_details_frame,text="Sex :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        sex_lbl.place(x=50,y=40)
        sex_var= StringVar()
        sex_combo = ttk.Combobox(general_details_frame,width=20,textvariable= sex_var)
        sex_combo['values'] = ('Male','Female')
        sex_combo.place(x=100,y=45)
        sex_combo.delete(0,END)
        sex_combo.insert(0,data[0][8])

        birth_date_lbl=Label(general_details_frame,text="Birth Date :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        birth_date_lbl.place(x=280,y=40)
        birth_date_ent=DateEntry(general_details_frame,selectmode="day",date_pattern="dd-mm-y",width=17)
        birth_date_ent.place(x=370,y=45)
        birth_date_ent.delete(0,END)
        birth_date_ent.insert(0,data[0][9])

        category_lbl=Label(general_details_frame,text="Category :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        category_lbl.place(x=575,y=40)
        category_var=StringVar()
        category_combo = ttk.Combobox(general_details_frame,width=17,textvariable = category_var)
        category_combo['values'] = ('SEBC','ST','GEN','SC')
        category_combo.place(x=655,y=45)
        category_combo.delete(0,END)
        category_combo.insert(0,data[0][10])

        religion_lbl=Label(general_details_frame,text="Religion :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        religion_lbl.place(x=24,y=105)
        religion_var=StringVar()
        religion_combo = ttk.Combobox(general_details_frame,width=20,textvariable = religion_var)
        religion_combo['values'] = ('Hindhu','Muslim','Jain','Sikh','Cristian')
        religion_combo.place(x=100,y=110)
        religion_combo.delete(0,END)
        religion_combo.insert(0,data[0][11])

        
        birth_place_lbl=Label(general_details_frame,text="Birth Place :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        birth_place_lbl.place(x=274,y=105)
        birth_place_var=StringVar()
        birth_place_ent=Entry(general_details_frame,text=birth_place_var)
        birth_place_ent.place(x=370,y=110)
        birth_place_ent.delete(0,END)
        birth_place_ent.insert(0,data[0][12])

        previous_school_lbl=Label(general_details_frame,text="Previous School :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        previous_school_lbl.place(x=530,y=105)
        previous_school_var=StringVar()
        previous_school_ent=Entry(general_details_frame,text=previous_school_var)
        previous_school_ent.place(x=655,y=110)
        previous_school_ent.delete(0,END)
        previous_school_ent.insert(0,data[0][13])

        caste_lbl=Label(general_details_frame,text="Caste :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        caste_lbl.place(x=42,y=170)
        caste_var=StringVar()
        caste_combo = ttk.Combobox(general_details_frame,textvariable = caste_var)
        caste_combo['values'] = ('Hindhu','Muslim','Jain','Sikh','Cristian')
        caste_combo.place(x=100,y=175)
        caste_combo.delete(0,END)
        caste_combo.insert(0,data[0][14])

        
        birth_taluka_lbl=Label(general_details_frame,text="Birth Taluka :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        birth_taluka_lbl.place(x=268,y=170)
        birth_taluka_var=StringVar()
        birth_taluka_ent=Entry(general_details_frame,text=birth_taluka_var)
        birth_taluka_ent.place(x=370,y=175)
        birth_taluka_ent.delete(0,END)
        birth_taluka_ent.insert(0,data[0][15])

        subcaste_lbl=Label(general_details_frame,text="Subcaste :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        subcaste_lbl.place(x=21,y=240)
        subcaste_var=StringVar()
        subcaste_combo = ttk.Combobox(general_details_frame,width=20,textvariable = subcaste_var)
        subcaste_combo['values'] = ('Hindhu','Muslim','Jain','Sikh','Cristian')
        subcaste_combo.place(x=100,y=245)
        subcaste_combo.delete(0,END)
        subcaste_combo.insert(0,data[0][16])

        state_lbl=Label(general_details_frame,text="State :",padx=5,pady=5,bg="lightblue",font=("Arial",10,"bold"))
        state_lbl.place(x=310,y=240)
        state_var=StringVar()
        state_ent=Entry(general_details_frame,text=state_var)
        state_ent.place(x=370,y=245)
        state_ent.delete(0,END)
        state_ent.insert(0,data[0][17])

        minorityvalue=IntVar()
        minority_check=Checkbutton(general_details_frame,text="Minority",onvalue=1,offvalue=0,bg="lightblue",activebackground="black")
        minority_check.place(x=100,y=315)
        if (data[0][18]==0):
            minority_check.deselect()
        else:
            minority_check.select()

        rtevalue=IntVar()
        rte_check=Checkbutton(general_details_frame,text="RTE",variable=rtevalue,onvalue=1,offvalue=0,bg="lightblue",activebackground="black")
        rte_check.place(x=250,y=315)
        if(data[0][19] == 0):
            rte_check.deselect()
        else:
            rte_check.select()

        def grsave():
            grlst=[]
            grlst.append(form_no_ent.get())
            grlst.append(enquiry_no_ent.get())
            grlst.append(uid_ent.get())
            grlst.append(surname_ent.get())
            grlst.append(name_ent.get())
            grlst.append(father_ent.get())
            grlst.append(mother_ent.get())
            grlst.append(sex_combo.get())
            grlst.append(birth_date_ent.get())
            grlst.append(category_combo.get())
            grlst.append(religion_combo.get())
            grlst.append(birth_place_ent.get())
            grlst.append(previous_school_ent.get())
            grlst.append(caste_combo.get())
            grlst.append(birth_taluka_ent.get())
            grlst.append(subcaste_combo.get())            
            grlst.append(state_ent.get())
            grlst.append(minorityvalue.get())
            grlst.append(rtevalue.get())
            grlst.append(gr_ent.get())
            cur.execute("update gr_details set form_no=%s,enquiry_no=%s,uid=%s,surname=%s,name=%s,father=%s,MOTHER=%s,SEX=%s,BIRTH_DATE=%s,CATEGORY=%s,RELIGION=%s,BIRTH_PLACE=%s,PREVIOUS_SCH=%s,CASTE=%s,BIRTH_TALUKA=%s,SUB_CASTE=%s,STATE1=%s,MINORITY=%s,RTE=%s where gr_no=%s",grlst)
            mydb.commit()
            academic_details1()
        save_next_button = Button(MAIN_FRAME_0,text="NEXT",font=("Arial",20),command=grsave)
        save_next_button.place(x=1100,y=470)

    global academic_details1
    def academic_details1():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()
    
        academic_details_BTN["state"]="active"
        gr_details_BTN["state"]="disabled"
        other_details_BTN["state"]="disabled"



        academic_frame1=Frame(MAIN_FRAME_0,height=541,width=645,bg="lightblue",borderwidth=4,relief=RIDGE)
        academic_frame1.place(x=0,y=0)

        #
        Gr_label = Label(academic_frame1, text="GR NO : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Gr_label.place(x=90, y=10)
        Gr_var=StringVar()
        Gr_entry= Entry(academic_frame1, textvariable=Gr_var, width=20)
        Gr_entry.place(x=150, y=10)
        Gr_entry.delete(0,END)
        Gr_entry.insert(0,edit_gr_details)
        cur.execute("select * from academic_detail where gr_no=%s",[edit_gr_details])
        data = cur.fetchall()


        #
        Name_label = Label(academic_frame1, text="Name : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Name_label.place(x=310, y=10)
        Name_var=StringVar()
        Name_entry=Entry(academic_frame1, textvariable=Name_var, width=20)
        Name_entry.place(x=370,y=10)
        Name_entry.delete(0,END)
        Name_entry.insert(0,data[0][1])
  
        activevalue=IntVar()
        active_check=Checkbutton(academic_frame1,text="Active",variable=activevalue,offvalue=0,onvalue=1,activebackground="lightblue",font=("Arieal",10,"bold"),bg="lightblue")
        active_check.place(x=75,y=50)
        if(data[0][2] == 1):
            active_check.select()
        else:
            active_check.deselect()

        leftvalue=IntVar()
        left_check=Checkbutton(academic_frame1,text="Left",variable=leftvalue,offvalue=0,onvalue=1,activebackground="lightblue",font=("Arieal",10,"bold"),bg="lightblue")
        left_check.place(x=200,y=50)
        if(data[0][3] == 1):
            left_check.select()
        else:
            left_check.deselect()

        aaivalue=IntVar()
        aai_check=Checkbutton(academic_frame1,text="AAI",variable=aaivalue,offvalue=0,onvalue=1,activebackground="lightblue",font=("Arieal",10,"bold"),bg="lightblue")
        aai_check.place(x=325,y=50)
        if(data[0][4] == 1):
            aai_check.select()
        else:
            aai_check.deselect()
        #
        in_active_date_lbl=Label(academic_frame1,text="InActive Date :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        in_active_date_lbl.place(x=50,y=100)
        in_active_date_ent=DateEntry(academic_frame1,selectmode="day",date_pattern="dd-mm-y")
        in_active_date_ent.place(x=160,y=105)
        in_active_date_ent.delete(0,END)
        in_active_date_ent.insert(0,data[0][5])
 
        date_lbl=Label(academic_frame1,text="Date",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        date_lbl.place(x=180,y=160)

        year_lbl=Label(academic_frame1,text="Year",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        year_lbl.place(x=280,y=160)

        standard=Label(academic_frame1,text="Standard",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        standard.place(x=370,y=160)

        #
        addmission_lbl=Label(academic_frame1,text="Addmission :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        addmission_lbl.place(x=50,y=200)
        addmission_date_ent=DateEntry(academic_frame1,selectmode="day",date_pattern="dd-mm-y")
        addmission_date_ent.place(x=150,y=205)
        addmission_date_ent.delete(0,END)
        addmission_date_ent.insert(0,data[0][6])
        addmission_year_var=IntVar()
        addmission_year_ent=Entry(academic_frame1,textvariable=addmission_year_var,width=10)
        addmission_year_ent.place(x=275,y=205)
        addmission_year_ent.delete(0,END)
        addmission_year_ent.insert(0,data[0][7])
        addmission_standard_var=StringVar()
        addmission_standard_ent=ttk.Combobox(academic_frame1,textvariable=addmission_standard_var,width=10)
        addmission_standard_ent['values']=['NUR','JR.KG','SR.KG','1','2','3','4','5','6','7','8','9','10','11 COMM','11 SCI','12 COMM','12 SCI']
        addmission_standard_ent.place(x=370,y=205) 
        addmission_standard_ent.delete(0,END)
        addmission_standard_ent.insert(0,data[0][8])

        current_lbl=Label(academic_frame1,text="Current :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        current_lbl.place(x=75,y=240)
        current_date_ent=DateEntry(academic_frame1,selectmode="day",date_pattern="dd-mm-y")
        current_date_ent.place(x=150,y=245)
        current_date_ent.delete(0,END)
        current_date_ent.insert(0,data[0][9])
        current_year_var=IntVar()
        current_year_ent=Entry(academic_frame1,textvariable=current_year_var,width=10)
        current_year_ent.place(x=275,y=245)
        current_year_ent.delete(0,END)
        current_year_ent.insert(0,data[0][10])
        current_standard_var=StringVar()
        current_standard_ent=ttk.Combobox(academic_frame1,textvariable=current_standard_var,width=10)
        current_standard_ent['values']=['NUR','JR.KG','SR.KG','1','2','3','4','5','6','7','8','9','10','11 COMM','11 SCI','12 COMM','12 SCI']
        current_standard_ent.place(x=370,y=245) 
        current_standard_ent.delete(0,END)
        current_standard_ent.insert(0,data[0][11])

        division_lbl=Label(academic_frame1,text="Division :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        division_lbl.place(x=75,y=340)
        division_var=StringVar()
        division_ent=ttk.Combobox(academic_frame1,textvariable=division_var,width=8)
        division_ent['values']=['A','B','C','D','E']
        division_ent.place(x=150,y=345)
        division_ent.delete(0,END)
        division_ent.insert(0,data[0][12])

        roll_no_lbl=Label(academic_frame1,text="Roll No :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        roll_no_lbl.place(x=250,y=340)
        roll_no_var=IntVar()
        roll_no_ent=Entry(academic_frame1 ,textvariable=roll_no_var,width=10)
        roll_no_ent.place(x=320,y=345)
        roll_no_ent.delete(0,END)
        roll_no_ent.insert(0,data[0][13])

        inactive_reason_lbl=Label(academic_frame1,text="InActive Reason :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        inactive_reason_lbl.place(x=22,y=400)
        inactive_reason_var=StringVar()
        inactive_reason_ent=Entry(academic_frame1,textvariable=inactive_reason_var,width=35)
        inactive_reason_ent.place(x=150,y=405)
        inactive_reason_ent.delete(0,END)
        inactive_reason_ent.insert(0,data[0][14])

        academic_frame2=Frame(MAIN_FRAME_0,height=541,width=645,bg="lightblue",borderwidth=4,relief=RIDGE)
        academic_frame2.place(x=646,y=0)
        left_reason_lbl=Label(academic_frame2,text="Left Reason :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        left_reason_lbl.place(x=50,y=50)
        left_reason_var=StringVar()
        left_reason_ent=Entry(academic_frame2,textvariable=left_reason_var,width=60)
        left_reason_ent.place(x=150,y=55)
        left_reason_ent.delete(0,END)
        left_reason_ent.insert(0,data[0][15])

        progress_lbl=Label(academic_frame2,text="Progress :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        progress_lbl.place(x=70,y=100)
        progress_var=StringVar()
        progress_ent=Entry(academic_frame2,textvariable=progress_var,width=60)
        progress_ent.place(x=150,y=105)
        progress_ent.delete(0,END)
        progress_ent.insert(0,data[0][16])

        presence_lbl=Label(academic_frame2,text="Presence :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        presence_lbl.place(x=65,y=150)
        presence_var=IntVar()
        presence_ent=Entry(academic_frame2,textvariable=presence_var,width=10)
        presence_ent.place(x=150,y=155)
        presence_ent.delete(0,END)
        presence_ent.insert(0,data[0][17])

        out_of_lbl=Label(academic_frame2,text="Out Of :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        out_of_lbl.place(x=230,y=150)
        out_of_var=IntVar()
        out_of_ent=Entry(academic_frame2,textvariable=out_of_var,width=10)
        out_of_ent.place(x=290,y=155)
        out_of_ent.delete(0,END)
        out_of_ent.insert(0,data[0][18])

        lc_lbl=Label(academic_frame2,text="LC Book/No/Date :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        lc_lbl.place(x=17,y=200)
        lc_book_var=StringVar()
        lc_book_ent=Entry(academic_frame2,textvariable=lc_book_var,width=10)
        lc_book_ent.place(x=150,y=205)
        lc_book_ent.delete(0,END)
        lc_book_ent.insert(0,data[0][19])
        lc_no_var=IntVar()
        lc_no_ent=Entry(academic_frame2,textvariable=lc_no_var,width=10)
        lc_no_ent.place(x=220,y=205)
        lc_no_ent.delete(0,END)
        lc_no_ent.insert(0,data[0][20])
        lc_date_ent=DateEntry(academic_frame2,selectmode="day",date_pattern="dd-mm-y")
        lc_date_ent.place(x=290,y=205)
        lc_date_ent.delete(0,END)
        lc_date_ent.insert(0,data[0][21])

        lc_remark_lbl=Label(academic_frame2,text="LC Remark :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        lc_remark_lbl.place(x=55,y=250)
        lc_remark_var=StringVar()
        lc_remark_ent=Entry(academic_frame2,textvariable=lc_remark_var,width=60)
        lc_remark_ent.place(x=150,y=255)
        lc_remark_ent.delete(0,END)
        lc_remark_ent.insert(0,data[0][22])

        lc_copy_lbl=Label(academic_frame2,text="LC Copy :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        lc_copy_lbl.place(x=70,y=300)
        lc_copy_var=StringVar()
        lc_copy_ent=Entry(academic_frame2,textvariable=lc_copy_var)
        lc_copy_ent.place(x=150,y=305)
        lc_copy_ent.delete(0,END)
        lc_copy_ent.insert(0,data[0][23])
        def academic_details_save():
            academic_details_lst=[]
            academic_details_lst.append(Name_entry.get())#2
            academic_details_lst.append(activevalue.get())#3
            academic_details_lst.append(leftvalue.get())#4
            academic_details_lst.append(aaivalue.get())
            academic_details_lst.append(in_active_date_ent.get())#5
            academic_details_lst.append(addmission_date_ent.get())#6
            academic_details_lst.append(addmission_year_ent.get())#7
            academic_details_lst.append(addmission_standard_ent.get())#8
            academic_details_lst.append(current_date_ent.get())#9
            academic_details_lst.append(current_year_ent.get())#10
            academic_details_lst.append(current_standard_ent.get())#11
            academic_details_lst.append(division_ent.get())#12
            academic_details_lst.append(roll_no_ent.get())#13
            academic_details_lst.append(inactive_reason_ent.get())#14
            academic_details_lst.append(left_reason_ent.get())#15
            academic_details_lst.append(progress_ent.get())#16
            academic_details_lst.append(presence_ent.get())#17
            academic_details_lst.append(out_of_ent.get())#18
            academic_details_lst.append(lc_book_ent.get())#19
            academic_details_lst.append(lc_no_ent.get())#20
            academic_details_lst.append(lc_date_ent.get())#21
            academic_details_lst.append(lc_remark_ent.get())#22
            academic_details_lst.append(lc_copy_ent.get())#23
            academic_details_lst.append(Gr_entry.get())#1
            cur.execute("update academic_detail set name=%s,active1=%s,left1=%s,aai1=%s,inactive_date=%s,add_date=%s,add_year=%s,add_std=%s,curr_date=%s,curr_year=%s,curr_std=%s,divison=%s,roll_no=%s,inactive_reason=%s,left_reason=%s,progress=%s,presence=%s,out_of=%s,lc_book=%s,lc_no=%s,lc_date=%s,lc_remark=%s,lc_copy=%s where gr_no=%s",academic_details_lst)
            
            if(aaivalue.get() == 0):
                cur.execute("select * from std_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("update pending_fee_detail set ADMISSION_FEE=%s,ICARD=%s,APR_JUN_TUTION=%s,APR_JUN_ACTIVITY=%s,LATE_FEES=%s,JUL_SEP_TUTION=%s,JUL_SEP_ACTIVITY=%s,OCT_DEC_TUTION=%s,OCT_DEC_ACTIVITY=%s,JAN_MAR_TUTION=%s,JAN_MAR_ACTIVITY=%s,OTHERS=%s where GR_NO=%s",[data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12],Gr_entry.get()])
            else:
                cur.execute("select * from exmp_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("update pending_fee_detail set ADMISSION_FEE=%s,ICARD=%s,APR_JUN_TUTION=%s,APR_JUN_ACTIVITY=%s,LATE_FEES=%s,JUL_SEP_TUTION=%s,JUL_SEP_ACTIVITY=%s,OCT_DEC_TUTION=%s,OCT_DEC_ACTIVITY=%s,JAN_MAR_TUTION=%s,JAN_MAR_ACTIVITY=%s,OTHERS=%s where GR_NO=%s",[data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12],Gr_entry.get()])
            mydb.commit()
            other_details1()
        save_next_button = Button(MAIN_FRAME_0,text="NEXT",font=("Arial",20),command=academic_details_save)
        save_next_button.place(x=1100,y=470)



    global other_details1
    def other_details1():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()

        other_details_BTN["state"]="active"   
        academic_details_BTN["state"]="disabled"
        gr_details_BTN["state"]="disabled"
        #
        Gr_label = Label(MAIN_FRAME_0, text="GR NO : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Gr_label.place(x=90, y=10)
        Gr_var=StringVar()
        Gr_entry= Entry(MAIN_FRAME_0, textvariable=Gr_var, width=40)
        Gr_entry.place(x=150, y=10)
        Gr_entry.delete(0,END)
        Gr_entry.insert(0,edit_gr_details)
        cur.execute("select * from other_detail where gr_no=%s",[edit_gr_details])
        data = cur.fetchall()
        
        #
        Name_label = Label(MAIN_FRAME_0, text="Name : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Name_label.place(x=490, y=10)
        Name_var=StringVar()
        Name_entry=Entry(MAIN_FRAME_0, textvariable=Name_var, width=40)
        Name_entry.place(x=550,y=10)
        Name_entry.delete(0,END)
        Name_entry.insert(0,data[0][1])

        #
        Bank_holder=Label(MAIN_FRAME_0, text="Bank Acc. Holder : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Bank_holder.place(x=870,y=10)
        Bank_holder_var=StringVar()
        Bank_holder_entry = Entry(MAIN_FRAME_0, textvariable=Bank_holder_var, width=40)
        Bank_holder_entry.place(x=1000, y=10)
        Bank_holder_entry.delete(0,END)
        Bank_holder_entry.insert(0,data[0][2])

        #
        Scholarship_label = Label(MAIN_FRAME_0, text="Scholarship Category : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Scholarship_label.place(x=0, y=50)
        Scholarship_var=StringVar()
        Scholarship_entry = Entry(MAIN_FRAME_0, textvariable=Scholarship_var, width=40)
        Scholarship_entry.place(x=150, y=50)
        Scholarship_entry.delete(0,END)
        Scholarship_entry.insert(0,data[0][3])

        #
        Transport_label = Label(MAIN_FRAME_0, text="Transport : ", font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue" )
        Transport_label.place(x=470, y=50)
        Transport_var=StringVar()
        Transport_entry=Entry(MAIN_FRAME_0, textvariable=Transport_var, width=40)
        Transport_entry.place(x=550, y=50)
        Transport_entry.delete(0,END)
        Transport_entry.insert(0,data[0][4])

        #
        bnk_name_label = Label(MAIN_FRAME_0, text="Bank Name : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        bnk_name_label.place(x=905, y=50)
        bnk_name_var=StringVar()
        bnk_name_entry=Entry(MAIN_FRAME_0, textvariable=bnk_name_label, width=40)
        bnk_name_entry.place(x=1000,y=50)
        bnk_name_entry.delete(0,END)
        bnk_name_entry.insert(0,data[0][5])

        #
        preschool_label=Label(MAIN_FRAME_0,text='PreSchool Type : ',font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        preschool_label.place(x=30, y=90)
        preschool_var=StringVar()
        preschool_entry=Entry(MAIN_FRAME_0, textvariable=preschool_var, width=40)
        preschool_entry.place(x=150, y=90)
        preschool_entry.delete(0,END)
        preschool_entry.insert(0,data[0][6])

        #
        blood_label = Label(MAIN_FRAME_0, text="Blood Group : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        blood_label.place(x=450, y=90)
        blood_var=StringVar()
        blood_entry= Entry(MAIN_FRAME_0, textvariable=blood_var,width=40)
        blood_entry.place(x=550, y=90)
        blood_entry.delete(0,END)
        blood_entry.insert(0,data[0][7])

        #
        bank_acc_no_label = Label(MAIN_FRAME_0, text="Bank Account No : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        bank_acc_no_label.place(x=870, y=90)
        bank_ac_no_var=StringVar()
        bank_ac_no_entry = Entry(MAIN_FRAME_0, textvariable=bank_ac_no_var,width=40)
        bank_ac_no_entry.place(x=1000, y=90)
        bank_ac_no_entry.delete(0,END)
        bank_ac_no_entry.insert(0,data[0][8])

        #
        Remark_label = Label(MAIN_FRAME_0, text="Remark : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Remark_label.place(x=80, y=130)
        Remark_var=StringVar()
        Remark_entry= Entry(MAIN_FRAME_0, textvariable=Remark_var,width=107)
        Remark_entry.place(x=150, y=130)
        Remark_entry.delete(0,END)
        Remark_entry.insert(0,data[0][9])

        #
        bank_branch_label = Label(MAIN_FRAME_0, text="Bank Branch : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        bank_branch_label.place(x=900, y=130)
        bank_branch_var=StringVar()
        bank_branch_entry= Entry(MAIN_FRAME_0, textvariable=bank_branch_var,width=40)
        bank_branch_entry.place(x=1000, y=130)
        bank_branch_entry.delete(0,END)
        bank_branch_entry.insert(0,data[0][10])

        #
        student_email_label = Label(MAIN_FRAME_0, text="Student Email : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        student_email_label.place(x=40, y=170)
        student_email_var=StringVar()
        student_email_entry= Entry(MAIN_FRAME_0, textvariable=student_email_var,width=107)
        student_email_entry.place(x=150, y=170)
        student_email_entry.delete(0,END)
        student_email_entry.insert(0,data[0][11])

        #
        IFSC_label = Label(MAIN_FRAME_0, text="IFSC Code : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        IFSC_label.place(x=910, y=170)
        IFSC_var=StringVar()
        IFSC_entry= Entry(MAIN_FRAME_0, textvariable=IFSC_var,width=40)
        IFSC_entry.place(x=1000, y=170)
        IFSC_entry.delete(0,END)
        IFSC_entry.insert(0,data[0][12])

        #
        Mobile_No_label = Label(MAIN_FRAME_0, text="Mobile No. : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Mobile_No_label.place(x=60, y=210)
        Mobile_No_var=StringVar()
        Mobile_No_entry= Entry(MAIN_FRAME_0, textvariable=Mobile_No_var,width=40)
        Mobile_No_entry.place(x=150, y=210)
        Mobile_No_entry.delete(0,END)
        Mobile_No_entry.insert(0,data[0][13])

        #
        SUID_label = Label(MAIN_FRAME_0, text="SUID : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        SUID_label.place(x=495, y=210)
        SUID_var=StringVar()
        SUID_entry= Entry(MAIN_FRAME_0, textvariable=SUID_var,width=40)
        SUID_entry.place(x=550, y=210)
        SUID_entry.delete(0,END)
        SUID_entry.insert(0,data[0][14])

        #
        Adhar_no_label = Label(MAIN_FRAME_0, text="Adhar Card No : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Adhar_no_label.place(x=885, y=210)
        Adhar_no_var=StringVar()
        Adhar_no_entry= Entry(MAIN_FRAME_0, textvariable=Adhar_no_var,width=40)
        Adhar_no_entry.place(x=1000, y=210)
        Adhar_no_entry.delete(0,END)
        Adhar_no_entry.insert(0,data[0][15])



        present_address_frame = LabelFrame(MAIN_FRAME_0, bg="lightblue", text="Present Address", width=1280, height=240,relief=RIDGE)
        present_address_frame.place(x=10, y=300)

        #
        Address_label = Label(present_address_frame, text="Address : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Address_label.place(x=70, y=10)
        Address_var=StringVar()
        Address_entry1= Entry(present_address_frame, textvariable=Address_var, width=107)
        Address_entry1.place(x=140, y=10)
        Address_entry1.delete(0,END)
        Address_entry1.insert(0,data[0][16])
        Address_entry2= Entry(present_address_frame, textvariable=Address_var, width=107)
        Address_entry2.place(x=140, y=50)
        Address_entry2.delete(0,END)
        Address_entry2.insert(0,data[0][17])

        #
        Area_label = Label(present_address_frame, text="Area : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Area_label.place(x=90, y=90)
        Area_var=StringVar()
        Area_entry= Entry(present_address_frame, textvariable=Area_var,width=40)
        Area_entry.place(x=140, y=90)
        Area_entry.delete(0,END)
        Area_entry.insert(0,data[0][18])

        #
        City_label = Label(present_address_frame, text="City : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        City_label.place(x=493, y=90)
        City_var=StringVar()
        City_entry= Entry(present_address_frame, textvariable=City_var,width=40)
        City_entry.place(x=540, y=90)
        City_entry.delete(0,END)
        City_entry.insert(0,data[0][19])

        #
        District_label = Label(present_address_frame, text="District : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        District_label.place(x=78, y=130)
        District_var=StringVar()
        District_entry= Entry(present_address_frame, textvariable=District_var,width=40)
        District_entry.place(x=140, y=130)
        District_entry.delete(0,END)
        District_entry.insert(0,data[0][20])


        Pincode_label = Label(present_address_frame, text="Pincode : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Pincode_label.place(x=465, y=130)
        Pincode_var=StringVar()
        Pincode_entry= Entry(present_address_frame, textvariable=Pincode_var,width=40)
        Pincode_entry.place(x=540, y=130)
        Pincode_entry.delete(0,END)
        Pincode_entry.insert(0,data[0][21])


        Phone_label = Label(present_address_frame, text="Phone No : ",font=('Monteserrat', 10, 'bold'), fg="black", bg="lightblue")
        Phone_label.place(x=60, y=170)
        Phone_var=StringVar()
        Phone_entry= Entry(present_address_frame, textvariable=Phone_var,width=40)
        Phone_entry.place(x=140, y=170)
        Phone_entry.delete(0,END)
        Phone_entry.insert(0,data[0][22])

        def others_details1():
            others_details_list = []
            others_details_list.append(Name_entry.get())#2
            others_details_list.append(Bank_holder_entry.get())#3
            others_details_list.append(Scholarship_entry.get())#4
            others_details_list.append(Transport_entry.get())#5
            others_details_list.append(bnk_name_entry.get())#6
            others_details_list.append(preschool_entry.get())#7
            others_details_list.append(blood_entry.get())#8
            others_details_list.append(bank_ac_no_entry.get())#9
            others_details_list.append(Remark_entry.get())#10
            others_details_list.append(bank_branch_entry.get())#11
            others_details_list.append(student_email_entry.get())#12
            others_details_list.append(IFSC_entry.get())#13
            others_details_list.append(Mobile_No_entry.get())#14
            others_details_list.append(SUID_entry.get())#15
            others_details_list.append(Adhar_no_entry.get())#16
            others_details_list.append(Address_entry1.get())#17
            others_details_list.append(Address_entry2.get())#18
            others_details_list.append(Area_entry.get())#19
            others_details_list.append(City_entry.get())#20
            others_details_list.append(District_entry.get())#21
            others_details_list.append(Pincode_entry.get())#22
            others_details_list.append(Phone_entry.get())#23
            others_details_list.append(Gr_entry.get())#1
            cur.execute("update other_detail set name=%s,bnk_ac_holder=%s,scholar_cat=%s,transport=%s,bnk_name=%s,presch_type=%s,blood_grp=%s,bnk_ac_name=%s,remark=%s,bnk_branch=%s,student_email=%s,ifsc_code=%s,mobile_no=%s,suid=%s,adhar_cardno=%s,address1=%s,address2=%s,area=%s,city=%s,district=%s,pincode=%s,phone_no=%s where gr_no=%s",others_details_list)
            mydb.commit()
            gr_details()

        save_next_button = Button(MAIN_FRAME_0,text="SAVE",font=("Arial",20),command=others_details1)
        save_next_button.place(x=1100,y=470)

    def add1():
        GR_EDIT_BTN["state"]="active"
        GR_DELETE_BTN["state"]="active"
        GR_PRINT_BTN["state"]="active"
        gr_details_BTN["state"]="active"
        academic_details_BTN["state"]="active"
        other_details_BTN["state"]="active"
        gr_details()

    def edit1():
        gr_details1()



    gr_details_BTN=Button(MAIN_FRAME,text="GR DETAILS",width=15,command=gr_details)
    gr_details_BTN.place(x=0,y=0)
    gr_details_BTN["state"]="disabled"
        

    academic_details_BTN=Button(MAIN_FRAME,text="ACADEMIC DETAILS",width=15,command=academic_details)
    academic_details_BTN.place(x=120,y=0)
    academic_details_BTN["state"]="disabled"
        

    other_details_BTN=Button(MAIN_FRAME,text="OTHER DETAILS",width=15,command=other_details)
    other_details_BTN.place(x=240,y=0)
    other_details_BTN["state"]="disabled"

    





    img1_add = Image.open(r"ICONS\add.png")
    resized1_add = img1_add.resize((50,50))
    img_add = ImageTk.PhotoImage(resized1_add)
    GR_ADD_BTN=Button(MENU_FRAME2,text="ADD",command=add1,image=img_add,compound=TOP, bg="lightgrey", relief=FLAT)
    GR_ADD_BTN.place(x=20,y=60)
    


    img1_edit = Image.open(r"ICONS\edit.png")
    resized1_edit = img1_edit.resize((50,50))
    img_edit = ImageTk.PhotoImage(resized1_edit)
    GR_EDIT_BTN=Button(MENU_FRAME2,text="EDIT",command=edit1,image=img_edit,compound=TOP, bg="lightgrey", relief=FLAT)
    GR_EDIT_BTN.place(x=20,y=160)
    GR_EDIT_BTN["state"]="disabled"
   


    img1_delete = Image.open(r"ICONS\delete.png")
    resized1_delete= img1_delete.resize((50,50))
    img_delete = ImageTk.PhotoImage(resized1_delete)
    GR_DELETE_BTN=Button(MENU_FRAME2,text=r"DELETE",image=img_delete,compound=TOP, bg="lightgrey", relief=FLAT)
    GR_DELETE_BTN.place(x=20,y=260)
    GR_DELETE_BTN["state"]="disabled"
  


    img1_print = Image.open(r"ICONS\search.png")
    resized1_print = img1_print.resize((50,50))
    img_print = ImageTk.PhotoImage(resized1_print)
    GR_PRINT_BTN=Button(MENU_FRAME2,text="PRINT",image=img_print,compound=TOP, bg="lightgrey", relief=FLAT)
    GR_PRINT_BTN.place(x=20,y=360)
    GR_PRINT_BTN["state"]="disabled"



    img1_exit = Image.open(r"ICONS\exit.png")
    resized1_exit = img1_exit.resize((50,50))
    img_exit = ImageTk.PhotoImage(resized1_exit)
    GR_EXIT_BTN=Button(MENU_FRAME2,text="EXIT",image=img_exit,compound=TOP, bg="lightgrey", relief=FLAT)
    GR_EXIT_BTN.place(x=20,y=460)
    mainloop()
    










    #=================    =================    =================    =================   
    #=================    =================    =================    ================= 
    #====                 ====                 ====                 ====
    #====                 ====                 ====                 ====
    #=================    =================    =================    ================= 
    #=================    =================    =================    ================= 
    #===                  ====                 ====                              ====
    #===                  ====                 ====                              ====
    #===                  =================    =================    ================= 
    #===                  =================    =================    ================= 


    
     
    


    

def FEES_FUNCTION():
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy()
    MAIN_FRAME.configure(bg="lightpink")

    FEES_1=Button(MENU_FRAME2,text="FEES 1")
    FEES_1.place(x=20,y=20)


    wrapper1=Frame(MAIN_FRAME,height=250,width=620)
    wrapper1.place(x=50,y=170)
    style = ttk.Style()
    style.theme_use('clam')
    trv=ttk.Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="10")

    trv.pack(side=LEFT)

    trv.heading("#1",text="Fees Name")
    trv.heading("#2",text="Fees Amount")
    trv.heading("#3",text="Exemption")
    trv.heading("#4",text="Total")
    trv.column("#1",width=180)
    trv.column("#2",width=180)
    trv.column("#3",width=180)
    trv.column("#4",width=180)


    y_scroll=Scrollbar(wrapper1,orient="vertical",command=trv.yview)
    y_scroll.pack(side=RIGHT,fill='y')
    trv.configure(yscrollcommand=y_scroll.set)




    wrapper2=Frame(MAIN_FRAME,bg="lightpink",height=250,width=270,relief=RIDGE,borderwidth=2)
    wrapper2.place(x=1000,y=100)


    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    # CheckVar6 = IntVar()

    C1 = Checkbutton(wrapper2, text = "APR JUN FEES", variable = CheckVar1,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C2 = Checkbutton(wrapper2, text = "JUL SEP FEES", variable = CheckVar2,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C3 = Checkbutton(wrapper2, text = "OCT DEC FEES", variable = CheckVar3,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C4 = Checkbutton(wrapper2, text = "JAN MAR FEES", variable = CheckVar4,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    C5 = Checkbutton(wrapper2, text = "OTHERS", variable = CheckVar5,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
    # C6 = Checkbutton(wrapper2, text = "6", variable = CheckVar6,onvalue = 1, offvalue = 0, height=1,)
    C1.place(x=0,y=0)
    C2.place(x=0,y=45)
    C3.place(x=0,y=90)
    C4.place(x=0,y=135)
    C5.place(x=0,y=180)
    # C6.place(x=0,y=150)



    def fees_search():

        root.bell()
        top = Toplevel()
        # top.attributes('-fullscreen', True)
        top.geometry("1400x700")
        top.title("ZETA CORE")
        photo = PhotoImage(file = r"ICONS\Zeta.png")
        top.iconphoto(False, photo)

        def search():
            name=name_entry.get()
            name = name.capitalize()
            surname=surname_entry.get()
            surname = surname.capitalize()
            gr_end = gr_num_var2.get()
            gr_start = gr_num_var.get()

            for record in treeview.get_children():
                treeview.delete(record)

            for i in range(len(values)):
                # print(values[i])
                for j in range(len(values[i])):
                    # print(values[i][j])
                    id=0
                    name_in_data=values[i][1]
                    # print(name_in_data)
                    surname_in_data=values[i][2]
                    # print(surname_in_data)
                    for p in range(gr_start, gr_end):
                        if values[i][0]==p:
                            if name == name_in_data[:len(name)] and surname==surname_in_data[:len(surname)]:
                                try:
                                    treeview.insert(parent='', iid=id, index='end',text='', values=values[i])  
                                    id+=1 
                                    break
                                except:
                                    pass

        def add_data():
            for record in treeview.get_children():
                treeview.delete(record)

            for i in range(len(values)):
                treeview.insert(parent='', iid=i, index='end',text='', values=values[i])

            
        global treeview
        global name_entry
        global surname_entry
        global values
        main_frame=Frame(top,bg='lightpink', width=1400, height=700, borderwidth=3, relief=RIDGE)
        main_frame.place(x=0, y=0)

        search_label=Label(main_frame, text='Search : ', font=('Orator Std',16), fg='white', bg='lightpink')
        search_label.place(x=100, y=20)


        gr_num_label=Label(main_frame, text="Gr no :  >=",font=('Orator Std',12, 'bold'), bg='lightpink')
        gr_num_label.place(x=150, y=80)
        gr_num_var=IntVar()
        gr_num_entry=Entry(main_frame, textvariable=gr_num_var, width=10)
        gr_num_entry.place(x=240, y=83)


        gr_num_label2=Label(main_frame, text="<=",font=('Orator Std',12, 'bold'), bg='lightpink')
        gr_num_label2.place(x=315, y=80)
        gr_num_var2=IntVar()
        gr_num_entry2=Entry(main_frame, font=('Orator Std',10, 'bold'), textvariable=gr_num_var2, width=10)
        gr_num_entry2.place(x=350, y=83)


        surname_label=Label(main_frame,text="Surname :", font=('Orator Std',12, 'bold'), bg='lightpink')
        surname_label.place(x=500, y=80)
        surname_var=StringVar()
        surname_entry=Entry(main_frame, font=('Orator Std',10, 'bold'),textvariable=surname_var, width=18)
        surname_entry.place(x=600, y=83)


        name_label=Label(main_frame,text="Name :", font=('Orator Std',12, 'bold'), bg='lightpink')
        name_label.place(x=800, y=80)
        name_var=StringVar()
        name_entry=Entry(main_frame, font=('Orator Std',10, 'bold'),textvariable=name_var, width=18)
        name_entry.place(x=900, y=83)


        rte_var=StringVar()
        rte_label=Label(main_frame,text="RTE", font=("Orator STD", 8, 'bold'), bg='lightpink')
        rte_label.place(x=1075, y=87)
        rte_check=Checkbutton(main_frame,bg='lightpink',textvariable=rte_var)
        rte_check.place(x=1100 , y=83)


        std_label=Label(main_frame,text="STD :", font=('Orator Std',12, 'bold'), bg='lightpink')
        std_label.place(x=170, y=130)
        std_var=StringVar()
        std_entry=Entry(main_frame, font=('Orator Std',10, 'bold'),textvariable=std_var, width=18)
        std_entry.place(x=230, y=130)


        Div_label=Label(main_frame,text="Div :", font=('Orator STD',12, 'bold'), bg='lightpink')
        Div_label.place(x=400, y=130)
        Div_var=StringVar()
        Div_entry=Entry(main_frame, font=('Orator STD',10, 'bold'),textvariable=Div_var, width=10)
        Div_entry.place(x=500, y=130)


        Roll_no_label=Label(main_frame,text="Roll no :", font=('Orator STD',12, 'bold'), bg='lightpink')
        Roll_no_label.place(x=600, y=130)
        Roll_no_var=StringVar()
        Roll_no_entry=Entry(main_frame, font=('Orator STD',10, 'bold'),textvariable=Roll_no_var, width=10)
        Roll_no_entry.place(x=700, y=130)


        Active_label=Label(main_frame,text="Active :", font=('Orator STD',12, 'bold'), bg='lightpink')
        Active_label.place(x=800, y=130)
        Active_var=StringVar()
        Active_entry=Checkbutton(main_frame,textvariable=Active_var, bg='lightpink')
        Active_entry.place(x=900, y=130)

        search_btn=Button(main_frame, text="Search",font=('Orator STD',10, 'bold'),command=search, width=10)
        search_btn.place(x=1000, y=130)

        reset_btn=Button(main_frame, text="Reset Data",font=('Orator STD',10, 'bold'), command=add_data, width=10)
        reset_btn.place(x=1100, y=130)

        tree_frame=Frame(main_frame, width=1000)
        tree_frame.place(x=100, y=200)

        scrollbary = Scrollbar(tree_frame, orient=VERTICAL)    
        scrollbary.pack(side=RIGHT, fill=Y)

        style = ttk.Style()
        style.configure("Treeview", foreground="black")
        treeview = ttk.Treeview(tree_frame, yscrollcommand=scrollbary.set,columns=("GR No", "Name", "Surname","Standard", "Division", "Roll No"), show='headings', height=22)  
        treeview.pack(fill=X)
        scrollbary.config(command=treeview.yview())

        treeview.heading("GR No", text="GR No")
        treeview.heading("Name", text="Name")
        treeview.heading("Surname", text="Surname")
        treeview.heading("Standard", text="Standard")
        treeview.heading("Division", text="Division")
        treeview.heading("Roll No", text="Roll No")


        values=[(2154, 'Prat','Chellani', 12, 'B', 24),(1616,'Kunal','Adwani', 12,'B',19),(2901, 'Yash', 'Mehta', 12, 'A', 22)]
        for i in range(len(values)):
            treeview.insert(parent='', iid=i, index='end',text='', values=values[i])
    

        top.mainloop()

    

        

    SEARCH_BTN=Button(MAIN_FRAME,text="SEARCH",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=fees_search)
    SEARCH_BTN.place(x=1100,y=420)

    







    FEES_DEPT_LABEL=Label(MAIN_FRAME,text="DEPT : ",font=('Arial', 10),bg="lightpink")
    FEES_DEPT_LABEL.place(x=50,y=10)
    FEES_DEPT_ENTRY=Entry(MAIN_FRAME,width=20)
    FEES_DEPT_ENTRY.place(x=110,y=10)

    FEES_GR_LABEL=Label(MAIN_FRAME,text="GR : ",font=('Arial', 10),bg="lightpink")
    FEES_GR_LABEL.place(x=250,y=10)
    FEES_GR_ENTRY=Entry(MAIN_FRAME,width=20,font=('Arial', 10))
    FEES_GR_ENTRY.place(x=295,y=10)

    FEES_DATE_LABEL=Label(MAIN_FRAME,text="DATE : ",font=('Arial', 10),bg="lightpink")
    FEES_DATE_LABEL.place(x=460,y=10)
    FEES_DATE_ENTRY=DateEntry(MAIN_FRAME,selectmode="day",date_pattern="dd-mm-y",width=17,font=('Arial', 10))
    FEES_DATE_ENTRY.place(x=520,y=10)


    FEES_RECEIPTNO_LABEL=Label(MAIN_FRAME,text="RECEIPT NO. : ",font=('Arial', 10),bg="lightpink")
    FEES_RECEIPTNO_LABEL.place(x=680,y=10)
    FEES_RECEIPTNO_ENTRY=Entry(MAIN_FRAME,width=20,font=('Arial', 10))
    FEES_RECEIPTNO_ENTRY.place(x=790,y=10)


    FEES_NAME_LABEL=Label(MAIN_FRAME,text="NAME : ",font=('Arial', 10),bg="lightpink")
    FEES_NAME_LABEL.place(x=50,y=50)
    FEES_NAME_ENTRY=Entry(MAIN_FRAME,width=54)
    FEES_NAME_ENTRY.place(x=110,y=50)


    FEES_RECEIPTBOOK_LABEL=Label(MAIN_FRAME,text="RECEIPT BOOK : ",font=('Arial', 10),bg="lightpink")
    FEES_RECEIPTBOOK_LABEL.place(x=680,y=50)
    FEES_RECEIPTBOOK_ENTRY=Entry(MAIN_FRAME,width=20,font=('Arial', 10))
    FEES_RECEIPTBOOK_ENTRY.place(x=790,y=50)


    FEES_STD_LABEL=Label(MAIN_FRAME,text="STD : ",font=('Arial', 10),bg="lightpink")
    FEES_STD_LABEL.place(x=50,y=90)
    FEES_STD_ENTRY=Entry(MAIN_FRAME,width=17,font=('Arial', 10))
    FEES_STD_ENTRY.place(x=110,y=90)


    FEES_DIV_LABEL=Label(MAIN_FRAME,text="DIV : ",font=('Arial', 10),bg="lightpink")
    FEES_DIV_LABEL.place(x=250,y=90)
    FEES_DIV_ENTRY=Entry(MAIN_FRAME,width=20,font=('Arial', 10))
    FEES_DIV_ENTRY.place(x=295,y=90)



    FEES_TOTALAMOUNT_LABEL=Label(MAIN_FRAME,text="TOTAL : ",font=('Arial', 10),bg="lightpink")
    FEES_TOTALAMOUNT_LABEL.place(x=80,y=460)
    FEES_TOTALAMOUNT_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_TOTALAMOUNT_ENTRY.place(x=50,y=480)

    FEES_LATEFEES_LABEL=Label(MAIN_FRAME,text="LATE FEES : ",font=('Arial', 10),bg="lightpink")
    FEES_LATEFEES_LABEL.place(x=280,y=460)
    FEES_LATEFEES_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_LATEFEES_ENTRY.place(x=250,y=480)


    EXEMPTION_LABEL=Label(MAIN_FRAME,text="EXEMPTION : ",font=('Arial', 10),bg="lightpink")
    EXEMPTION_LABEL.place(x=480,y=460)
    EXEMPTION_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    EXEMPTION_ENTRY.place(x=450,y=480)

    
    FEES_GRANDTOTAL_LABEL=Label(MAIN_FRAME,text="GRAND TOTAL : ",font=('Arial', 10),bg="lightpink")
    FEES_GRANDTOTAL_LABEL.place(x=680,y=460)
    FEES_GRANDTOTAL_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_GRANDTOTAL_ENTRY.place(x=650,y=480)






    FEES_PAYMODE_LABEL=Label(MAIN_FRAME,text="PAYMODE : ",font=('Arial', 10),bg="lightpink")
    FEES_PAYMODE_LABEL.place(x=80,y=530)
    FEES_PAYMODE_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_PAYMODE_ENTRY.place(x=50,y=550)

    FEES_BANKNAME_LABEL=Label(MAIN_FRAME,text="BANK : ",font=('Arial', 10),bg="lightpink")
    FEES_BANKNAME_LABEL.place(x=280,y=530)
    FEES_BANKNAME_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_BANKNAME_ENTRY.place(x=250,y=550)

    FEES_CHEQUENUMBER_LABEL=Label(MAIN_FRAME,text="CHEQUENO : ",font=('Arial', 10),bg="lightpink")
    FEES_CHEQUENUMBER_LABEL.place(x=480,y=530)
    FEES_CHEQUENUMBER_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_CHEQUENUMBER_ENTRY.place(x=450,y=550)

    FEES_CHEQUEDATE_LABEL=Label(MAIN_FRAME,text="CHEQUEDATE : ",font=('Arial', 10),bg="lightpink")
    FEES_CHEQUEDATE_LABEL.place(x=680,y=530)
    FEES_CHEQUEDATE_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    FEES_CHEQUEDATE_ENTRY.place(x=650,y=550)
    
    def fees_save():
        root.bell()
        fee_lst=[]
        fee_lst.append(FEES_RECEIPTNO_ENTRY.get())
        fee_lst.append(FEES_DEPT_ENTRY.get())
        fee_lst.append(FEES_GR_ENTRY.get())
        fee_lst.append(FEES_DATE_ENTRY.get())
        fee_lst.append(FEES_NAME_ENTRY.get())
        fee_lst.append(FEES_RECEIPTBOOK_ENTRY.get())
        fee_lst.append(FEES_STD_ENTRY.get())
        fee_lst.append(FEES_DIV_ENTRY.get())
        fee_lst.append(FEES_TOTALAMOUNT_ENTRY.get())
        fee_lst.append(FEES_LATEFEES_ENTRY.get())
        fee_lst.append(EXEMPTION_ENTRY.get())
        fee_lst.append(int(FEES_TOTALAMOUNT_ENTRY.get())-int(FEES_LATEFEES_ENTRY.get())-int(EXEMPTION_ENTRY.get()))
        fee_lst.append(FEES_PAYMODE_ENTRY.get())
        fee_lst.append(FEES_BANKNAME_ENTRY.get())
        fee_lst.append(FEES_CHEQUENUMBER_ENTRY.get())
        fee_lst.append(FEES_CHEQUEDATE_ENTRY.get())
        fee_lst.append(CheckVar1.get())
        fee_lst.append(CheckVar2.get())
        fee_lst.append(CheckVar3.get())
        fee_lst.append(CheckVar4.get())
        fee_lst.append(CheckVar5.get())
        cur.execute("insert into tran_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",fee_lst)
        cur.execute("insert into fee_tran values({},0,0,0,0,0)".format(FEES_RECEIPTNO_ENTRY.get()))

        if (CheckVar1.get() == 0):
            cur.execute("update gr_check set c1=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c1 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c1=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c1=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c1='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))


        if(CheckVar2.get() == 0):
            cur.execute("update gr_check set c2=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c2 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c2=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c2=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c2='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))

        if(CheckVar3.get() == 0):
            cur.execute("update gr_check set c3=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c3 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c3=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c3=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c3='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))

        if(CheckVar4.get() == 0):
            cur.execute("update gr_check set c4=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c4 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c4=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c4=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c4='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
        if(CheckVar5.get() == 0):
            cur.execute("update gr_check set c5=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c5 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c5=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c5=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c5='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))

        FEES_FUNCTION()




    def fees_generate():
        SAVE_BTN["state"]=ACTIVE



    GENERATE_BTN=Button(MAIN_FRAME,text="GENERATE",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=fees_generate)
    GENERATE_BTN.place(x=900,y=500)
    
    SHOW_BTN=Button(MAIN_FRAME,text="SHOW\nFEE DETAIL",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=fees_generate)
    SHOW_BTN.place(x=900,y=420)


    SAVE_BTN=Button(MAIN_FRAME,text="SAVE",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=fees_save)
    SAVE_BTN.place(x=1100,y=500)
    SAVE_BTN["state"]=DISABLED



















def FEES_EDIT_FUNCTION():
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy() 
    # text_Q1="FEES EDIT"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\fees_edit.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\fees_edit.mp3")
    #pygame.mixer.music.play(loops=0)

    MAIN_FRAME.configure(bg="#dda0dd")

    standard_select_lbl=Label(MAIN_FRAME,text="Select Standard :",padx=5,pady=5,bg="#dda0dd",font=("Arial",10,"bold"))
    standard_select_lbl.place(x=50,y=105)
    standard_select_var=StringVar()
    standard_select_combo = ttk.Combobox(MAIN_FRAME,width=20,textvariable = standard_select_var,font=("Arial",10,"bold"))
    standard_select_combo['values'] = ('Nursery','1','2','3','4','5','6','7','8','9','10','11 Comm','11 Sci','12 Comm','12 Sci')
 
    standard_select_combo.place(x=200,y=110)


    fees_frame = Frame(MAIN_FRAME, bg="#dda0dd", width=500, height=250,relief=RIDGE)
    fees_frame.place(x=500, y=100)




    def next():
        s = standard_select_combo.get()
        fees_select_label = Label(fees_frame,text="Select Fees :",padx=5,pady=5,bg="#dda0dd",font=("Arial",10,"bold"))
        fees_select_label.place(x=100,y=20)
        fees_select_combo = ttk.Combobox(fees_frame,width=20,font=("Arial",10,"bold"))
        fees_select_combo['values'] = ('a')

        def selected(event):
            SAVE_BTN["state"]=ACTIVE
            if fees_select_combo.get() == 'a':
                old_fees_amount_entry.configure(state = "normal")
                old_fees_amount_entry.delete(0,END)
                old_fees_amount_entry.insert(0,"100")
                old_fees_amount_entry.configure(state = "disabled")
                new_fees_amount_entry.delete(0,END)
                new_fees_amount_entry.insert(0,"100")
            
            # elif:





        fees_select_combo.bind('<<ComboboxSelected>>',selected)
        fees_select_combo.place(x=200,y=20)


        old_fees_amount_label = Label(fees_frame,text="Old Amount :",padx=5,pady=5,bg="#dda0dd",font=("Arial",10,"bold"))
        old_fees_amount_label.place(x=98,y=100)
        old_fees_amount_entry = Entry(fees_frame,width=22,font=("Arial",10,"bold"),state='disabled')
        old_fees_amount_entry.place(x=200,y=100)

        new_fees_amount_label = Label(fees_frame,text="New Amount :",padx=5,pady=5,bg="#dda0dd",font=("Arial",10,"bold"))
        new_fees_amount_label.place(x=94,y=150)
        new_fees_amount_entry = Entry(fees_frame,width=22,font=("Arial",10,"bold"))
        new_fees_amount_entry.place(x=200,y=150)




    SUBMIT_BTN=Button(MAIN_FRAME,text="Submit",height=1,width=19,bg="lightgrey",activebackground='lightgrey',font=('Arial', 10),command=next)
    SUBMIT_BTN.place(x=200,y=160)

    SAVE_BTN=Button(MAIN_FRAME,text="SAVE",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 10))
    SAVE_BTN.place(x=1100,y=500)
    SAVE_BTN["state"]=DISABLED








def FEES_REPORT_FUNCTION():
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy() 

    # text_Q1="FEES REPORT"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\fees_report.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\fees_report.mp3")
    #pygame.mixer.music.play(loops=0)

    MAIN_FRAME.configure(bg="#dda0dd")










def LIBRARY_FUNCTION():
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy()  
    # text_Q1="LIBRARY"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\library.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\library.mp3")
    #pygame.mixer.music.play(loops=0)



def CERTIFICATES_FUNCTION():
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy()
    # text_Q1="CERTIFICATES"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\certificates.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\certificates.mp3")
    #pygame.mixer.music.play(loops=0)

    MAIN_FRAME.configure(bg="#dda0dd")

    # bonafied_frame=Frame(MAIN_FRAME,height=350,width=650,background="#dda0dd")
    # bonafied_frame.place(x=335,y=125)

    #-------------------------LABELS---------------------------------

    numlbl=Label(MAIN_FRAME,text="No. : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    numlbl.place(x=340,y=150,anchor=E)

    dtlbl=Label(MAIN_FRAME,text="Date : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    dtlbl.place(x=340,y=200,anchor=E)

    grnlbl=Label(MAIN_FRAME,text="Gr No : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    grnlbl.place(x=340,y=250,anchor=E)

    namelbl=Label(MAIN_FRAME,text="Name : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    namelbl.place(x=340,y=300,anchor=E)

    remarklbl=Label(MAIN_FRAME,text="Remark : ",bg='#dda0dd',font=("ariel", 15, "bold"))
    remarklbl.place(x=340,y=350,anchor=E)

    stdlbl=Label(MAIN_FRAME,text="Standard :",bg="#dda0dd",font=("ariel", 15, "bold"))
    stdlbl.place(x=780,y=200,anchor=E)

    divlbl=Label(MAIN_FRAME,text="Division :",bg="#dda0dd",font=("ariel", 15, "bold"))
    divlbl.place(x=780,y=250,anchor=E)

    # #-------------------------------ENTRY TABS----------------------------------

    num_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    num_entry_tab.place(x=350,y=135)

    #dt_entry_tab=Entry(MAIN_FRAME)
    #dt_entry_tab.place(x=90,y=70)

    dt_entry_tab=DateEntry(MAIN_FRAME,selectmode="day",date_pattern="dd-mm-y",font=("ariel", 15, "bold"),width=18)
    dt_entry_tab.place(x=350,y=185)

    grn_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    grn_entry_tab.place(x=350,y=235)

    name_entry_tab=Entry(MAIN_FRAME,width=60,font=("ariel", 15, "bold"))
    name_entry_tab.place(x=350,y=285)

    remark_entry_tab=Entry(MAIN_FRAME,width=60,font=("ariel", 15, "bold"))
    remark_entry_tab.place(x=350,y=335)

    std_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    std_entry_tab.place(x=790,y=185)

    div_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    div_entry_tab.place(x=790,y=235)


def BACKUP_FUNCTION():
    pass
    # text_Q1="backed up succesfully"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\backup.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\backup.mp3")
    #pygame.mixer.music.play(loops=0)

def ABOUTUS_FUNCTION():
    # text_Q1="School Details"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\schooldetails.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\schooldetails.mp3")
    #pygame.mixer.music.play(loops=0)
    root1=Toplevel()
    root1.title("ZETA CORE")
    photo = PhotoImage(file = r"ICONS\Zeta.png")
    root1.iconphoto(False, photo)
    root1.geometry("500x700")
    root1.maxsize(500, 700)
    root1.configure(bg="lightgrey")


    def WHATSAPP_FUNCTION():
        url='http://web.whatsapp.in/'
        webbrowser.open_new_tab(url)
    def FACEBOOK_FUNCTION():
        url='https://www.facebook.com/airportschoolahmedabad?mibextid=ZbWKwL'
        webbrowser.open_new_tab(url)
    def YOUTUBE_FUNCTION():
        url='https://youtube.com/@AirportSchoolAhmedabad'
        webbrowser.open_new_tab(url)
    def TWITTER_FUNCTION():
        url='https://twitter.com/airportschahm'
        webbrowser.open_new_tab(url)


    image_schl_logo= Image.open(r"ICONS\school_logo.png")
    img_schl_logo=image_schl_logo.resize((130,130))
    photo_schl_logo= ImageTk.PhotoImage(img_schl_logo)
    LBL_SCHL_LOGO=Label(root1,image=photo_schl_logo,bg="lightgrey")
    LBL_SCHL_LOGO.place(x=170,y=20)

    aff_lbl=Label(root1,bg='lightgrey',text="Affiliation No : 430133", font=("Arial Rounded MT Bold",10))
    aff_lbl.place(x=180,y=150)

    bank_frame=LabelFrame(root1,width=480,text="Bank Details",height=150,bg="lightgrey")
    bank_frame.place(x=10,y=190)
    bank_ent=Text(bank_frame,bg='lightgrey',width=59,height=8, font=("Arial Rounded MT Bold",10),relief=FLAT)
    bank_ent.tag_configure('A/c Name : Airport School Association\nA/c No : 66510200000026\nIFSC Code : BARB0VJDAPB(Fifth digit is "0"zero)\nMICR Code : 380012193\nBank Name : Bank of Baroda\nBranch : Airport Domestic Terminal Branch,\nSVPI Airport, Ahmedabad\nUPI id : airpo9904904175@barodampay', justify='center')
    bank_ent.insert(1.0,'A/c Name : Airport School Association\nA/c No : 66510200000026\nIFSC Code : BARB0VJDAPB(Fifth digit is "0"zero)\nMICR Code : 380012193\nBank Name : Bank of Baroda\nBranch : Airport Domestic Terminal Branch,\nSVPI Airport, Ahmedabad\nUPI id : airpo9904904175@barodampay')
    bank_ent.tag_add('A/c Name : Airport School Association\nA/c No : 66510200000026\nIFSC Code : BARB0VJDAPB(Fifth digit is "0"zero)\nMICR Code : 380012193\nBank Name : Bank of Baroda\nBranch : Airport Domestic Terminal Branch,\nSVPI Airport, Ahmedabad\nUPI id : airpo9904904175@barodampay', "1.0", "end")
    bank_ent['state']=DISABLED
    bank_ent.place(x=0,y=0)
    # bank_lbl=Label(bank_frame,bg='lightgrey',text='A/c Name : Airport School Association\nA/c No : 66510200000026\nIFSC Code : BARB0VJDAPB(Fifth digit is "0"zero)\nMICR Code : 380012193\n Bank Name : Bank of Baroda\n Branch : Airport Domestic Terminal Branch,\nSVPI Airport, Ahmedabad\nUPI id : airpo9904904175@barodampay', font=("Arial Rounded MT Bold",10))
    # bank_lbl.place(x=100,y=5)

    address_frame=LabelFrame(root1,width=480,text="Address",height=100,bg="lightgrey")
    address_frame.place(x=10,y=350)
    address_ent=Text(address_frame,bg='lightgrey',width=59,height=4, font=("Arial Rounded MT Bold",10),relief=FLAT)
    address_ent.tag_configure('Airport School Ahmedabad,\n AAI Residential Quarters,\n Opp. S.V.P. International Airport,\n Sardarnagar, Ahmedabad–382475', justify='center')
    address_ent.insert(1.0,'Airport School Ahmedabad,\n AAI Residential Quarters,\n Opp. S.V.P. International Airport,\n Sardarnagar, Ahmedabad–382475')
    address_ent.tag_add("Airport School Ahmedabad,\n AAI Residential Quarters,\n Opp. S.V.P. International Airport,\n Sardarnagar, Ahmedabad–382475", "1.0", "end")
    address_ent['state']=DISABLED
    address_ent.place(x=0,y=0)
    # add_lbl=Label(address_frame,bg='lightgrey',text="Airport School Ahmedabad,\n AAI Residential Quarters,\n Opp. S.V.P. International Airport,\n Sardarnagar, Ahmedabad–382475", font=("Arial Rounded MT Bold",10))
    # add_lbl.place(x=100,y=5)

    contact_frame=LabelFrame(root1,width=480,text="Contact Details",height=100,bg="lightgrey")
    contact_frame.place(x=10,y=460)
    contact_ent=Text(contact_frame,bg='lightgrey',width=59,height=4, font=("Arial Rounded MT Bold",10),relief=FLAT)
    contact_ent.tag_configure("Phone No : 079 – 22864175 ,\n079 – 22869014 ,\n+91-99049-04175\nEmail Address : info@airportschoolahm.in", justify='center')
    contact_ent.insert(1.0,'Phone No : 079 – 22864175 ,\n079 – 22869014 ,\n+91-99049-04175\nEmail Address : info@airportschoolahm.in')
    contact_ent.tag_add("Phone No : 079 – 22864175 ,\n079 – 22869014 ,\n+91-99049-04175\nEmail Address : info@airportschoolahm.in", "1.0", "end")
    contact_ent['state']=DISABLED
    contact_ent.place(x=0,y=0)
    # contact_lbl=Label(contact_frame,bg='lightgrey',text='Phone No : 079 – 22864175 ,\n079 – 22869014 ,\n+91-99049-04175\n Email Address : info@airportschoolahm.in', font=("Arial Rounded MT Bold",10))
    # contact_lbl.place(x=100,y=5)





    image_whatsapp= Image.open(r"ICONS\wp.png")
    image_whatsapp= image_whatsapp.resize((45,45))
    img_whatsapp= ImageTk.PhotoImage(image_whatsapp)
    WHATSAPP_BTN=Button(root1,bg="lightgrey",image = img_whatsapp,compound=TOP,text="WHATSAPP",command=WHATSAPP_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
    WHATSAPP_BTN.place(x=80,y=580)

    image_facebook= Image.open(r"ICONS\fb.png")
    image_facebook= image_facebook.resize((45,45))
    img_facebook= ImageTk.PhotoImage(image_facebook)
    FACEBOOK_BTN=Button(root1,bg="lightgrey",image = img_facebook,compound=TOP,text="FACEBOOK",command=FACEBOOK_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
    FACEBOOK_BTN.place(x=160,y=580)

    image_youtube= Image.open(r"ICONS\yt.png")
    image_youtube= image_youtube.resize((45,45))
    img_youtube= ImageTk.PhotoImage(image_youtube)
    YOUTUBE_BTN=Button(root1,bg="lightgrey",image = img_youtube,compound=TOP,text="YOUTUBE",command=YOUTUBE_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
    YOUTUBE_BTN.place(x=240,y=580)


    image_twitter= Image.open(r"ICONS\twitter.png")
    image_twitter= image_twitter.resize((45,45))
    img_twitter= ImageTk.PhotoImage(image_twitter)
    TWITTER_BTN=Button(root1,bg="lightgrey",image = img_twitter,compound=TOP,text="TWITTER",command=TWITTER_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
    TWITTER_BTN.place(x=320,y=580)


    root1.mainloop()

def SCHL_FUNCTION():
    # text_Q1="AIRPORT SCHOOL AHMEDABAD"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\SCHL.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\SCHL.mp3")
    #pygame.mixer.music.play(loops=0)
    url='http://airportschoolahm.in/'
    webbrowser.open_new_tab(url)


def BANK_FUNCTION():
    top=Toplevel()
    top.geometry("1400x600")
    top.title("ZETA CORE")
    photo = PhotoImage(file = r"ICONS\Zeta.png")
    top.iconphoto(False, photo)
    top.mainloop()


def EXIT_FUNCTION():
    # text_Q1="Good bye "
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\exit.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\exit.mp3")
    #pygame.mixer.music.play(loops=0)
    time.sleep(1)
    # text_Q1="HAVE A NICE DAY"
    # myobj = gTTS(text=text_Q1, slow=False)
    # myobj.save(r"AUDIOS\exit1.mp3")
    #pygame.mixer.init()
    #pygame.mixer.music.load(r"AUDIOS\exit1.mp3")
    #pygame.mixer.music.play(loops=0)
    time.sleep(3)

    root.destroy()


#---------------------------------------------------------------------------------------------------------


MENU_FRAME=Frame(root,relief=RIDGE,bg="lightgrey",height=100,width=1550,borderwidth=5)
MENU_FRAME.place(x=0,y=0)

#---------------------------------------------------------------------------------------------------------

MENU_FRAME2=Frame(root,relief=RIDGE,bg="lightgrey",height=700,width=100,borderwidth=1)
MENU_FRAME2.place(x=0,y=100)


#---------------------------------------------------------------------------------------------------------


MAIN_FRAME=Frame(root,relief=RIDGE,bg="white",height=600,width=1320,borderwidth=4) 
MAIN_FRAME.place(x=150,y=150)

#---------------------------------------------------------------------------------------------------------




image_gr= Image.open(r"ICONS\gr.png")
image_gr= image_gr.resize((55,55))
img_gr= ImageTk.PhotoImage(image_gr)
GR_BTN=Button(MENU_FRAME,image = img_gr,bg='lightgrey',compound=TOP,text="GR",command=GR_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
GR_BTN.place(x=200,y=0)


image_fees= Image.open(r"ICONS\fees.png")
image_fees= image_fees.resize((55,55))
img_fees= ImageTk.PhotoImage(image_fees)
FEES_BTN=Button(MENU_FRAME,image = img_fees,bg='lightgrey',compound=TOP,text="FEES",command=FEES_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
FEES_BTN.place(x=300,y=0) 


image_fees_edit= Image.open(r"ICONS\edity1.png")
image_fees_edit= image_fees_edit.resize((55,55))
img_fees_edit= ImageTk.PhotoImage(image_fees_edit)
FEES_EDIT_BTN=Button(MENU_FRAME,image = img_fees_edit,bg='lightgrey',compound=TOP,text="FEES EDIT",command=FEES_EDIT_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
FEES_EDIT_BTN.place(x=400,y=0) 



image_fees_report= Image.open(r"ICONS\fee_report.png")
image_fees_report= image_fees_report.resize((55,55))
img_fees_report= ImageTk.PhotoImage(image_fees_report)
FEES_REPORT_BTN=Button(MENU_FRAME,image = img_fees_report,bg='lightgrey',compound=TOP,text="FEES REPORT",command=FEES_REPORT_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
FEES_REPORT_BTN.place(x=490,y=0) 



image_library= Image.open(r"ICONS\Library.png")
image_library= image_library.resize((55,55))
img_library= ImageTk.PhotoImage(image_library)
LIBRARY_BTN=Button(MENU_FRAME,image = img_library,bg='lightgrey',compound=TOP,text="LIBRARY",command=LIBRARY_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
LIBRARY_BTN.place(x=590,y=0)



image_certificate= Image.open(r"ICONS\certificate.png")
image_certificate= image_certificate.resize((55,55))
img_certificate= ImageTk.PhotoImage(image_certificate)
CERTIFICATES_BTN=Button(MENU_FRAME,image = img_certificate,bg='lightgrey',compound=TOP,text="CERTIFICATES",command=CERTIFICATES_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
CERTIFICATES_BTN.place(x=680,y=0)



image_backup= Image.open(r"ICONS\backup.png")
image_backup= image_backup.resize((55,55))
img_backup= ImageTk.PhotoImage(image_backup)
BACKUP_BTN=Button(MENU_FRAME,image = img_backup,bg='lightgrey',compound=TOP,text="BACKUP",command=BACKUP_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
BACKUP_BTN.place(x=780,y=0)



image_aboutus= Image.open(r"ICONS\about us.png")
image_aboutus= image_aboutus.resize((50,55))
img_aboutus= ImageTk.PhotoImage(image_aboutus)
ABOUTUS_BTN=Button(MENU_FRAME,image = img_aboutus,bg='lightgrey',compound=TOP,text="DETAILS",command=ABOUTUS_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
ABOUTUS_BTN.place(x=870,y=0)



image_exit= Image.open(r"ICONS\EXIT_menu.png")
image_exit= image_exit.resize((55,55))
img_exit= ImageTk.PhotoImage(image_exit)
EXIT_BTN=Button(MENU_FRAME,image = img_exit,bg='lightgrey',compound=TOP,text="EXIT",command=EXIT_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
EXIT_BTN.place(x=960,y=0)



image_schl_logo= Image.open(r"ICONS\school_logo.png")
img_schl_logo=image_schl_logo.resize((85,85))
photo_schl_logo= ImageTk.PhotoImage(img_schl_logo)
SCHL_BTN=Button(MENU_FRAME,image = photo_schl_logo,bg='lightgrey',compound=TOP,command=SCHL_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
SCHL_BTN.place(x=0,y=0)




DATElbl=Label(MENU_FRAME,text="Date : ",bg='light grey',fg='#151B54',font=("Copperplate Gothic Bold",12))
DATElbl.place(x=1150, y=60)

label_date_now = Label(MENU_FRAME,text="Current Date",bg='light grey',fg='#151B54',font=("Copperplate Gothic Bold",12))
label_date_now.place(x=1210, y=60)

TIMElbl=Label(MENU_FRAME,text="Time : ",bg='light grey',fg='#151B54',font=("Copperplate Gothic Bold",12))
TIMElbl.place(x=1330, y=60)

label_time_now = Label(MENU_FRAME,text="Current Time",bg='lightgrey',fg='#151B54',font=("Copperplate Gothic Bold",12))
label_time_now.place(x=1390, y=60)

def y():
    current_date=datetime.datetime.today().strftime('%d-%m-%y')
    current_time=datetime.datetime.now().strftime('%H:%M:%S %p')
    label_date_now.config(text=current_date)
    label_time_now.config(text=current_time)
    label_time_now.after(100,y)
y()





root.mainloop()
