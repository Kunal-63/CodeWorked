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
from gtts import gTTS
from tkVideoPlayer import TkinterVideo
import csv
import time
from tkhtmlview import HTMLLabel
import webbrowser

video =Tk()
video.geometry("1000x600")
video.title("ZETA CORE")
photo = PhotoImage(file = r"ICONS\Zeta.png")
video.iconphoto(False, photo)
video.resizable(False, False)
videoplayer = TkinterVideo(master=video, scaled=True)
videoplayer.load(r"VIDEOS\ZETACORE.mp4")
videoplayer.set_size(size=(1000, 600), keep_aspect=False)
videoplayer.pack(expand=True, fill="both")
videoplayer.play()
def video_ended(event):
    # print("video ended")
    duration_video = videoplayer.current_duration()
    # print(f"video duration: {duration_video}")
    if(duration_video == 14.833333333333334):
        video.destroy()
videoplayer.bind("<<Ended>>", video_ended )
video.mainloop()




















mydb = con.connect(host="localhost",user="root",password="Mouse@2010",database="airport_school1")
cur = mydb.cursor()
root=Tk()
root.state('zoomed')
root.geometry("1000x500")
# root.attributes('-fullscreen', True)
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
                cur.execute("select * from std_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("insert into pending_fee_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[Gr_entry.get(),data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12]])
            cur.execute("insert into gr_check values({},0,0,0,0,0,0,0)".format(Gr_entry.get()))
            cur.execute("insert into fee_details values({},' ',' ',' ',' ',' ',' ',' ')".format(Gr_entry.get()))
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
            # cur.execute("select GRNO,NAME,CURRENT_STANDARD,division from academic_details")
            # aca_data = cur.fetchall()
            # cur.execute("insert into fee(GR,NAME,STD,division) values(%s,%s,%s,%s)",[aca_data[0][0],aca_data[0][1],aca_data[0][2],aca_data[0][3]])
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

        def edit_keybinding(e):
            def edit_insert():
                form_no_ent.delete(0,END)
                form_no_ent.insert(0,data[0][1])  
                enquiry_no_ent.delete(0,END)
                enquiry_no_ent.insert(0,data[0][2]) 
                uid_ent.delete(0,END)
                uid_ent.insert(0,data[0][3])
                surname_ent.delete(0,END)
                surname_ent.insert(0,data[0][4])
                name_ent.delete(0,END)
                name_ent.insert(0,data[0][5])
                father_ent.delete(0,END)
                father_ent.insert(0,data[0][6])
                mother_ent.delete(0,END)
                mother_ent.insert(0,data[0][7])
                sex_combo.delete(0,END)
                sex_combo.insert(0,data[0][8])
                birth_date_ent.delete(0,END)
                birth_date_ent.insert(0,data[0][9])
                category_combo.delete(0,END)
                category_combo.insert(0,data[0][10])
                religion_combo.delete(0,END)
                religion_combo.insert(0,data[0][11])
                birth_place_ent.delete(0,END)
                birth_place_ent.insert(0,data[0][12])
                previous_school_ent.delete(0,END)
                previous_school_ent.insert(0,data[0][13])
                caste_combo.delete(0,END)
                caste_combo.insert(0,data[0][14])
                birth_taluka_ent.delete(0,END)
                birth_taluka_ent.insert(0,data[0][15])
                subcaste_combo.delete(0,END)
                subcaste_combo.insert(0,data[0][16])
                state_ent.delete(0,END)
                state_ent.insert(0,data[0][17])
                if (data[0][18]==0):
                    minority_check.deselect()
                else:
                    minority_check.select()
                if(data[0][19] == 0):
                    rte_check.deselect()
                else:
                    rte_check.select()


            data = cur.execute("select * from gr_details where gr_no={}".format(gr_ent.get()))
            data = cur.fetchall()
            global edit_gr_details
            edit_gr_details = data[0][0]
            edit_insert()
        gr_ent.bind('<Return>',edit_keybinding)


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
        save_next_button.place(x=1050,y=370)

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
        addmission_standard_ent.set(data[0][8])

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
        current_standard_ent.set(data[0][11])

        division_lbl=Label(academic_frame1,text="Division :",padx=5,pady=5,font=("Arieal",10,"bold"),bg="lightblue")
        division_lbl.place(x=75,y=340)
        division_var=StringVar()
        division_ent=ttk.Combobox(academic_frame1,textvariable=division_var,width=8)
        division_ent['values']=['A','B','C','D','E']
        division_ent.place(x=150,y=345)
        division_ent.delete(0,END)
        division_ent.set(data[0][12])

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
            cur.execute("update academic_detail set name=%s,active1=%s,left1=%s,aai1=%s,inactive_date=%s,add_date=%s,add_year=%s,add_std=%s,curr_date=%s,curr_year=%s,curr_std=%s,division=%s,roll_no=%s,inactive_reason=%s,left_reason=%s,progress=%s,presence=%s,out_of=%s,lc_book=%s,lc_no=%s,lc_date=%s,lc_remark=%s,lc_copy=%s where gr_no=%s",academic_details_lst)
            
            if(aaivalue.get() == 0):
                cur.execute("select * from std_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("update pending_fee_detail set ADMISSION_FEE=%s,ICARD=%s,APR_JUN_TUTION=%s,APR_JUN_ATITVITY=%s,LATE_FEES=%s,JUL_SEP_TUTION=%s,JUL_SEP_ACTIVITY=%s,OCT_DEC_TUTION=%s,OCT_DEC_ACTIVITY=%s,JAN_MAR_TUTION=%s,JAN_MAR_ACTIVITY=%s,OTHERS=%s where GR_NO=%s",[data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12],Gr_entry.get()])
            else:
                cur.execute("select * from STD_fees where std='{}'".format(current_standard_ent.get()))
                data = cur.fetchall()
                cur.execute("update pending_fee_detail set ADMISSION_FEE=%s,ICARD=%s,APR_JUN_TUTION=%s,APR_JUN_ATITVITY=%s,LATE_FEES=%s,JUL_SEP_TUTION=%s,JUL_SEP_ACTIVITY=%s,OCT_DEC_TUTION=%s,OCT_DEC_ACTIVITY=%s,JAN_MAR_TUTION=%s,JAN_MAR_ACTIVITY=%s,OTHERS=%s where GR_NO=%s",[data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12],Gr_entry.get()])
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

    def gr_delete1():
        for widget in MAIN_FRAME_0.winfo_children():
            widget.destroy()
        gr_details_BTN["state"]="disable"
        academic_details_BTN["state"]="disable"
        other_details_BTN["state"]="disable"

        Gr_label_delete = Label(MAIN_FRAME_0, text="GR NO : ", font=('Monteserrat', 20, 'bold'), fg="black", bg="lightblue")
        Gr_label_delete.place(x=400, y=200)
        Gr_var_delete=StringVar()
        Gr_entry_delete= Entry(MAIN_FRAME_0, textvariable=Gr_var_delete, width=10, font=('Monteserrat', 20, 'bold'))
        Gr_entry_delete.place(x=520, y=200)

        def delete_main():
            gr_deleting = Gr_var_delete.get()
            cur.execute("select gr_no from gr_details")
            data = cur.fetchall()

            found = False
            for i in data:
                if(i[0] == int(gr_deleting)):
                    found = True
            if found==False:
                messagebox.showerror("ERROR","GR not found")
            else:
                try:
                    cur.execute("delete from gr_details where GR_NO={}".format(int(gr_deleting)))
                except:
                    pass
                try:
                    cur.execute("update academic_detail set active1=0 where GR_NO={}".format(int(gr_deleting)))
                except:
                    pass
                try:
                    cur.execute("delete from other_detail where GR_NO={}".format(int(gr_deleting)))
                except:
                    pass
                # try:
                #     cur.execute("delete from gr_check where GR_NO={}".format(int(gr_deleting)))
                # except:
                #     pass
                # try:
                #     cur.execute("delete from pending_fee_detail where GR_NO={}".format(int(gr_deleting)))
                # except:
                #     pass
                mydb.commit()
                messagebox.showinfo("Info","GR deleted successfully")
            Gr_entry_delete.delete(0,END)
            

        save_delete_button = Button(MAIN_FRAME_0,text="Delete",font=("Arial",20), command=delete_main)
        save_delete_button.place(x=1100,y=470)



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
    GR_DELETE_BTN=Button(MENU_FRAME2,text=r"DELETE",image=img_delete,compound=TOP,command=gr_delete1, bg="lightgrey", relief=FLAT)
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

    def receipt_delete_function():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()

        def receipt_searching(event):
            rec_no = FEES_RECEIPTNO_ENTRY1.get()
            cur.execute("select * from tran_details where RECEIPT_NO={}".format(int(rec_no)))
            data = cur.fetchall()[0]
            FEES_GR_ENTRY.delete(0,END)
            FEES_GR_ENTRY.insert(0,data[2])
            FEES_NAME_ENTRY.delete(0,END)
            FEES_NAME_ENTRY.insert(0,data[4])
            FEES_RECEIPTBOOK_ENTRY.delete(0,END)
            FEES_RECEIPTBOOK_ENTRY.insert(0,data[5])
            FEES_STD_ENTRY.delete(0,END)
            FEES_STD_ENTRY.insert(0,data[6])
            FEES_DIV_ENTRY.delete(0,END)
            FEES_DIV_ENTRY.insert(0,data[7])
            FEES_LATEFEES_ENTRY.delete(0,END)
            FEES_LATEFEES_ENTRY.insert(0,data[9])
            FEES_TOTALAMOUNT_ENTRY.delete(0,END)
            FEES_TOTALAMOUNT_ENTRY.insert(0,data[8])
            EXEMPTION_ENTRY.delete(0,END)
            EXEMPTION_ENTRY.insert(0,data[10])
            FEES_GRANDTOTAL_ENTRY.delete(0,END)
            FEES_GRANDTOTAL_ENTRY.insert(0,data[11])
            FEES_PAYMODE_ENTRY.delete(0,END)
            FEES_PAYMODE_ENTRY.insert(0,data[12])
            FEES_BANKNAME_ENTRY.delete(0,END)
            FEES_BANKNAME_ENTRY.insert(0,data[13])
            FEES_CHEQUEDATE_ENTRY.delete(0,END)
            FEES_CHEQUEDATE_ENTRY.insert(0,data[15])
            FEES_CHEQUENUMBER_ENTRY.delete(0,END)
            FEES_CHEQUENUMBER_ENTRY.insert(0,data[14])
            if(int(data[16])==1):
                C1.select()
            else:
                C1.deselect()
            if(int(data[17])==1):
                C2.select()
            else:
                C2.deselect()
            if(int(data[18])==1):
                C3.select()
            else:
                C3.deselect()
            if(int(data[19])==1):
                C4.select()
            else:
                C4.deselect()
            if(int(data[20])==1):
                C5.select()
            else:
                C5.deselect()
            if(int(data[21])==1):
                C6.select()
            else:
                C6.deselect()
            if(int(data[22])==1):
                C7.select()
            else:
                C7.deselect()
            



        FEES_RECEIPTNO_LABEL1=Label(MAIN_FRAME,text="RECEIPT NO. : ",font=('Arial', 13),bg="lightpink")
        FEES_RECEIPTNO_LABEL1.place(x=70,y=30)
        FEES_RECEIPTNO_ENTRY1=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_RECEIPTNO_ENTRY1.place(x=220,y=30)
        FEES_RECEIPTNO_ENTRY1.bind("<Return>",receipt_searching)


        FEES_GR_LABEL=Label(MAIN_FRAME,text="GR : ",font=('Arial', 13),bg="lightpink")
        FEES_GR_LABEL.place(x=70,y=80)
        FEES_GR_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_GR_ENTRY.place(x=220,y=80)

        FEES_NAME_LABEL=Label(MAIN_FRAME,text="NAME : ",font=('Arial', 13),bg="lightpink")
        FEES_NAME_LABEL.place(x=70,y=130)
        FEES_NAME_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_NAME_ENTRY.place(x=220,y=130)


        FEES_RECEIPTBOOK_LABEL=Label(MAIN_FRAME,text="RECEIPT BOOK : ",font=('Arial', 13),bg="lightpink")
        FEES_RECEIPTBOOK_LABEL.place(x=70,y=180)
        FEES_RECEIPTBOOK_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_RECEIPTBOOK_ENTRY.place(x=220,y=180)


        FEES_STD_LABEL=Label(MAIN_FRAME,text="STD : ",font=('Arial', 13),bg="lightpink")
        FEES_STD_LABEL.place(x=70,y=230)
        FEES_STD_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_STD_ENTRY.place(x=220,y=230)


        FEES_DIV_LABEL=Label(MAIN_FRAME,text="DIV : ",font=('Arial', 13),bg="lightpink")
        FEES_DIV_LABEL.place(x=70,y=280)
        FEES_DIV_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_DIV_ENTRY.place(x=220,y=280)


        FEES_LATEFEES_LABEL=Label(MAIN_FRAME,text="LATE FEES : ",font=('Arial', 13),bg="lightpink")
        FEES_LATEFEES_LABEL.place(x=70,y=330)
        FEES_LATEFEES_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_LATEFEES_ENTRY.place(x=220,y=330)






        FEES_TOTALAMOUNT_LABEL=Label(MAIN_FRAME,text="TOTAL : ",font=('Arial', 13),bg="lightpink")
        FEES_TOTALAMOUNT_LABEL.place(x=400,y=30)
        FEES_TOTALAMOUNT_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_TOTALAMOUNT_ENTRY.place(x=550,y=30)



        EXEMPTION_LABEL=Label(MAIN_FRAME,text="EXEMPTION : ",font=('Arial', 13),bg="lightpink")
        EXEMPTION_LABEL.place(x=400,y=80)
        EXEMPTION_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        EXEMPTION_ENTRY.place(x=550,y=80)
        

        FEES_GRANDTOTAL_LABEL=Label(MAIN_FRAME,text="GRAND TOTAL : ",font=('Arial', 13),bg="lightpink")
        FEES_GRANDTOTAL_LABEL.place(x=400,y=130)
        FEES_GRANDTOTAL_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_GRANDTOTAL_ENTRY.place(x=550,y=130)




        FEES_PAYMODE_LABEL=Label(MAIN_FRAME,text="PAYMODE : ",font=('Arial', 13),bg="lightpink")
        FEES_PAYMODE_LABEL.place(x=400,y=180)
        FEES_PAYMODE_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_PAYMODE_ENTRY.place(x=550,y=180)

        FEES_BANKNAME_LABEL=Label(MAIN_FRAME,text="BANK : ",font=('Arial', 13),bg="lightpink")
        FEES_BANKNAME_LABEL.place(x=400,y=230)
        FEES_BANKNAME_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_BANKNAME_ENTRY.place(x=550,y=230)

        FEES_CHEQUENUMBER_LABEL=Label(MAIN_FRAME,text="CHEQUENO : ",font=('Arial', 13),bg="lightpink")
        FEES_CHEQUENUMBER_LABEL.place(x=400,y=280)
        FEES_CHEQUENUMBER_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_CHEQUENUMBER_ENTRY.place(x=550,y=280)

        FEES_CHEQUEDATE_LABEL=Label(MAIN_FRAME,text="CHEQUEDATE : ",font=('Arial', 13),bg="lightpink")
        FEES_CHEQUEDATE_LABEL.place(x=400,y=330)
        FEES_CHEQUEDATE_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 13))
        FEES_CHEQUEDATE_ENTRY.place(x=550,y=330)



        wrapper2=Frame(MAIN_FRAME,bg="lightpink",height=380 ,width=270,relief=RIDGE,borderwidth=2)
        wrapper2.place(x=800,y=30)


        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        # CheckVar8 = IntVar()
        

        C1 = Checkbutton(wrapper2, text = "APR JUN FEES", variable = CheckVar1,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C2 = Checkbutton(wrapper2, text = "JUL SEP FEES", variable = CheckVar2,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C3 = Checkbutton(wrapper2, text = "OCT DEC FEES", variable = CheckVar3,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C4 = Checkbutton(wrapper2, text = "JAN MAR FEES", variable = CheckVar4,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C5 = Checkbutton(wrapper2, text = "OTHERS", variable = CheckVar5,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C6 = Checkbutton(wrapper2, text = "ADMISSION FEE", variable = CheckVar6,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C7 = Checkbutton(wrapper2, text = "ICARD", variable = CheckVar7,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        # C8 = Checkbutton(wrapper2, text = "LATE FEE", variable = CheckVar8,onvalue = 1, offvalue = 0, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        
        C1.place(x=0,y=0)
        C2.place(x=0,y=45)
        C3.place(x=0,y=90)
        C4.place(x=0,y=135)
        C5.place(x=0,y=180)
        C6.place(x=0,y=225)
        C7.place(x=0,y=270)
        # C8.place(x=0,y=315)

        def receipt_delete():
            passroot = Tk()
            passroot.title("PASSWORD")
            passroot.geometry("300x200")
            passroot.resizable(0,0)
            Label(passroot,text="ENTER PASSWORD",font=('Arial', 13)).place(x=80,y=20)
            pass_entry=Entry(passroot,width=14,show="*",font=('Arial', 13))
            pass_entry.place(x=80,y=60)
            def pass_check():
                val = pass_entry.get()
                if(val == "Admin@321"):
                    abc1()
                else:
                    messagebox.showerror("ERROR","WRONG PASSWORD")
            submit_button=Button(passroot,text="SUBMIT",font=('Arial', 13),command=pass_check)
            submit_button.place(x=120,y=100)

            global abc1
            def abc1():
                passroot.destroy()
                cur.execute("select * from std_fees where STD='{}'".format(FEES_STD_ENTRY.get()))
                
                fees_data = cur.fetchall()[0]

                if(CheckVar1.get() == 1):
                    cur.execute("update gr_check set c1=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set apr_jun_tution={},APR_JUN_ATITVITY={} where gr_no={}".format(fees_data[3],fees_data[4],FEES_GR_ENTRY.get()))
                    cur.execute("update fee_details set c1=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                if(CheckVar2.get() == 1):
                    cur.execute("update gr_check set c2=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set JUL_SEP_TUTION={},JUL_SEP_ACTIVITY={} where gr_no={}".format(fees_data[6],fees_data[7],FEES_GR_ENTRY.get()))
                    cur.execute("update fee_details set c2=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                if(CheckVar3.get() == 1):
                    cur.execute("update gr_check set c3=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set OCT_DEC_TUTION={},OCT_DEC_ACTIVITY={} where gr_no={}".format(fees_data[8],fees_data[9],FEES_GR_ENTRY.get()))
                    cur.execute("update fee_details set c3=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                if(CheckVar4.get() == 1):
                    cur.execute("update gr_check set c4=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set JAN_MAR_TUTION={},JAN_MAR_ACTIVITY={} where gr_no={}".format(fees_data[10],fees_data[11],FEES_GR_ENTRY.get()))
                    cur.execute("update fee_details set c4=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                if(CheckVar5.get() == 1):
                    cur.execute("update gr_check set c5=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set OTHERS={} where gr_no={}".format(fees_data[12],FEES_GR_ENTRY))
                    cur.execute("update fee_details set c5=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                if(CheckVar6.get() == 1):
                    cur.execute("update gr_check set c6=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set ADMISSION_FEE={} where gr_no={}".format(fees_data[1],FEES_GR_ENTRY))
                    cur.execute("update fee_details set c6=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                if(CheckVar7.get() == 1):
                    cur.execute("update gr_check set c7=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                    cur.execute("update pending_fee_detail set ICARD={} where gr_no={}".format(fees_data[2],FEES_GR_ENTRY))
                    cur.execute("update fee_details set c7=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                # if(CheckVar8.get() == 1):
                #     cur.execute("update gr_check set c8=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
                #     cur.execute("update pending_fee_detail set LATE_FEES={} where gr_no={}".format(0,FEES_GR_ENTRY))
                #     cur.execute("update fee_details set c8=' ' where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("delete from tran_details where receipt_no={}".format(FEES_RECEIPTNO_ENTRY1.get()))
                cur.execute("delete from fee_tran where receipt_no={}".format(FEES_RECEIPTNO_ENTRY1.get()))
                mydb.commit()
                for widget in MAIN_FRAME.winfo_children():
                    widget.destroy()
        delete_button=Button(MAIN_FRAME,text="DELETE",height=3,width=15,bg="lightgrey",activebackground='lightgrey',font=('Arial', 7),command=receipt_delete)
        delete_button.place(x=980,y=440)

    


    FEES_1=Button(MENU_FRAME2,text="RECEIPT DELETE",command = receipt_delete_function)
    FEES_1.place(x=20,y=20)


    def pending_paid_report():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()
        RadioVar2 = IntVar()

        Pending = Radiobutton(MAIN_FRAME, text = "Pending", variable = RadioVar2, value=1, height=2,font=('Arial', 30),bg="lightpink",activebackground='lightpink')
        Paid = Radiobutton(MAIN_FRAME, text = "Paid", variable = RadioVar2, value=2, height=2,font=('Arial', 30),bg="lightpink",activebackground='lightpink')


        Pending.place(x=100,y=150)
        Paid.place(x=100,y=250)

        def pending_paid_report_submit():
            if(RadioVar2.get() == 1):
                file = open("pending_report.csv","w",newline="\n")
                writer2 = csv.writer(file)
                data_heading=['GR NO','NAME','CLASS','FEES','APR-JUN TUTION','APR-JUN ACTIVTIY','JUL-SEP TUTION','JUL-SEP ACTIVITY','OCT-DEC TUTION','OCT-DEC ACTIVITY','JAN-MAR TUTION','JAN-MAR ACTIVITY','OTHERS','ADMISSION','ICARD']
                writer2.writerow(data_heading)
                cur.execute("select * from GR_CHECK order by gr_no")
                data1 = cur.fetchall()
                for i in data1:
                    data=[]
                    cur.execute("select * from pending_fee_detail where gr_no={}".format(i[0]))
                    data2 = cur.fetchall()[0]
                    data.append(i[0])
                    if (data1[1] == 1):
                        data.append(data2[3])
                        data.append(data2[4])
                    else:
                        data.append(0)
                        data.append(0)
                    if data1[2] == 1:
                        data.append(data2[6])
                        data.append(data2[7])
                    else:
                        data.append(0)
                        data.append(0)
                    if data1[3] == 1:
                        data.append(data2[8])
                        data.append(data2[9])
                    else:
                        data.append(0)
                        data.append(0)
                    if data1[4] == 1:
                        data.append(data2[10])
                        data.append(data2[11])
                    else:
                        data.append(0)
                        data.append(0)
                    if data1[5] == 1:
                        data.append(data2[12])
                    else:
                        data.append(0)
                    if data1[6] == 1:
                        data.append(data2[1])
                    else:
                        data.append(0)
                    if data1[7] == 1:
                        data.append(data2[2])
                    else:
                        data.append(0)
                file.close()
                    
            if(RadioVar2.get() == 2):
                file = open("paid_report.csv","w",newline="\n")
                writer2 = csv.writer(file)
                data_heading=['GR NO','NAME','CLASS','FEES','LATE FEES','AMOUNT PAID','DATE']
                writer2.writerow(data_heading)
                cur.execute("select * from tran_details order by gr_no")
                data1 = cur.fetchall()
                for i in data1:
                    data=[]
                    data.append(i[2])
                    data.append(i[4])
                    data.append(str(i[6]) + "-" + str(i[7]))
                    xyz = [i[16],i[17],i[18],i[19],i[20],i[21],i[22]]
                    a = ""
                    if xyz[0] == 1:
                        a = a + "APR-JUN,"
                    if xyz[1] == 1:
                        a = a + "JUL-SEP,"
                    if xyz[2] == 1:
                        a = a + "OCT-DEC,"
                    if xyz[3] == 1:
                        a = a + "JAN-MAR,"
                    if xyz[4] == 1:
                        a = a + "OTHER,"
                    if xyz[6] == 1:
                        a = a + "ICARD,"
                    if xyz[5] == 1:
                        a = a + "ADMISSION,"
                    data.append(a)
                    data.append(i[9])
                    data.append(i[11])
                    data.append(i[3])
                    writer2.writerow(data)
                file.close()
        SAVE_BTN=Button(MAIN_FRAME,text="SUBMIT",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=pending_paid_report_submit)
        SAVE_BTN.place(x=950,y=350)

    FEES_2=Button(MENU_FRAME2,text="FEES REPORT",command=pending_paid_report)
    FEES_2.place(x=20,y=80)

    def gr_fees_change():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()
        def gr_fees_change_submit(e):
            cur.execute("select * from pending_fee_detail where gr_no={}".format(FEES_GR_ENTRY.get()))
            pending_data = cur.fetchall()[0]
            cur.execute("select name,surname from gr_details where gr_no={}".format(FEES_GR_ENTRY.get()))
            gr_data = cur.fetchall()[0]
            cur.execute("select curr_std,division,aai1 from academic_detail where gr_no={}".format(FEES_GR_ENTRY.get()))
            std_data = cur.fetchall()[0]
            cur.execute("select * from exmp_fees where std='{}'".format(std_data[0]))
            exmp_data = cur.fetchall()[0]
            FEES_NAME_ENTRY.delete(0,END)
            FEES_STD_ENTRY.delete(0,END)
            FEES_DIV_ENTRY.delete(0,END)
            OLD_ENT.delete(0,END)
            OLD_ENT1.delete(0,END)
            NEW_ENT.delete(0,END)
            NEW_ENT1.delete(0,END)
            FEES_NAME_ENTRY.insert(0,gr_data[0] + " " + gr_data[1])
            FEES_STD_ENTRY.insert(0,std_data[0])
            FEES_DIV_ENTRY.insert(0,std_data[1])
            val = RadioVar.get()
            if std_data[2] == 0:
                if (val == 1):
                    OLD_ENT.insert(0,pending_data[3])
                    OLD_ENT1.insert(0,pending_data[4])
                if (val == 2):
                    OLD_ENT.insert(0,pending_data[6])
                    OLD_ENT1.insert(0,pending_data[7])
                if(val == 3):
                    OLD_ENT.insert(0,pending_data[8])
                    OLD_ENT1.insert(0,pending_data[9])
                if(val == 4):
                    OLD_ENT.insert(0,pending_data[10])
                    OLD_ENT1.insert(0,pending_data[11])
                if (val == 5):
                    OLD_ENT.insert(0,pending_data[12])
                if (val == 6):
                    OLD_ENT.insert(0,pending_data[2])
                if (val == 7):
                    OLD_ENT.insert(0,pending_data[1])
            else:
                if (val == 1):
                    OLD_ENT.insert(0,pending_data[3] - exmp_data[3])
                    OLD_ENT1.insert(0,pending_data[4] - exmp_data[4])
                if (val == 2):
                    OLD_ENT.insert(0,pending_data[6] - exmp_data[6])
                    OLD_ENT1.insert(0,pending_data[7] - exmp_data[7])
                if(val == 3):
                    OLD_ENT.insert(0,pending_data[8] - exmp_data[8])
                    OLD_ENT1.insert(0,pending_data[9] - exmp_data[9])
                if(val == 4):
                    OLD_ENT.insert(0,pending_data[10] - exmp_data[10])
                    OLD_ENT1.insert(0,pending_data[11] - exmp_data[11])
                if (val == 5):
                    OLD_ENT.insert(0,pending_data[12] - exmp_data[12])
                if (val == 6):
                    OLD_ENT.insert(0,pending_data[2] - exmp_data[2])
                if (val == 7):
                    OLD_ENT.insert(0,pending_data[1] - exmp_data[1])
        FEES_GR_LABEL=Label(MAIN_FRAME,text="GR : ",font=('Arial', 13),bg="lightpink")
        FEES_GR_LABEL.place(x=70,y=80)
        FEES_GR_ENTRY=Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        FEES_GR_ENTRY.place(x=220,y=80)
        FEES_GR_ENTRY.bind("<Return>",gr_fees_change_submit)

        FEES_NAME_LABEL=Label(MAIN_FRAME,text="NAME : ",font=('Arial', 13),bg="lightpink")
        FEES_NAME_LABEL.place(x=70,y=130)
        FEES_NAME_ENTRY=Entry(MAIN_FRAME,width=30,font=('Arial', 13))
        FEES_NAME_ENTRY.place(x=220,y=130)


        FEES_STD_LABEL=Label(MAIN_FRAME,text="STD : ",font=('Arial', 13),bg="lightpink")
        FEES_STD_LABEL.place(x=70,y=180)
        FEES_STD_ENTRY=Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        FEES_STD_ENTRY.place(x=220,y=180)


        FEES_DIV_LABEL=Label(MAIN_FRAME,text="DIV : ",font=('Arial', 13),bg="lightpink")
        FEES_DIV_LABEL.place(x=70,y=230)
        FEES_DIV_ENTRY=Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        FEES_DIV_ENTRY.place(x=220,y=230)



        wrapper2=Frame(MAIN_FRAME,bg="lightpink",height=350,width=270,relief=RIDGE,borderwidth=2)
        wrapper2.place(x=850,y=30)

        RadioVar = IntVar()

        C1 = Radiobutton(wrapper2, text = "APR JUN FEES", variable = RadioVar, value=1, height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C2 = Radiobutton(wrapper2, text = "JUL SEP FEES", variable = RadioVar, value=2,height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C3 = Radiobutton(wrapper2, text = "OCT DEC FEES", variable = RadioVar, value=3,height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C4 = Radiobutton(wrapper2, text = "JAN MAR FEES", variable = RadioVar, value=4,height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C5 = Radiobutton(wrapper2, text = "OTHERS", variable = RadioVar, value=5,height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C6 = Radiobutton(wrapper2, text = "ICARD", variable = RadioVar, value=6,height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C7 = Radiobutton(wrapper2, text = "ADMISSION", variable = RadioVar, value=7,height=2,font=('Arial', 13),bg="lightpink",activebackground='lightpink')
        C1.place(x=0,y=0)
        C2.place(x=0,y=45)
        C3.place(x=0,y=90)
        C4.place(x=0,y=135)
        C5.place(x=0,y=180)
        C6.place(x=0,y=225)
        C7.place(x=0,y=270)



        Label(MAIN_FRAME,text="TUTION",font=('Arial', 13),bg="lightpink").place(x=220,y=350)
        Label(MAIN_FRAME,text="ACTIVITY",font=('Arial', 13),bg="lightpink").place(x=400,y=350)
        OLD_LABEL = Label(MAIN_FRAME,text="OLD FEES : ",font=('Arial', 13),bg="lightpink")
        OLD_LABEL.place(x=70,y=400)
        OLD_ENT = Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        OLD_ENT.place(x=220,y=400)
        OLD_ENT1 = Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        OLD_ENT1.place(x=400,y=400)


        NEW_LABEL = Label(MAIN_FRAME,text="NEW FEES : ",font=('Arial', 13),bg="lightpink")
        NEW_LABEL.place(x=70,y=450)
        NEW_ENT = Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        NEW_ENT.place(x=220,y=450)
        NEW_ENT1 = Entry(MAIN_FRAME,width=17,font=('Arial', 13))
        NEW_ENT1.place(x=400,y=450)


        def gr_fees_change_save():
            cur.execute("select * from pending_fee_detail where gr_no={}".format(FEES_GR_ENTRY.get()))
            pending_data = cur.fetchall()[0]
            cur.execute("select name,surname from gr_details where gr_no={}".format(FEES_GR_ENTRY.get()))
            gr_data = cur.fetchall()[0]
            cur.execute("select curr_std,division,aai1 from academic_detail where gr_no={}".format(FEES_GR_ENTRY.get()))
            std_data = cur.fetchall()[0]
            cur.execute("select * from exmp_fees where std='{}'".format(std_data[0]))
            exmp_data = cur.fetchall()[0]
            val = RadioVar.get()
            gr = FEES_GR_ENTRY.get()
            newfee = NEW_ENT.get()
            newfee1 = NEW_ENT1.get()
            cur.execute("select aai1 from academic_detail where gr_no={}".format(gr))
            aai1 = cur.fetchall()[0]
            if aai1[0] == 0:
                if (val == 1):
                    cur.execute("update pending_fee_detail set apr_jun_tution={},apr_jun_atitvity={} where gr_no={}".format(newfee,newfee1,gr))
                if (val == 2):
                    cur.execute("update pending_fee_detail set jul_sep_tution={},jul_sep_activity={} where gr_no={}".format(newfee,newfee1,gr))
                if(val == 3):
                    cur.execute("update pending_fee_detail set oct_dec_tution={},oct_dec_activity={} where gr_no={}".format(newfee,newfee1,gr))
                if(val == 4):
                    cur.execute("update pending_fee_detail set jan_mar_tution={},jan_mar_activity={} where gr_no={}".format(newfee,newfee1,gr))
                if (val == 5):
                    cur.execute("update pending_fee_detail set OTHERS={} where gr_no={}".format(newfee,gr))
                if (val == 6):
                    cur.execute("update pending_fee_detail set ICARD={} where gr_no={}".format(newfee,gr))
                if (val == 7):
                    cur.execute("update pending_fee_detail set admission_fee={} where gr_no={}".format(newfee,gr))
            else:
                if (val == 1):
                    cur.execute("update pending_fee_detail set apr_jun_tution={},apr_jun_atitvity={} where gr_no={}".format(int(newfee) + exmp_data[3],int(newfee1) + exmp_data[4],gr))
                if (val == 2):
                    cur.execute("update pending_fee_detail set jul_sep_tution={},jul_sep_activity={} where gr_no={}".format(int(newfee) + exmp_data[6],int(newfee1) + exmp_data[7],gr))
                if(val == 3):
                    cur.execute("update pending_fee_detail set oct_dec_tution={},oct_dec_activity={} where gr_no={}".format(int(newfee) + exmp_data[8],int(newfee1) + exmp_data[9],gr))
                if(val == 4):
                    cur.execute("update pending_fee_detail set jan_mar_tution={},jan_mar_activity={} where gr_no={}".format(int(newfee) + exmp_data[10],int(newfee1) + exmp_data[11],gr))
                if (val == 5):
                    cur.execute("update pending_fee_detail set OTHERS={} where gr_no={}".format(int(newfee) + exmp_data[12],gr))
                if (val == 6):
                    cur.execute("update pending_fee_detail set ICARD={} where gr_no={}".format(int(newfee) + exmp_data[2],gr))
                if (val == 7):
                    cur.execute("update pending_fee_detail set admission_fee={} where gr_no={}".format(int(newfee) + exmp_data[1],gr))
            mydb.commit()
            for widget in MAIN_FRAME.winfo_children():
                widget.destroy()
        SAVE_BTN=Button(MAIN_FRAME,text="SAVE",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=gr_fees_change_save)
        SAVE_BTN.place(x=850,y=400)


    FEES_3=Button(MENU_FRAME2,text="GR FEES CHANGE",command=gr_fees_change)
    FEES_3.place(x=20,y=140)




    wrapper1=Frame(MAIN_FRAME,height=250,width=620)
    wrapper1.place(x=50,y=170)
    style = ttk.Style()
    style.theme_use('clam')
    trv=ttk.Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="8")

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




    wrapper2=Frame(MAIN_FRAME,bg="lightpink",height=320,width=250,relief=RIDGE,borderwidth=2)
    wrapper2.place(x=1000,y=60)


    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()

    C1 = Checkbutton(wrapper2, text = "APR JUN FEES", variable = CheckVar1,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')
    C2 = Checkbutton(wrapper2, text = "JUL SEP FEES", variable = CheckVar2,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')
    C3 = Checkbutton(wrapper2, text = "OCT DEC FEES", variable = CheckVar3,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')
    C4 = Checkbutton(wrapper2, text = "JAN MAR FEES", variable = CheckVar4,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')
    C5 = Checkbutton(wrapper2, text = "OTHERS", variable = CheckVar5,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')
    C6 = Checkbutton(wrapper2, text = "ADMISSION", variable = CheckVar6,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')
    C7 = Checkbutton(wrapper2, text = "ICARD", variable = CheckVar7,onvalue = 1, offvalue = 0, height=2,font=('Arial', 11),bg="lightpink",activebackground='lightpink')

    C1.place(x=0,y=0)
    C2.place(x=0,y=45)
    C3.place(x=0,y=90)
    C4.place(x=0,y=135)
    C5.place(x=0,y=180)
    C6.place(x=0,y=225)
    C7.place(x=0,y=270)
    


    global fees_search
    def fees_search(e):
    
        root.bell()
        top = Toplevel()
        # top.attributes('-fullscreen', True)
        top.geometry("1400x700")
        top.title("ZETA CORE")
        top.configure(bg="lightpink")
        photo = PhotoImage(file = r"ICONS\Zeta.png")
        top.iconphoto(False, photo)

        search_label=Label(top, text='Search : ', font=('Orator Std',16), fg='white', bg='lightpink')
        search_label.place(x=100, y=20)


        surname_label=Label(top,text="Surname :", font=('Orator Std',12, 'bold'), bg='lightpink')
        surname_label.place(x=250, y=100)
        surname_var=StringVar()
        surname_entry=Entry(top, font=('Orator Std',10, 'bold'),textvariable=surname_var, width=18)
        surname_entry.place(x=350, y=100)
        


        name_label=Label(top,text="Name :", font=('Orator Std',12, 'bold'), bg='lightpink')
        name_label.place(x=550, y=100)
        name_var=StringVar()
        name_entry=Entry(top, font=('Orator Std',10, 'bold'),textvariable=name_var, width=18)
        name_entry.place(x=630, y=100)


        gr_num_label=Label(top, text="GR no :",font=('Orator Std',12, 'bold'), bg='lightpink')
        gr_num_label.place(x=200, y=150)
        gr_num_label=Label(top, text=">=",font=('Orator Std',12, 'bold'), bg='lightpink')
        gr_num_label.place(x=300, y=150)
        gr_num_var=IntVar()
        gr_num_entry=Entry(top,font=('Orator Std',10, 'bold'), textvariable=gr_num_var, width=15)
        gr_num_entry.place(x=350, y=150)


        gr_num_label2=Label(top, text="<=",font=('Orator Std',12, 'bold'), bg='lightpink')
        gr_num_label2.place(x=580, y=150)
        gr_num_var2=IntVar()
        gr_num_entry2=Entry(top,font=('Orator Std',10, 'bold'), textvariable=gr_num_var2, width=15)
        gr_num_entry2.place(x=630, y=150)






        


        tree_frame=Frame(top, width=1000)
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

        cur.execute("select gr_details.gr_no,gr_details.name,gr_details.surname,academic_detail.curr_std,academic_detail.division,academic_detail.roll_no from gr_details,academic_detail where gr_details.gr_no=academic_detail.gr_no")
        data = cur.fetchall()
        
        for i in range(len(data)):
            treeview.insert(parent='', iid=i, index='end',text='', values=data[i])
        
        
        
        # def treeview_insert():
        #     cur.execute("select gr_details.gr_no,gr_details.name,gr_details.surname,academic_detail.curr_std,academic_detail.division,academic_detail.roll_no from gr_details,academic_detail where gr_details.gr_no=academic_detail.gr_no and gr_details.name like {}% and gr_details.surname like {}% and academic_detail.curr_std like {}%".format(name_var.get(),surname_var.get(),gr_num_var.get()))
        #     data = cur.fetchall()
            
        #     for i in range(len(data)):
        #         treeview.insert(parent='', iid=i, index='end',text='', values=data[i])

        def fees_search1(e):
            # print(gr_num_entry.get())
            # print(gr_num_entry2.get())
            if(name_entry.get() == '' or surname_entry.get() == ''):
                cur.execute("select gr_details.gr_no,gr_details.name,gr_details.surname,academic_detail.curr_std,academic_detail.division,academic_detail.roll_no from gr_details,academic_detail where gr_details.gr_no=academic_detail.gr_no and gr_details.gr_no >= {} and gr_details.gr_no <= {}".format(gr_num_entry.get(),gr_num_entry2.get()))
                treeview.delete(*treeview.get_children())
                data = cur.fetchall()
            else:
                cur.execute("select gr_details.gr_no,gr_details.name,gr_details.surname,academic_detail.curr_std,academic_detail.division,academic_detail.roll_no from gr_details,academic_detail where gr_details.gr_no=academic_detail.gr_no and gr_details.gr_no >= {} and gr_details.gr_no <= {} and gr_details.name like '{}%' and gr_details.surname like '{}%'".format(gr_num_entry.get(),gr_num_entry2.get(),name_entry.get(),surname_entry.get()))

                treeview.delete(*treeview.get_children())
                data = cur.fetchall()
        
            for i in range(len(data)):
                treeview.insert(parent='', iid=i, index='end',text='', values=data[i])
        surname_entry.bind("<Return>",fees_search1)
        name_entry.bind("<Return>",fees_search1)
        gr_num_entry.bind("<Return>",fees_search1)
        gr_num_entry2.bind("<Return>",fees_search1)
        

        search_btn=Button(top, text="Search",font=('Orator STD',10, 'bold'), width=10,command=fees_search1)
        search_btn.place(x=1000, y=150)
        top.mainloop()
    

    

        

    SEARCH_BTN=Button(MAIN_FRAME,text="SEARCH",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=fees_search)
    SEARCH_BTN.place(x=1100,y=420)


    







    FEES_DEPT_LABEL=Label(MAIN_FRAME,text="DEPT : ",font=('Arial', 10),bg="lightpink")
    FEES_DEPT_LABEL.place(x=50,y=10)
    FEES_DEPT_ENTRY=Entry(MAIN_FRAME,width=20)
    FEES_DEPT_ENTRY.place(x=110,y=10)
    FEES_DEPT_ENTRY.delete(0,END)
    FEES_DEPT_ENTRY.insert(0,"CBSE")

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
    cur.execute("select * from fee_tran")
    data = cur.fetchall()
    FEES_RECEIPTNO_ENTRY.delete(0,END)
    FEES_RECEIPTNO_ENTRY.insert(0,data[-1][0]+1)


    FEES_NAME_LABEL=Label(MAIN_FRAME,text="NAME : ",font=('Arial', 10),bg="lightpink")
    FEES_NAME_LABEL.place(x=50,y=50)
    FEES_NAME_ENTRY=Entry(MAIN_FRAME,width=54)
    FEES_NAME_ENTRY.place(x=110,y=50)


    FEES_RECEIPTBOOK_LABEL=Label(MAIN_FRAME,text="RECEIPT BOOK : ",font=('Arial', 10),bg="lightpink")
    FEES_RECEIPTBOOK_LABEL.place(x=680,y=50)
    FEES_RECEIPTBOOK_ENTRY=Entry(MAIN_FRAME,width=20,font=('Arial', 10))
    FEES_RECEIPTBOOK_ENTRY.place(x=790,y=50)
    FEES_RECEIPTBOOK_ENTRY.delete(0,END)
    FEES_RECEIPTBOOK_ENTRY.insert(0,"ARPT")


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
    FEES_LATEFEES_ENTRY.insert(0,0)


    EXEMPTION_LABEL=Label(MAIN_FRAME,text="EXEMPTION : ",font=('Arial', 10),bg="lightpink")
    EXEMPTION_LABEL.place(x=480,y=460)
    EXEMPTION_ENTRY=Entry(MAIN_FRAME,width=14,font=('Arial', 15))
    EXEMPTION_ENTRY.place(x=450,y=480)
    EXEMPTION_ENTRY.insert(0,0)

    
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
        fee_lst.append(FEES_RECEIPTNO_ENTRY.get())#1
        fee_lst.append(FEES_DEPT_ENTRY.get())#2
        fee_lst.append(FEES_GR_ENTRY.get())#3
        fee_lst.append(FEES_DATE_ENTRY.get())#4
        fee_lst.append(FEES_NAME_ENTRY.get())#5
        fee_lst.append(FEES_RECEIPTBOOK_ENTRY.get())#6
        fee_lst.append(FEES_STD_ENTRY.get())#7
        fee_lst.append(FEES_DIV_ENTRY.get())#8
        fee_lst.append(FEES_TOTALAMOUNT_ENTRY.get())#9
        fee_lst.append(FEES_LATEFEES_ENTRY.get())#10
        fee_lst.append(EXEMPTION_ENTRY.get())#11
        fee_lst.append(int(FEES_TOTALAMOUNT_ENTRY.get())+int(FEES_LATEFEES_ENTRY.get())-int(EXEMPTION_ENTRY.get()))#12
        fee_lst.append(FEES_PAYMODE_ENTRY.get())#13
        fee_lst.append(FEES_BANKNAME_ENTRY.get())#14
        fee_lst.append(FEES_CHEQUENUMBER_ENTRY.get())#15
        fee_lst.append(FEES_CHEQUEDATE_ENTRY.get())#16
        fee_lst.append(CheckVar1.get())#17
        fee_lst.append(CheckVar2.get())#18
        fee_lst.append(CheckVar3.get())#19
        fee_lst.append(CheckVar4.get())#20
        fee_lst.append(CheckVar5.get())#21
        fee_lst.append(CheckVar6.get())#22
        fee_lst.append(CheckVar7.get())#23
        cur.execute("insert into tran_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",fee_lst)
        cur.execute("insert into fee_tran values({},0,0,0,0,0,0,0)".format(FEES_RECEIPTNO_ENTRY.get()))

        if (CheckVar1.get() == 0):
            cur.execute("update gr_check set c1=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c1 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c1=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c1=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c1='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
                cur.execute("update pending_fee_detail set APR_JUN_TUTION=0,APR_JUN_ATITVITY=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))



        if(CheckVar2.get() == 0):
            cur.execute("update gr_check set c2=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c2 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c2=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c2=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c2='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
                cur.execute("update pending_fee_detail set JUL_SEP_TUTION=0,JUL_SEP_ACTIVITY=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))
        if(CheckVar3.get() == 0):
            cur.execute("update gr_check set c3=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c3 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c3=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c3=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c3='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
                cur.execute("update pending_fee_detail set OCT_DEC_TUTION=0,OCT_DEC_ACTIVITY=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))
        if(CheckVar4.get() == 0):
            cur.execute("update gr_check set c4=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c4 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c4=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c4=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c4='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
                cur.execute("update pending_fee_detail set JAN_MAR_TUTION=0,JAN_MAR_ACTIVITY=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))

        if(CheckVar5.get() == 0):
            cur.execute("update gr_check set c5=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c5 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c5=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c5=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update fee_details set c5='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
                cur.execute("update pending_fee_detail set OTHERS=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))
        if(CheckVar6.get() == 0):
            cur.execute("update gr_check set c6=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c6 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c6=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c6=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update pending_fee_detail set ADMISSION_FEE=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_details set c6='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
        if(CheckVar7.get() == 0):
            cur.execute("update gr_check set c7=0 where gr_no={}".format(FEES_GR_ENTRY.get()))
        else:
            cur.execute("select c7 from gr_check where gr_no={}".format(FEES_GR_ENTRY.get()))
            data = cur.fetchall()
            if(int(data[0][0]) == 0):
                cur.execute("update gr_check set c7=1 where gr_no={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_tran set c7=1 where RECEIPT_NO={}".format(FEES_RECEIPTNO_ENTRY.get()))
                cur.execute("update pending_fee_detail set ICARD=0 WHERE GR_NO={}".format(FEES_GR_ENTRY.get()))
                cur.execute("update fee_details set c7='{}' where gr_no={}".format(FEES_CHEQUENUMBER_ENTRY.get(),FEES_GR_ENTRY.get()))
        mydb.commit()




        def number_to_word(number):
            def get_word(n):
                words={ 0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninty" }
                if n<=20:
                    return words[n]
                else:
                    ones=n%10
                    tens=n-ones
                    return words[tens]+" "+words[ones]
                    
            def get_all_word(n):
                d=[100,10,100,100]
                v=["","Hundred And","Thousand","lakh"]
                w=[]
                for i,x in zip(d,v):
                    t=get_word(n%i)
                    if t!="":
                        t+=" "+x
                    w.append(t.rstrip(" "))
                    n=n//i
                w.reverse()
                w=' '.join(w).strip()
                if w.endswith("And"):
                    w=w[:-3]
                return w

            arr=str(number).split(".")
            number=int(arr[0])
            crore=number//10000000
            number=number%10000000
            word=""
            if crore>0:
                word+=get_all_word(crore)
                word+=" crore "
            word+=get_all_word(number).strip()+" Rupees"
            if len(arr)>1:
                if len(arr[1])==1:
                    arr[1]+="0"
                word+=" and "+get_all_word(int(arr[1]))+" paisa"
            return word

        def fees_print():
            Grvalue=FEES_GR_ENTRY.get()
            RECEIPT_VAR=FEES_RECEIPTNO_ENTRY.get()
            DATE_VAR=FEES_DATE_ENTRY.get()
            TOTAL_AMOUNT_VAR=FEES_GRANDTOTAL_ENTRY.get()
            PAY_TYPE=FEES_PAYMODE_ENTRY.get()
            CHEQUE_VAR=FEES_CHEQUENUMBER_ENTRY.get()
            t=(number_to_word(int(TOTAL_AMOUNT_VAR)))
            BANK_VAR=FEES_BANKNAME_ENTRY.get()

            cur.execute("select SURNAME,NAME,FATHER from gr_details WHERE GR_NO=%s",[Grvalue])
            fee_wee=cur.fetchall()

            cur.execute("select curr_std,division from academic_detail WHERE GR_NO=%s",[Grvalue])
            fee_wee_1=cur.fetchall()


            NAME_VAR=fee_wee[0][1]
            SURNAME_VAR=fee_wee[0][0]
            FATHERS_NAME_VAR=fee_wee[0][2]
            STD_VAR=fee_wee_1[0][0]+"-"+fee_wee_1[0][1]

            


            print(Grvalue,RECEIPT_VAR,DATE_VAR,TOTAL_AMOUNT_VAR,PAY_TYPE,CHEQUE_VAR,BANK_VAR,NAME_VAR,SURNAME_VAR,FATHERS_NAME_VAR,STD_VAR)
            cur.execute("select aai1 from academic_detail where gr_no={}".format(Grvalue))
            aai_data=cur.fetchall()[0]


            FEES_NAME_PAID=[]
            FEES_AMT_PAID=[]
            for child in trv.get_children():
                # print(trv.item(child)["values"])
                FEES_NAME_PAID.append(trv.item(child)["values"][0])
                FEES_AMT_PAID.append(trv.item(child)["values"][3])

            


            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch
            from reportlab.lib.pagesizes import letter, A4

            my_path = "RECIEPTS\\{}  - {}.pdf".format(str(NAME_VAR)+" "+str(SURNAME_VAR),str(RECEIPT_VAR))

            c=canvas.Canvas(my_path,pagesize=A4)
            c.translate(inch,inch)
            c.setStrokeColorRGB(0,0,0) 
            c.setLineWidth(2)
            c.line(-15,580,475,580)

            c.setFont('Helvetica-Bold',17)
            c.drawString(130,690,"AIRPORT SCHOOL - AHMEDABAD")
            c.setFont('Helvetica',15)

            c.drawString(145,670,"CBSE AFFILIATION NO 430133")
            c.drawString(108,650,"AIRPORT COLONY, SARDARNAGAR, AHMEDABAD")
            c.drawString(173,630,"PHONE : 079-22864175")
            
            c.setFont('Helvetica-Bold',17)
            c.drawString(193,610,"C.B.S.E BOARD")
            c.setFont('Helvetica',12)
            
            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,557,"Receipt No :")
            c.setFont('Helvetica',12)
            c.drawString(80,557,str(RECEIPT_VAR))
            
            c.setFont('Helvetica-Bold',12)
            c.drawString(350,557,"Date :")
            c.setFont('Helvetica',12)
            c.drawString(390,557,str(DATE_VAR))


            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,540,"Student's Name :")
            c.setFont('Helvetica',12)
            c.drawString(100,542,str(NAME_VAR)+" "+str(SURNAME_VAR))

            c.setFont('Helvetica-Bold',12)
            c.drawString(350,540,"Std :")
            c.setFont('Helvetica',12)
            c.drawString(390,540,str(STD_VAR))

            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,523,"Father's Name :")
            c.setFont('Helvetica',12)
            c.drawString(95,523,str(FATHERS_NAME_VAR)+" "+str(SURNAME_VAR))

            c.setFont('Helvetica-Bold',12)
            c.drawString(350,523,"G.R.No :")
            c.setFont('Helvetica',12)
            c.drawString(410,523,str(Grvalue))
            c.setLineWidth(2)
            c.line(-15,7.2*inch,6.6*inch,7.2*inch)
            c.setFont('Helvetica-Bold',12)
            c.drawString(140,498,"Fee Detail")
            c.drawString(380,498,"Fee Amount")
            c.setFont('Helvetica',12)

            x=25
            y=460

            p=435
            q=460
            c.drawString(x,y,str(FEES_NAME_PAID[0]))
            c.drawString(p,q,str(FEES_AMT_PAID[0]))
            print(FEES_NAME_PAID)
            if(aai_data[0] == 0):
                for i in range(len(FEES_NAME_PAID)):
                    if FEES_NAME_PAID[i] == "APR_JUN_ATITVITY":
                        FEES_NAME_PAID[i]="APR_JUN_ACTIVITY"
                    if FEES_NAME_PAID[i] == "ICARD":
                        FEES_NAME_PAID[i]="ICARD, ALMANAC & CLASS GROUP PHOTO"
            else:
                for i in range(len(FEES_NAME_PAID)):
                    if FEES_NAME_PAID[i] == "APR_JUN_ATITVITY":
                        FEES_NAME_PAID[i]="APR_SEP_ACTIVITY"
                    if FEES_NAME_PAID[i] == "JUL_SEP_ACTIVITY":
                        FEES_NAME_PAID[i]="OCT_MAR_ACTIVITY"
                    if FEES_NAME_PAID[i] == "ICARD":
                        FEES_NAME_PAID[i]="ICARD, ALMANAC & CLASS GROUP PHOTO"
            print(FEES_NAME_PAID)

            for a in range(1,len(FEES_NAME_PAID)):
                y=y-20
                c.drawString(x,y,str(FEES_NAME_PAID[a]))

            for b in range(1,len(FEES_AMT_PAID)):
                q=q-20
                c.drawString(p,q,str(FEES_AMT_PAID[b]))


            c.setLineWidth(2)
            c.line(-15,6.8*inch,6.6*inch,6.8*inch)

            c.setLineWidth(2)
            c.line(-15,0.7*inch,6.6*inch,0.7*inch)

            c.setLineWidth(2)
            c.line(-15,0.4*inch,6.6*inch,0.4*inch)

            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,5,"Pay By :")
            c.setFont('Helvetica',12)
            
            c.drawString(50,5,str(PAY_TYPE)+' '+str(CHEQUE_VAR)+' '+str(BANK_VAR))
            


            c.drawString(0,34,str(t))
            c.setFont('Helvetica-Bold',12)
            c.drawString(400,34,str(TOTAL_AMOUNT_VAR)+str('/-'))
            c.setFont('Helvetica',12)

            

            c.drawString(370,-10,"RAMESH")
            c.setLineWidth(2)
            c.line(350,-14,440,-14)

            c.setFont('Helvetica-Bold',12)
            c.drawString(360,-25,"Receiver Sign")
            c.setFont('Helvetica',12)

            c.drawImage(r"ICONS\schl logo1.png",-0.3*inch,8.5*inch)

            c.setLineWidth(2)
            c.setStrokeColorRGB(0,0,0)
            c.rect(-0.2*inch,-0.5*inch,6.8*inch,10.8*inch,fill=0)
            c.showPage()
            
            c.translate(inch,inch)
            c.setStrokeColorRGB(0,0,0) 
            c.setLineWidth(2)
            c.line(-15,580,475,580)

            c.setFont('Helvetica-Bold',17)
            c.drawString(130,690,"AIRPORT SCHOOL - AHMEDABAD")
            c.setFont('Helvetica',15)

            c.drawString(145,670,"CBSE AFFILIATION NO 430133")
            c.drawString(108,650,"AIRPORT COLONY, SARDARNAGAR, AHMEDABAD")
            c.drawString(173,630,"PHONE : 079-22864175")
            
            c.setFont('Helvetica-Bold',17)
            c.drawString(193,610,"C.B.S.E BOARD")
            c.setFont('Helvetica',12)
            
            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,557,"Receipt No :")
            c.setFont('Helvetica',12)
            c.drawString(80,557,str(RECEIPT_VAR))
            
            c.setFont('Helvetica-Bold',12)
            c.drawString(350,557,"Date :")
            c.setFont('Helvetica',12)
            c.drawString(390,557,str(DATE_VAR))


            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,540,"Student's Name :")
            c.setFont('Helvetica',12)
            c.drawString(100,542,str(NAME_VAR)+" "+str(SURNAME_VAR))

            c.setFont('Helvetica-Bold',12)
            c.drawString(350,540,"Std :")
            c.setFont('Helvetica',12)
            c.drawString(390,540,str(STD_VAR))
            
            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,523,"Father's Name :")
            c.setFont('Helvetica',12)
            c.drawString(95,523,str(FATHERS_NAME_VAR)+" "+str(SURNAME_VAR))

            c.setFont('Helvetica-Bold',12)
            c.drawString(350,523,"G.R.No :")
            c.setFont('Helvetica',12)
            c.drawString(410,523,str(Grvalue))
            
            c.setLineWidth(2)
            c.line(-15,7.2*inch,6.6*inch,7.2*inch)
            c.setFont('Helvetica-Bold',12)
            c.drawString(140,498,"Fee Detail")
            c.drawString(380,498,"Fee Amount")
            c.setFont('Helvetica',12)
            x=25
            y=460

            p=435
            q=460
            c.drawString(x,y,str(FEES_NAME_PAID[0]))
            c.drawString(p,q,str(FEES_AMT_PAID[0]))
            for a in range(1,len(FEES_NAME_PAID)):
                y=y-20
                c.drawString(x,y,str(FEES_NAME_PAID[a]))

            for b in range(1,len(FEES_AMT_PAID)):
                q=q-20
                c.drawString(p,q,str(FEES_AMT_PAID[b]))             


            c.setLineWidth(2)
            c.line(-15,6.8*inch,6.6*inch,6.8*inch)

            c.setLineWidth(2)
            c.line(-15,0.7*inch,6.6*inch,0.7*inch)

            c.setLineWidth(2)
            c.line(-15,0.4*inch,6.6*inch,0.4*inch)

            c.setFont('Helvetica-Bold',12)
            c.drawString(-0.1,5,"Pay By :")
            c.setFont('Helvetica',12)

            c.drawString(50,5,str(PAY_TYPE)+' '+str(CHEQUE_VAR)+' '+str(BANK_VAR))

            c.drawString(0,34,str(t))
            c.setFont('Helvetica-Bold',12)
            c.drawString(400,34,str(TOTAL_AMOUNT_VAR)+str('/-'))
            c.setFont('Helvetica',12)


            c.drawString(370,-10,"RAMESH")
            c.setLineWidth(2)
            c.line(350,-14,440,-14)

            c.setFont('Helvetica-Bold',12)
            c.drawString(360,-25,"Receiver Sign")
            c.setFont('Helvetica',12)

            c.drawImage(r"ICONS\schl logo1.png",-0.3*inch,8.5*inch)

            c.setLineWidth(2)
            c.setStrokeColorRGB(0,0,0)
            c.rect(-0.2*inch,-0.5*inch,6.8*inch,10.8*inch,fill=0)

            c.showPage()
            
            c.save()
            
            import os
            os.startfile(my_path)
            
        fees_print()
        FEES_REPORT_FUNCTION()
        BACKUP_FUNCTION()
        FEES_FUNCTION()




    def fees_generate():
        GR_VALUE = FEES_GR_ENTRY.get()
        cur.execute("select curr_std,division from academic_detail where gr_no={}".format(GR_VALUE))
        data1 = cur.fetchall()
        trv.delete(*trv.get_children())
        cur.execute("select * from gr_check where gr_no={}".format(GR_VALUE))
        gr_checks = cur.fetchall()
        cur.execute("select * from pending_fee_detail where gr_no={}".format(GR_VALUE))
        pending_data = cur.fetchall()
        cur.execute("select aai1 from academic_detail where gr_no={}".format(GR_VALUE))
        aaidata = cur.fetchall()[0]
        if(aaidata[0] == 1):
            cur.execute("select * from exmp_fees where std='{}'".format(data1[0][0]))
            exmp_data = cur.fetchall()
        else:
            exmp_data = [[data1[0][0],0,0,0,0,0,0,0,0,0,0,0,0]]
        if (CheckVar1.get() == 1):
            if(gr_checks[0][1] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("APR_JUN_TUTION",pending_data[0][3],exmp_data[0][3],pending_data[0][3]-exmp_data[0][3]))
                trv.insert(parent='',index="end",text='',value=("APR_JUN_ATITVITY",pending_data[0][4],exmp_data[0][4],pending_data[0][4]-exmp_data[0][4]))
        if (CheckVar2.get() == 1):
            if(gr_checks[0][2] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("JUL_SEP_TUTION",pending_data[0][6],exmp_data[0][6],pending_data[0][6]-exmp_data[0][6]))
                trv.insert(parent='',index="end",text='',value=("JUL_SEP_ACTIVITY",pending_data[0][7],exmp_data[0][7],pending_data[0][7]-exmp_data[0][7]))
        if (CheckVar3.get() == 1):
            if(gr_checks[0][3] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("OCT_DEC_TUTION",pending_data[0][8],exmp_data[0][8],pending_data[0][8]-exmp_data[0][8]))
                trv.insert(parent='',index="end",text='',value=("OCT_DEC_ACTIVITY",pending_data[0][9],exmp_data[0][9],pending_data[0][9]-exmp_data[0][9]))
        if (CheckVar4.get() == 1):
            if(gr_checks[0][4] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("JAN_MAR_TUTION",pending_data[0][10],exmp_data[0][10],pending_data[0][10]-exmp_data[0][10]))
                trv.insert(parent='',index="end",text='',value=("JAN_MAR_ACTIVITY",pending_data[0][11],exmp_data[0][11],pending_data[0][11]-exmp_data[0][11]))
        if (CheckVar5.get() == 1):
            if(gr_checks[0][5] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("OTHERS",pending_data[0][12],exmp_data[0][12],pending_data[0][12]-exmp_data[0][12]))
        if (CheckVar6.get() == 1):
            if(gr_checks[0][5] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("ADMISSION_FEE",pending_data[0][1],exmp_data[0][1],pending_data[0][1]-exmp_data[0][1]))
        if (CheckVar7.get() == 1):
            if(gr_checks[0][5] == 1):
                pass
            else:
                trv.insert(parent='',index="end",text='',value=("ICARD",pending_data[0][2],exmp_data[0][2],pending_data[0][2]-exmp_data[0][2]))
        if (len(trv.get_children()) != 0):
            total = 0
            for l in trv.get_children():
                values1 = []
                for v in trv.item(l)["values"]:
                    values1.append(v)
                total += int(values1[-1])
        FEES_TOTALAMOUNT_ENTRY.delete(0,END)
        FEES_TOTALAMOUNT_ENTRY.insert(0,total)
        late_fees = int(FEES_LATEFEES_ENTRY.get())
        if late_fees>0:
            trv.insert(parent='',index="end",text='',value=("LATE FEES",late_fees,0,late_fees))

        exmp_fees = int(EXEMPTION_ENTRY.get())
        if exmp_fees>0:
            trv.insert(parent='',index="end",text='',value=("EXEMPTION",exmp_fees,0,exmp_fees))
        FEES_GRANDTOTAL_ENTRY.delete(0,END)
        FEES_GRANDTOTAL_ENTRY.insert(0,total+late_fees-exmp_fees)
        mydb.commit()
        
        SAVE_BTN["state"]=ACTIVE

    def fees_insert(e):
        GR_VALUE = FEES_GR_ENTRY.get()
        cur.execute("select name,father,surname from gr_details where gr_no={}".format(GR_VALUE))
        data = cur.fetchall()
        full_name = data[0][0] +" "+ data[0][1] +" "+ data[0][2]
        cur.execute("select curr_std,division from academic_detail where gr_no={}".format(GR_VALUE))
        data1 = cur.fetchall()
        FEES_STD_ENTRY.delete(0,END)
        FEES_STD_ENTRY.insert(0,data1[0][0])
        FEES_DIV_ENTRY.delete(0,END)
        FEES_DIV_ENTRY.insert(0,data1[0][1])
        FEES_NAME_ENTRY.delete(0,END)
        FEES_NAME_ENTRY.insert(0,full_name)

        FEES_DEPT_ENTRY.delete(0,END)
        FEES_DEPT_ENTRY.insert(0,"CBSE")
        FEES_RECEIPTBOOK_ENTRY.delete(0,END)
        FEES_RECEIPTBOOK_ENTRY.insert(0,"ARPT")
        cur.execute("select receipt_no from fee_tran")
        rec = cur.fetchall()
        FEES_RECEIPTNO_ENTRY.delete(0,END)
        FEES_RECEIPTNO_ENTRY.insert(0,rec[-1][0] + 1)
        
        cur.execute("select * from gr_check where gr_no={}".format(GR_VALUE))
        gr_checks = cur.fetchall()
        
        if(gr_checks[0][1] == 0):
            C1.deselect()
            C1 .config(state=ACTIVE)
        else:
            C1.select()
            C1.config(state=DISABLED)

        if(gr_checks[0][2] == 0):
            C2.deselect()
            C2.config(state=ACTIVE)
        else:
            C2.select()
            C2.config(state=DISABLED)
        if(gr_checks[0][3] == 0):
            C3.deselect()
            C3.config(state=ACTIVE)
        else:
            C3.select()
            C3.config(state=DISABLED)
        if(gr_checks[0][4] == 0):
            C4.deselect()
            C4.config(state=ACTIVE)
        else:
            C4.select()
            C4.config(state=DISABLED)
        if(gr_checks[0][5] == 0):
            C5.deselect()
            C5.config(state=ACTIVE)
        else:
            C5.select()
            C5.config(state=DISABLED)
        if(gr_checks[0][6] == 0):
            C6.deselect()
            C6.config(state=ACTIVE)
        else:
            C6.select()
            C6.config(state=DISABLED)
        if(gr_checks[0][7] == 0):
            C7.deselect()
            C7.config(state=ACTIVE)
        else:
            C7.select()
            C7.config(state=DISABLED)
        mydb.commit()
    FEES_GR_ENTRY.bind('<Return>',fees_insert)






    def show_fee_details_func(e):
        grval = FEES_GR_ENTRY.get()
        win=Toplevel()
        win.geometry("1500x900")
        win.configure(background="lightpink")

        GR_NO_SEARCH_lbl=Label(win,text="GR NO :",bg="lightpink",font=('Arial', 10,"bold"))
        GR_NO_SEARCH_lbl.place(x=200,y=150)
        GR_NO_SEARCH_entry=Entry(win,font=('Arial', 10,"bold"),width=20)
        GR_NO_SEARCH_entry.place(x=270,y=150)
        GR_NO_SEARCH_entry.insert(0,grval)

        cur.execute("select name,surname from gr_details where gr_no={}".format(grval))
        data = cur.fetchall()
        NAME_SEARCH_lbl=Label(win,text="NAME :",bg="lightpink",font=('Arial', 10,"bold"))
        NAME_SEARCH_lbl.place(x=490,y=150)        
        NAME_SEARCH_ENTRY=Entry(win,font=('Arial', 10,"bold"),width=20)
        NAME_SEARCH_ENTRY.place(x=550,y=150)
        NAME_SEARCH_ENTRY.insert(0,data[0][0])



        SUR_NAME_SEARCH_lbl=Label(win,text="SUR NAME :",bg="lightpink",font=('Arial', 10, "bold"))
        SUR_NAME_SEARCH_lbl.place(x=790,y=150)
        SUR_NAME_SEARCH_ENTRY=Entry(win,font=('Arial', 10, "bold"),width=20)
        SUR_NAME_SEARCH_ENTRY.place(x=890,y=150)
        SUR_NAME_SEARCH_ENTRY.insert(0,data[0][1])
    


        style = ttk.Style()
        style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings', height=15)
        #tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Fee Name")
        tree.heading("# 2", text="Amount")
        tree.heading("# 3", text="Exemption") 
        tree.heading("# 4", text="Paid")
        tree.heading("# 5", text="Paid details")
        tree.heading("# 6", text="Remain")
        tree.heading("#7",text="Receipt Book")
        # tree.insert()
        cur.execute("select * from pending_fee_detail where gr_no={}".format(grval))
        pending_data = cur.fetchall()[0]
        cur.execute("select receipt_no from tran_details where gr_no={}".format(grval))
        receipt_no = cur.fetchall()[0]
        for i in receipt_no:
            print(i)
            cur.execute("select * from fee_tran where receipt_no={}".format(i))
            fee_tran_data = cur.fetchall()[0]
            cur.execute("select * from tran_details where RECEIPT_NO={}".format(i))
            tran_details = cur.fetchall()[0]
            cur.execute("select * from std_fees where std={}".format(tran_details[6]))
            std_fees_data  = cur.fetchall()[0]
            cur.execute("select * from exmp_fees where std={}".format(tran_details[6]))
            exmp_data = cur.fetchall()[0]
            print(fee_tran_data[1])
            if(fee_tran_data[1] == 1):
                tree.insert(parent='',index="end",text='',value=("APR_JUN_TUTION",std_fees_data[3],std_fees_data[3]-exmp_data[3],std_fees_data[3]-exmp_data[3],tran_details[14],std_fees_data[3]-pending_data[3]-exmp_data[3]))
                tree.insert(parent='',index="end",text='',value=("APR_JUN_ATITVITY",std_fees_data[4],std_fees_data[4]-exmp_data[4],pending_data[4]-exmp_data[4],tran_details[14],std_fees_data[4]-pending_data[4]-exmp_data[4]))
            else:
                tree.insert(parent='',index="end",text='',value=("APR_JUN_TUTION",std_fees_data[3],std_fees_data[3]-exmp_data[3],pending_data[3]-exmp_data[3],' ',std_fees_data[3]-pending_data[3]-exmp_data[3]))
                tree.insert(parent='',index="end",text='',value=("APR_JUN_ATITVITY",std_fees_data[4],std_fees_data[4]-exmp_data[4],pending_data[4]-exmp_data[4],' ',std_fees_data[4]-pending_data[4]-exmp_data[4]))
            
            if(fee_tran_data[2] == 1):
                tree.insert(parent='',index="end",text='',value=("SEP_JUL_TUTION",std_fees_data[6],std_fees_data[6]-exmp_data[6],pending_data[6]-exmp_data[6],tran_details[14],std_fees_data[6]-pending_data[6]-exmp_data[6]))
                tree.insert(parent='',index="end",text='',value=("SEP_JUL_ACTIVITY",std_fees_data[7],std_fees_data[7]-exmp_data[7],pending_data[7]-exmp_data[7],tran_details[14],std_fees_data[7]-pending_data[7]-exmp_data[7]))
            else:
                tree.insert(parent='',index="end",text='',value=("SEP_JUL_TUTION",std_fees_data[6],std_fees_data[6]-exmp_data[6],pending_data[6]-exmp_data[6],' ',std_fees_data[6]-pending_data[6]-exmp_data[6]))
                tree.insert(parent='',index="end",text='',value=("SEP_JUL_ACTIVITY",std_fees_data[7],std_fees_data[7]-exmp_data[7],pending_data[7]-exmp_data[7],' ',std_fees_data[7]-pending_data[7]-exmp_data[7]))

            if(fee_tran_data[2] == 1):
                tree.insert(parent='',index="end",text='',value=("OCT_DEC_TUTION",std_fees_data[8],std_fees_data[8]-exmp_data[8],pending_data[8]-exmp_data[8],tran_details[14],std_fees_data[8]-pending_data[8]-exmp_data[8]))
                tree.insert(parent='',index="end",text='',value=("OCT_DEC_ACTIVITY",std_fees_data[9],std_fees_data[9]-exmp_data[9],pending_data[9]-exmp_data[9],tran_details[14],std_fees_data[9]-pending_data[9]-exmp_data[9]))
            else:
                tree.insert(parent='',index="end",text='',value=("OCT_DEC_TUTION",std_fees_data[8],std_fees_data[8]-exmp_data[8],pending_data[8]-exmp_data[8],' ',std_fees_data[8]-pending_data[8]-exmp_data[8]))
                tree.insert(parent='',index="end",text='',value=("OCT_DEC_ACTIVITY",std_fees_data[9],std_fees_data[9]-exmp_data[9],pending_data[9]-exmp_data[9],' ',std_fees_data[9]-pending_data[9]-exmp_data[9]))
            
            if(fee_tran_data[2] == 1):
                tree.insert(parent='',index="end",text='',value=("JAN_MAR_TUTION",std_fees_data[10],std_fees_data[10]-exmp_data[10],pending_data[10]-exmp_data[10],tran_details[14],std_fees_data[10]-pending_data[10]-exmp_data[10]))
                tree.insert(parent='',index="end",text='',value=("JAN_MAR_ACTIVITY",std_fees_data[11],std_fees_data[11]-exmp_data[11],pending_data[11]-exmp_data[11],tran_details[14],std_fees_data[11]-pending_data[11]-exmp_data[11]))
            else:
                tree.insert(parent='',index="end",text='',value=("JAN_MAR_TUTION",std_fees_data[10],std_fees_data[10]-exmp_data[10],pending_data[10]-exmp_data[10],' ',std_fees_data[10]-pending_data[10]-exmp_data[10]))
                tree.insert(parent='',index="end",text='',value=("JAN_MAR_ACTIVITY",std_fees_data[11],std_fees_data[11]-exmp_data[11],pending_data[11]-exmp_data[11],' ',std_fees_data[11]-pending_data[11]-exmp_data[11]))

        tree.place(x=50,y=300)
        win.mainloop()
    

    GENERATE_BTN=Button(MAIN_FRAME,text="GENERATE",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=fees_generate)
    GENERATE_BTN.place(x=900,y=500)
    
    SHOW_BTN=Button(MAIN_FRAME,text="SHOW\nFEE DETAIL",height=3,width=20,bg="lightgrey",activebackground='lightgrey',font=('Arial', 13),command=show_fee_details_func)
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
    standard_select_combo['values'] = ('NUR','JR.KG','SR.KG','1','2','3','4','5','6','7','8','9','10','11 COMM','11 SCI','12 COMM','12 SCI')
    AAI1 = IntVar()
    aai_combo = Checkbutton(MAIN_FRAME,text="AAI",variable=AAI1,onvalue=1,offvalue=0,bg="#dda0dd")
    aai_combo.place(x=450,y=105)
 
    standard_select_combo.place(x=200,y=110)


    fees_frame = Frame(MAIN_FRAME, bg="#dda0dd", width=500, height=250,relief=RIDGE)
    fees_frame.place(x=500, y=100)




    def next():
        s = standard_select_combo.get()
        fees_select_label = Label(fees_frame,text="Select Fees :",padx=5,pady=5,bg="#dda0dd",font=("Arial",10,"bold"))
        fees_select_label.place(x=100,y=20)
        fees_select_combo = ttk.Combobox(fees_frame,width=20,font=("Arial",10,"bold"))
        fees_select_combo['values'] = ('TUTION','ACTIVITY','ICARD','ADMISSION','OTHERS')


        def selected(event):
            # SAVE_BTN["state"]=ACTIVE
            if AAI1.get() == 0:
        
                cur.execute("select * from std_fees where std='{}'".format(s))
                data = cur.fetchall()
                if fees_select_combo.get() == 'TUTION':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][3])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][3])
                if fees_select_combo.get() == 'ACTIVITY':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][4])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][4])
                if fees_select_combo.get() == 'ICARD':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][2])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][2])
                if fees_select_combo.get() == 'ADMISSION':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][1])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][1])
                if fees_select_combo.get() == 'OTHERS':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][-1])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][-1])
            else:
                cur.execute("select * from exmp_fees where std='{}'".format(s))
                data = cur.fetchall()
                if fees_select_combo.get() == 'TUTION':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][3])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][3])
                if fees_select_combo.get() == 'ACTIVITY':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][4])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][4])
                if fees_select_combo.get() == 'ICARD':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][2])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][2])
                if fees_select_combo.get() == 'ADMISSION':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][1])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][1])
                if fees_select_combo.get() == 'OTHERS':
                    old_fees_amount_entry.configure(state = "normal")
                    old_fees_amount_entry.delete(0,END)
                    old_fees_amount_entry.insert(0,data[0][-1])
                    old_fees_amount_entry.configure(state = "disabled")
                    new_fees_amount_entry.delete(0,END)
                    new_fees_amount_entry.insert(0,data[0][-1])
            
            
            # elif:


        global fees_edit_save1
        def fees_edit_save1():
            a = new_fees_amount_entry.get()
            b = old_fees_amount_entry.get()
            if(fees_select_combo.get() == 'TUTION'):
                cur.execute("update std_fees set APR_JUN_TUTION={},JUL_SEP_TUTION={},OCT_DEC_TUTION={},JAN_MAR_TUTION={} WHERE STD='{}'".format(a,a,a,a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                print(gr_nos)
                for i1  in gr_nos:
                    cur.execute("select APR_JUN_TUTION,JUL_SEP_TUTION,OCT_DEC_TUTION,JAN_MAR_TUTION from pending_fee_detail where gr_no={}".format(i1[0]))
                    data=cur.fetchall()
                    dict = {'APR_JUN_TUTION':data[0][0],
                            'JUL_SEP_TUTION':data[0][1],
                            'OCT_DEC_TUTION':data[0][2],
                            'JAN_MAR_TUTION':data[0][3]
                            }
                    for i,j in dict.items():
                        print("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                        cur.execute("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                    mydb.commit()
            if(fees_select_combo.get() == 'ACTIVITY'):
                cur.execute("update std_fees set APR_JUN_ATITVITY={},JUL_SEP_ACTIVITY={},OCT_DEC_ACTIVITY={},JAN_MAR_ACTIVITY={} WHERE STD='{}'".format(a,a,a,a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("select APR_JUN_ATITVITY,JUL_SEP_ACTIVITY,OCT_DEC_ACTIVITY,JAN_MAR_ACTIVITY from pending_fee_detail where gr_no={}".format(i1[0]))
                    data=cur.fetchall()
                    dict = {'APR_JUN_ATITVITY':data[0][0],
                            'JUL_SEP_ACTIVITY':data[0][1],
                            'OCT_DEC_ACTIVITY':data[0][2],
                            'JAN_MAR_ACTIVITY':data[0][3]
                            }
                    for i,j in dict.items():
                        cur.execute("select {} from pending_fee_detail where gr_no={}".format(i,i1[0]))
                        data = cur.fetchall()[0]
                        if(data[0] == 0):
                            pass
                        else:
                            cur.execute("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                    mydb.commit()
                mydb.commit()
            if(fees_select_combo.get() == 'ADMISSION'):
                cur.execute("update std_fees set ADMISSION_FEE={} WHERE STD='{}'".format(a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("select admission_fee from pending_fee_detail where gr_no={}".format(i1[0]))
                    data = cur.fetchall()[0]
                    if (data[0] == 0):
                        pass
                    else:
                        cur.execute("update pending_fee_detail set ADMISSION_FEE={} where gr_no={}".format(a,i1[0]))
                    mydb.commit()
                mydb.commit()
                
            if(fees_select_combo.get() == 'ICARD'):
                cur.execute("update std_fees set ICARD={} WHERE STD='{}'".format(a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                # print(gr_nos)
                for i1  in gr_nos:
                    cur.execute("select ICARD from pending_fee_detail where gr_no={}".format(i1[0]))
                    data = cur.fetchall()[0]
                    if (data[0] == 0):
                        pass
                    else:
                        cur.execute("update pending_fee_detail set ICARD={} where gr_no={}".format(a,i1[0]))
                    mydb.commit()
                mydb.commit()

            if(fees_select_combo.get() == 'OTHERS'):
                cur.execute("update std_fees set OTHERS1={} WHERE STD='{}'".format(a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("select others from pending_fee_detail where gr_no={}".format(i1[0]))
                    data = cur.fetchall()[0]
                    if (data[0] == 0):
                        pass
                    else:
                        cur.execute("update pending_fee_detail set OTHERS={} where gr_no={}".format(a,i1[0]))
                    mydb.commit()
            mydb.commit()
            FEES_EDIT_FUNCTION()
        fees_select_combo.bind('<<ComboboxSelected>>',selected)
        fees_select_combo.place(x=200,y=20)
        mydb.commit()
        
    
    
        global fees_edit_save
        def fees_edit_save():
            a = new_fees_amount_entry.get()
            b = old_fees_amount_entry.get()
            if(fees_select_combo.get() == 'TUTION'):
                cur.execute("update exmp_fees set APR_JUN_TUTION={},JUL_SEP_TUTION={},OCT_DEC_TUTION={},JAN_MAR_TUTION={} WHERE STD='{}'".format(a,a,a,a,s))
                print("update exmp_fees set APR_JUN_TUTION={},JUL_SEP_TUTION={},OCT_DEC_TUTION={},JAN_MAR_TUTION={} WHERE STD='{}'".format(a,a,a,a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                print(gr_nos)
                for i1  in gr_nos:
                    cur.execute("select APR_JUN_TUTION,JUL_SEP_TUTION,OCT_DEC_TUTION,JAN_MAR_TUTION from pending_fee_detail where gr_no={}".format(i1[0]))
                    data=cur.fetchall()
                    dict = {'APR_JUN_TUTION':data[0][0],
                            'JUL_SEP_TUTION':data[0][1],
                            'OCT_DEC_TUTION':data[0][2],
                            'JAN_MAR_TUTION':data[0][3]
                            }
                    for i,j in dict.items():
                        print("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                        cur.execute("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                    mydb.commit()
                mydb.commit()
            if(fees_select_combo.get() == 'ACTIVITY'):
                cur.execute("update exmp_fees set APR_JUN_ATITVITY={},JUL_SEP_ACTIVITY={},OCT_DEC_ACTIVITY={},JAN_MAR_ACTIVITY={} WHERE STD='{}'".format(a,a,a,a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("select APR_JUN_ATITVITY,JUL_SEP_ACTIVITY,OCT_DEC_ACTIVITY,JAN_MAR_ACTIVITY from pending_fee_detail where gr_no={}".format(i1[0]))
                    data=cur.fetchall()
                    dict = {'APR_JUN_ATITVITY':data[0][0],
                            'JUL_SEP_ACTIVITY':data[0][1],
                            'OCT_DEC_ACTIVITY':data[0][2],
                            'JAN_MAR_ACTIVITY':data[0][3]
                            }
                    for i,j in dict.items():
                        # print("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                        cur.execute("update pending_fee_detail set {}={} where gr_no={}".format(i,a,i1[0]))
                    mydb.commit()
                mydb.commit()
            if(fees_select_combo.get() == 'ADMISSION'):
                cur.execute("update exmp_fees set ADMISSION_FEE={} WHERE STD='{}'".format(a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("update pending_fee_detail set ADMISSION_FEE={} where gr_no={}".format(a,i1[0]))
                    mydb.commit()
                mydb.commit()
                
            if(fees_select_combo.get() == 'ICARD'):
                cur.execute("update exmp_fees set ICARD={} WHERE STD='{}'".format(a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("update pending_fee_detail set ICARD={} where gr_no={}".format(a,i1[0]))
                    mydb.commit()
                mydb.commit()

            if(fees_select_combo.get() == 'OTHERS'):
                cur.execute("update exmp_fees set OTHERS1={} WHERE STD='{}'".format(a,s))
                cur.execute("select gr_no from academic_detail where curr_std='{}'".format(s))
                gr_nos = cur.fetchall()
                for i1  in gr_nos:
                    cur.execute("update pending_fee_detail set OTHERS={} where gr_no={}".format(a,i1[0]))
                    mydb.commit()
                mydb.commit()
            FEES_EDIT_FUNCTION()
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
        if AAI1.get() == 1:
        
            SAVE_BTN=Button(MAIN_FRAME,text="SAVE",height=3,width=20,bg="lightgrey",command=fees_edit_save,activebackground='lightgrey',font=('Arial', 10))
            SAVE_BTN.place(x=1100,y=500)
        else:
            SAVE_BTN=Button(MAIN_FRAME,text="SAVE",height=3,width=20,bg="lightgrey",command=fees_edit_save1,activebackground='lightgrey',font=('Arial', 10))
            SAVE_BTN.place(x=1100,y=500)
        mydb.commit()
        # SAVE_BTN["state"]=DISABLED

    


    SUBMIT_BTN=Button(MAIN_FRAME,text="Submit",height=1,width=19,bg="lightgrey",activebackground='lightgrey',font=('Arial', 10),command=next)
    SUBMIT_BTN.place(x=200,y=160)










global FEES_REPORT_FUNCTION
def FEES_REPORT_FUNCTION():
    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy() 

    import csv
    current_date=datetime.datetime.today().strftime('%d-%m-%Y')
    f1=open("report_{}.csv".format(current_date),"w",newline="\n")
    wrt=csv.writer(f1)
    wrt.writerow(["RECIEPT NO","DATE","GR_NO","NAME","PAY TYPE","CHEQUE_NO","BANK NAME","TOTAL"])
    print(current_date)
    cur.execute("select RECEIPT_NO,date1,gr_no,name,paymode,cheque_no,bank,grand_total from tran_details where date1='{}'".format(current_date))
    data_report = cur.fetchall()
    for i in data_report:
        wrt.writerow(i)


    f2 = open(r"REPORTS\gr_report.csv",'w',newline="\n")
    wrt = csv.writer(f2)
    wrt.writerow(["CLASS","DIVISION","TOTAL"])
    cur.execute("select curr_std,division,count(gr_no) as total from academic_detail where active1=1 group by curr_std,division order by curr_std")
    data_report = cur.fetchall()
    for i in data_report:
        wrt.writerow(i)
    f2.close()

    f3 = open(r"REPORTS\male_female.csv",'w',newline="\n")
    wrt = csv.writer(f3)
    wrt.writerow(["CLASS","DIVISION","SEX","TOTAL"])
    cur.execute("select academic_detail.curr_std,academic_detail.division,gr_details.sex,count(gr_details.sex) as total from gr_details,academic_detail where academic_detail.active1=1 group by academic_detail.curr_std,academic_detail.division,gr_details.sex order by academic_detail.curr_std,academic_detail.division")
    data_report = cur.fetchall()
    for i in data_report:
        wrt.writerow(i)
    f3.close()

    f4 = open(r"REPORTS\caste_report.csv",'w',newline="\n")
    wrt = csv.writer(f4)
    wrt.writerow(["CLASS","DIVISION","CASTE","TOTAL"])
    cur.execute("select academic_detail.curr_std,academic_detail.division,gr_details.caste,count(gr_details.caste) as total from gr_details,academic_detail where academic_detail.active1=1 group by academic_detail.curr_std,academic_detail.division,gr_details.caste order by academic_detail.curr_std,academic_detail.division")
    data_report = cur.fetchall()    
    for i in data_report:
        wrt.writerow(i)
    f4.close()

    f5 = open(r"REPORTS\new_admission.csv",'w',newline="\n")
    wrt = csv.writer(f5)
    wrt.writerow(["GR NO","NAME","FATHER","SURNAME","CURR STD","DIVISION"])
    cur.execute("select gr_details.gr_no,gr_details.name,gr_details.father,gr_details.surname,academic_detail.curr_std,academic_detail.division from gr_details,academic_detail where gr_details.gr_no>4575 and gr_details.gr_no=academic_detail.gr_no and academic_detail.active1=1")
    data_report = cur.fetchall()    
    for i in data_report:
        wrt.writerow(i)
    f5.close()










def LIBRARY_FUNCTION():

        # text_Q1="LIBRARY"
        # myobj = gTTS(text=text_Q1, slow=False)
        # myobj.save(r"AUDIOS\library.mp3")
        #pygame.mixer.init()
        #pygame.mixer.music.load(r"AUDIOS\library.mp3")
        #pygame.mixer.music.play(loops=0)


    for widget in MENU_FRAME2.winfo_children():
        widget.destroy()
    for widget in MAIN_FRAME.winfo_children():
        widget.destroy()  

    def LIB_1():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()

        MAIN_FRAME.configure(bg="#c1e0b7")

        organisation_lbl=Label(MAIN_FRAME,text="Organisation :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        organisation_lbl.place(x=55,y=40)
        organisation_var=StringVar()
        organisation_combo = ttk.Combobox(MAIN_FRAME,width=27,textvariable = organisation_var)
        organisation_combo['values'] = ('SEBC','ST','GEN','SC')
        organisation_combo.place(x=160,y=45)


        GR_label = Label(MAIN_FRAME,text="GR :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        GR_label.place(x=115,y=80)
        GR_entry = Entry(MAIN_FRAME,width=15,font=("Arial",10,"bold"))
        GR_entry.place(x=160,y=85)


        mobile_no_label = Label(MAIN_FRAME,text="Mobile :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        mobile_no_label.place(x=295,y=80)
        mobile_no_entry = Entry(MAIN_FRAME,width=15,font=("Arial",10,"bold"))
        mobile_no_entry.place(x=365,y=85)


        
        standard_label = Label(MAIN_FRAME,text="Std :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        standard_label.place(x=510,y=80)
        standard_entry = Entry(MAIN_FRAME,width=15,font=("Arial",10,"bold"))
        standard_entry.place(x=555,y=85)


        
        roll_no_label = Label(MAIN_FRAME,text="Roll No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        roll_no_label.place(x=705,y=80)
        roll_no_entry = Entry(MAIN_FRAME,width=15,font=("Arial",10,"bold"))
        roll_no_entry.place(x=775,y=85)

        
        Name_label = Label(MAIN_FRAME,text="Name :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Name_label.place(x=95,y=120)
        Name_entry = Entry(MAIN_FRAME,width=25,font=("Arial",10,"bold"))
        Name_entry.place(x=160,y=125)






        book_issue_frame=Frame(MAIN_FRAME,height=220,width=500,bg="#c1e0b7",borderwidth=4,relief=RIDGE)
        book_issue_frame.place(x=50,y=170)


        accession_no_label = Label(book_issue_frame,text="Accession No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        accession_no_label.place(x=15,y=15)
        accession_no_entry = Entry(book_issue_frame,width=20,font=("Arial",9,"bold"))
        accession_no_entry.place(x=125,y=20)
        
        Book_name_label = Label(book_issue_frame,text="Book Name :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        Book_name_label.place(x=25,y=55)
        Book_name_entry = Entry(book_issue_frame,width=45,font=("Arial",9,"bold"))
        Book_name_entry.place(x=125,y=60)


        issue_dt_lbl=Label(book_issue_frame,text="Issue Date : ",bg="#c1e0b7",font=("Arial",9,"bold"))
        issue_dt_lbl.place(x=35,y=95)
        issue_dt_entry_tab=DateEntry(book_issue_frame,selectmode="day",date_pattern="dd-mm-y",font=("Arial",9,"bold"),width=10)
        issue_dt_entry_tab.place(x=125,y=95)

        # to_date_lbl=Label(book_issue_frame,text="Issue Date : ",bg="#c1e0b7",font=("Arial",9,"bold"))
        # to_date_lbl.place(x=252,y=95)
        # to_date_entry_tab=DateEntry(book_issue_frame,selectmode="day",date_pattern="dd-mm-y",font=("Arial",9,"bold"),width=10)
        # to_date_entry_tab.place(x=345,y=95)

            
        Issue_remark_label = Label(book_issue_frame,text="Issue Remark :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        Issue_remark_label.place(x=10,y=130)
        Issue_remark_entry = Entry(book_issue_frame,width=45,font=("Arial",9,"bold"))
        Issue_remark_entry.place(x=125,y=135)

        








        book_return_frame=Frame(MAIN_FRAME,height=220,width=500,bg="#c1e0b7",borderwidth=4,relief=RIDGE)
        book_return_frame.place(x=700,y=170)

        return_dt_lbl=Label(book_return_frame,text="Return Date : ",bg="#c1e0b7",font=("Arial",9,"bold"))
        return_dt_lbl.place(x=25,y=15)
        return_dt_entry_tab=DateEntry(book_return_frame,selectmode="day",date_pattern="dd-mm-y",font=("Arial",9,"bold"),width=10)
        return_dt_entry_tab.place(x=125,y=15)

        penalty_days_label = Label(book_return_frame,text="Penalty Days :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        penalty_days_label.place(x=20,y=45)
        penalty_days_entry = Entry(book_return_frame,width=20,font=("Arial",9,"bold"))
        penalty_days_entry.place(x=125,y=50)

        penalty_days_label = Label(book_return_frame,text="Penalty Rate :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        penalty_days_label.place(x=300,y=25)
        penalty_rate_entry = Entry(book_return_frame,width=20,font=("Arial",9,"bold"))
        penalty_rate_entry.place(x=305,y=50)

        penalty_amount_label = Label(book_return_frame,text="Penalty Amount :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        penalty_amount_label.place(x=5,y=80)
        penalty_amount_entry = Entry(book_return_frame,width=20,font=("Arial",9,"bold"))
        penalty_amount_entry.place(x=125,y=85)

        return_remark_label = Label(book_return_frame,text="Return Remark :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",9,"bold"))
        return_remark_label.place(x=5,y=115)
        return_remark_entry = Entry(book_return_frame,width=45,font=("Arial",9,"bold"))
        return_remark_entry.place(x=125,y=120)
            
        RETURN_BTN=Button(book_return_frame,text="Return",height=1,width=12,bg="lightgrey",activebackground='lightgrey',font=('Arial',9,"bold"))
        RETURN_BTN.place(x=180,y=170)

        RETURN_DELETE_BTN=Button(book_return_frame,text="Return Delete",height=1,width=12,bg="lightgrey",activebackground='lightgrey',font=('Arial',9,"bold"))
        RETURN_DELETE_BTN.place(x=320,y=170)


        
        wrapper1=Frame(MAIN_FRAME,height=150,width=1170)
        wrapper1.place(x=50,y=415)
        style = ttk.Style()
        style.theme_use('clam')
        trv=ttk.Treeview(wrapper1,columns=(1,2,3,4,5),show="headings",height="5")

        trv.pack(side=LEFT)

        trv.heading("#1",text="Accession No")
        trv.heading("#2",text="Book Name")
        trv.heading("#3",text="Issue Date")
        trv.heading("#4",text="Issue Upto")
        trv.heading("#5",text="Return Date")

        trv.column("#1",width=230)
        trv.column("#2",width=350)
        trv.column("#3",width=180)
        trv.column("#4",width=180)
        trv.column("#5",width=180)
        


        y_scroll=Scrollbar(wrapper1,orient="vertical",command=trv.yview)
        y_scroll.pack(side=RIGHT,fill='y')
        trv.configure(yscrollcommand=y_scroll.set)

        def data_entry_func(e):
            grval = GR_entry.get()
            mobileval = 0
            cur.execute("select name,roll_no")
        GR_entry.bind("<Return>",data_entry_func)

        def issue_book():
            lib_records = []
            lib_records.append(organisation_combo.get())#1
            lib_records.append(GR_entry.get())#2
            lib_records.append(mobile_no_entry.get())#3
            lib_records.append(standard_entry.get())#4
            lib_records.append(roll_no_entry.get())#5
            lib_records.append(Name_entry.get())#6
            lib_records.append(accession_no_entry.get())#7
            lib_records.append(Book_name_entry.get())#8
            lib_records.append(issue_dt_entry_tab.get())#9
            lib_records.append(Issue_remark_entry.get())#10
            lib_records.append(return_dt_entry_tab.get())#11
            lib_records.append(penalty_days_entry.get())#12
            lib_records.append(penalty_rate_entry.get())#13
            lib_records.append(penalty_amount_entry.get())#14
            lib_records.append(return_remark_entry.get())#15
            cur.execute("insert into lib_values values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",lib_records)
            cur.execute("insert into issued values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",lib_records)
            mydb.commit()
            LIB_1()
        
        def issue_delete():
            cur.execute("delete from issued where gr_no=%s",(GR_entry.get()))
            mydb.commit()
            LIB_1()
        
        ISSUE_BTN=Button(book_issue_frame,text="Issue",height=1,width=12,bg="lightgrey",activebackground='lightgrey',font=('Arial',9,"bold"),command=issue_book)
        ISSUE_BTN.place(x=180,y=170)

        ISSUE_DELETE_BTN=Button(book_issue_frame,text="Issue Delete",height=1,width=12,bg="lightgrey",activebackground='lightgrey',font=('Arial',9,"bold"),command=issue_delete)
        ISSUE_DELETE_BTN.place(x=320,y=170)




    LIBRARY_1=Button(MENU_FRAME2,text="LIBRARY 1",command = LIB_1)
    LIBRARY_1.place(x=20,y=20)





    def LIB_2():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()

        MAIN_FRAME.configure(bg="#c1e0b7")

        Accession_No_label = Label(MAIN_FRAME,text="Accession No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Accession_No_label.place(x=100,y=40)
        Accession_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Accession_No_entry.place(x=220,y=45)



        Book_No_label = Label(MAIN_FRAME,text="Book No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Book_No_label.place(x=130,y=80)
        Book_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Book_No_entry.place(x=220,y=85)


        Class_No_label = Label(MAIN_FRAME,text="Class No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Class_No_label.place(x=463,y=80)
        Class_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Class_No_entry.place(x=550,y=85)


        ISBN_No_label = Label(MAIN_FRAME,text="ISBN No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        ISBN_No_label.place(x=800,y=80)
        ISBN_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        ISBN_No_entry.place(x=890,y=85)


        
        Book_Name_label = Label(MAIN_FRAME,text="Book Name :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Book_Name_label.place(x=110,y=120)
        Book_Name_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Book_Name_entry.place(x=220,y=125)



        Author_label = Label(MAIN_FRAME,text="Author :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Author_label.place(x=140,y=160)
        Author_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Author_entry.place(x=220,y=165)


        

        Rec_No_label = Label(MAIN_FRAME,text="Rec No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Rec_No_label.place(x=807,y=160)
        Rec_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Rec_No_entry.place(x=890,y=165)


        
        Publisher_label = Label(MAIN_FRAME,text="Publisher :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Publisher_label.place(x=122,y=200)
        Publisher_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Publisher_entry.place(x=220,y=205)


        
        Sub_Rec_No_label = Label(MAIN_FRAME,text="Sub Rec No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Sub_Rec_No_label.place(x=777,y=200)
        Sub_Rec_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Sub_Rec_No_entry.place(x=890,y=205)


        
        Book_Category_label = Label(MAIN_FRAME,text="Book Category :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Book_Category_label.place(x=88,y=240)
        Book_Category_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Book_Category_entry.place(x=220,y=245)



        Price_label = Label(MAIN_FRAME,text="Price :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Price_label.place(x=816,y=240)
        Price_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Price_entry.place(x=890,y=245)


                
        Subject_label = Label(MAIN_FRAME,text="Subject :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Subject_label.place(x=133,y=280)
        Subject_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Subject_entry.place(x=220,y=285)


        
        Stock_label = Label(MAIN_FRAME,text="Stock :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Stock_label.place(x=815,y=280)
        Stock_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Stock_entry.place(x=890,y=285)

                

        Book_Language_label = Label(MAIN_FRAME,text="Book Language :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Book_Language_label.place(x=81,y=320)
        Book_Language_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Book_Language_entry.place(x=220,y=325)


        Currency_label = Label(MAIN_FRAME,text="Currency :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Currency_label.place(x=792,y=320)
        Currency_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Currency_entry.place(x=890,y=325)



        PUR_DON_label = Label(MAIN_FRAME,text="Purchased/Donated :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        PUR_DON_label.place(x=58,y=360)
        PUR_DON_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        PUR_DON_entry.place(x=220,y=365)


        
        Date_label = Label(MAIN_FRAME,text="Date :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Date_label.place(x=819,y=360)
        Date_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Date_entry.place(x=890,y=365)


        
        Book_Cancelvalue=IntVar()
        Book_Cancel_check=Checkbutton(MAIN_FRAME,text="Book Cancel",onvalue=1,offvalue=0,bg="#c1e0b7",activebackground="#c1e0b7")
        Book_Cancel_check.place(x=1100,y=365)



        Edition_label = Label(MAIN_FRAME,text="Edition :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Edition_label.place(x=138,y=400)
        Edition_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Edition_entry.place(x=220,y=405)


        Bill_No_Date_label = Label(MAIN_FRAME,text="Bill No / Date :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Bill_No_Date_label.place(x=764,y=400)
        Bill_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Bill_No_entry.place(x=890,y=405)
        Bill_Date_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Bill_Date_entry.place(x=1100,y=405)


        
        Authority_label = Label(MAIN_FRAME,text="Authority :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Authority_label.place(x=125,y=440)
        Authority_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Authority_entry.place(x=220,y=445)


        Voucher_No_Date_label = Label(MAIN_FRAME,text="Voucher No / Date :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Voucher_No_Date_label.place(x=734,y=440)
        Voucher_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Voucher_No_entry.place(x=890,y=445)
        Voucher_Date_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Voucher_Date_entry.place(x=1100,y=445)


        Issueablevalue=IntVar()
        Issueable_check=Checkbutton(MAIN_FRAME,text="Issueable",onvalue=1,offvalue=0,bg="#c1e0b7",activebackground="#c1e0b7")
        Issueable_check.place(x=220,y=485)


        Remark_label = Label(MAIN_FRAME,text="Remark :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Remark_label.place(x=125,y=520)
        Remark_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Remark_entry.place(x=220,y=525)




    LIBRARY_2=Button(MENU_FRAME2,text="LIBRARY 2",command = LIB_2)
    LIBRARY_2.place(x=20,y=100)

















    def LIB_3():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()

        MAIN_FRAME.configure(bg="#c1e0b7")


        
        Select_report_label = Label(MAIN_FRAME,text="Select Report :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Select_report_label.place(x=335,y=55)
        Select_report_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Select_report_entry.place(x=450,y=60)



        Author_label = Label(MAIN_FRAME,text="Author :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Author_label.place(x=335,y=90)
        Author_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Author_entry.place(x=450,y=95)


        
        Category_label = Label(MAIN_FRAME,text="Category :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Category_label.place(x=335,y=125)
        Category_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Category_entry.place(x=450,y=130)


                
        Language_label = Label(MAIN_FRAME,text="Language :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Language_label.place(x=335,y=160)
        Language_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Language_entry.place(x=450,y=165)


                        
        Book_label = Label(MAIN_FRAME,text="Book :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Book_label.place(x=335,y=195)
        Book_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Book_entry.place(x=450,y=200)


                                
        Issueable_label = Label(MAIN_FRAME,text="Issueable :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Issueable_label.place(x=335,y=230)
        Issueable_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Issueable_entry.place(x=450,y=235)


                

        Rec_No_label = Label(MAIN_FRAME,text="Rec No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Rec_No_label.place(x=335,y=265)
        Rec_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Rec_No_entry.place(x=450,y=270)


        Sub_Rec_No_label = Label(MAIN_FRAME,text="Sub Rec No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Sub_Rec_No_label.place(x=678,y=265)
        Sub_Rec_No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Sub_Rec_No_entry.place(x=778,y=270)



        Price_from_label = Label(MAIN_FRAME,text="Price From:",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Price_from_label.place(x=335,y=300)
        Price_from_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Price_from_entry.place(x=450,y=305)


        Price_to_label = Label(MAIN_FRAME,text="Price To :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Price_to_label.place(x=678,y=300)
        Price_to_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Price_to_entry.place(x=778,y=305)



        Quantity_from_label = Label(MAIN_FRAME,text="Quantity From:",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Quantity_from_label.place(x=335,y=335)
        Quantity_from_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Quantity_from_entry.place(x=450,y=340)


        Quantity_to_label = Label(MAIN_FRAME,text="Quantity To :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Quantity_to_label.place(x=678,y=335)
        Quantity_to_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Quantity_to_entry.place(x=778,y=340)



        No_label = Label(MAIN_FRAME,text="No :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        No_label.place(x=335,y=370)
        No_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        No_entry.place(x=450,y=375)



        
        Date_from_label = Label(MAIN_FRAME,text="Date From:",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Date_from_label.place(x=335,y=405)
        Date_from_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Date_from_entry.place(x=450,y=410)


        Date_to_label = Label(MAIN_FRAME,text="Date To :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Date_to_label.place(x=678,y=405)
        Date_to_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Date_to_entry.place(x=778,y=410)


        
        Reader_Type_label = Label(MAIN_FRAME,text="Reader Type :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Reader_Type_label.place(x=335,y=440)
        Reader_Type_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Reader_Type_entry.place(x=450,y=445)



        Standard_label = Label(MAIN_FRAME,text="Standard :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Standard_label.place(x=335,y=475)
        Standard_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Standard_entry.place(x=450,y=480)


        Division_label = Label(MAIN_FRAME,text="Division :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Division_label.place(x=678,y=475)
        Division_entry = Entry(MAIN_FRAME,width=23,font=("Arial",10,"bold"))
        Division_entry.place(x=778,y=480)



        Reader_label = Label(MAIN_FRAME,text="Reader :",padx=5,pady=5,bg="#c1e0b7",font=("Arial",10,"bold"))
        Reader_label.place(x=335,y=505)
        Reader_entry = Entry(MAIN_FRAME,width=70,font=("Arial",10,"bold"))
        Reader_entry.place(x=450,y=510)







    LIBRARY_3=Button(MENU_FRAME2,text="LIBRARY 3",command = LIB_3)
    LIBRARY_3.place(x=20,y=180)










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



    #-------------------------LABELS---------------------------------

    numlbl=Label(MAIN_FRAME,text="No. : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    numlbl.place(x=340,y=150,anchor=E)


    grnlbl=Label(MAIN_FRAME,text="Gr No : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    grnlbl.place(x=340,y=200,anchor=E)

    namelbl=Label(MAIN_FRAME,text="Name : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    namelbl.place(x=340,y=250,anchor=E)

    father_namelbl=Label(MAIN_FRAME,text="Father Name : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    father_namelbl.place(x=340,y=300,anchor=E)


    Addresslbl=Label(MAIN_FRAME,text="Address : ",bg='#dda0dd',font=("ariel", 15, "bold"))
    Addresslbl.place(x=340,y=350,anchor=E)
    Addresslbl=Label(MAIN_FRAME,text=" ",bg='#dda0dd',font=("ariel", 15, "bold"))
    Addresslbl.place(x=340,y=400,anchor=E)

    dtlbl=Label(MAIN_FRAME,text="Date : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    dtlbl.place(x=780,y=200,anchor=E)

    stdlbl=Label(MAIN_FRAME,text="Standard :",bg="#dda0dd",font=("ariel", 15, "bold"))
    stdlbl.place(x=780,y=250,anchor=E)

    dtbirthlbl=Label(MAIN_FRAME,text="Birth Date : ",bg="#dda0dd",font=("ariel", 15, "bold"))
    dtbirthlbl.place(x=780,y=300,anchor=E)



    # #-------------------------------ENTRY TABS----------------------------------

    num_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    num_entry_tab.place(x=350,y=135)
    cur.execute("select max(no) from bonafide")
    last_no_bonafide = cur.fetchall()[0][0]
    # print(last_no_bonafide)
    num_entry_tab.insert(0,last_no_bonafide+1)


    grn_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    grn_entry_tab.place(x=350,y=185)

    name_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    name_entry_tab.place(x=350,y=235)

    father_name_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    father_name_entry_tab.place(x=350,y=285)

    address_entry_tab1=Entry(MAIN_FRAME,width=60,font=("ariel", 15, "bold"))
    address_entry_tab1.place(x=350,y=335)
    address_entry_tab2=Entry(MAIN_FRAME,width=60,font=("ariel", 15, "bold"))
    address_entry_tab2.place(x=350,y=385)

        
    dt_entry_tab=DateEntry(MAIN_FRAME,selectmode="day",date_pattern="dd-mm-y",font=("ariel", 15, "bold"),width=18)
    dt_entry_tab.place(x=790,y=185)

    std_entry_tab=Entry(MAIN_FRAME,font=("ariel", 15, "bold"))
    std_entry_tab.place(x=790,y=235)

    dt_birth_entry_tab=DateEntry(MAIN_FRAME,selectmode="day",date_pattern="dd-mm-y",font=("ariel", 15, "bold"),width=18)
    dt_birth_entry_tab.place(x=790,y=285)


    def entry_bonafide(e):
        gr_no_value = grn_entry_tab.get()

        cur.execute("select NAME,FATHER,SURNAME,BIRTH_DATE from gr_details where gr_no={}".format(gr_no_value))
        data_gr_bonafide=cur.fetchall()

        cur.execute("select curr_std,curr_year from academic_detail where gr_no={}".format(gr_no_value))
        data_academic_bonafide=cur.fetchall()

        cur.execute("select address1,address2 from other_detail where gr_no={}".format(gr_no_value))
        data_other_bonafide=cur.fetchall()

        name_entry_tab.insert(0,data_gr_bonafide[0][0])
        father_name_entry_tab.insert(0,data_gr_bonafide[0][1])
        std_entry_tab.insert(0,data_academic_bonafide[0][0])
        address_entry_tab1.insert(0,data_other_bonafide[0][0])
        address_entry_tab2.insert(0,data_other_bonafide[0][1])
        dt_birth_entry_tab.set_date(datetime.datetime.strptime(data_gr_bonafide[0][3],'%d-%m-%Y').date())


        

    grn_entry_tab.bind("<Return>",entry_bonafide)

    def cert():
        num_value = num_entry_tab.get()
        gr_no_value = grn_entry_tab.get()
        name_value = name_entry_tab.get()
        date_value = dt_entry_tab.get()
        date_birth_value = dt_birth_entry_tab.get()
        std_value = std_entry_tab.get()



        from datetime import date
        from num2words import num2words
        
        date1 = date_birth_value
        date1 = date1.split("-")
        a = date(day=int(date1[0]), month=int(date1[1]), year=int(date1[2])).strftime('%A %d %B %Y')
        a = a.split(" ")
        a = a[1:]
        a[0] = num2words(int(a[0]))
        a[2] = num2words(int(a[2]))
        # print(a[0][0])
        date = a[0]
        month = a[1]
        year = a[2]
        year_list = year.split(" ")
        a = []
        for i in range(len(year_list)):
            year_list[i] = year_list[i].title()
            if(year_list[i] == "And"):
                pass
            else:
                a.append(year_list[i])
        date = date.title()
        words = date + " "+month+" "+" ".join(a)
        date_birth_in_words_value = words
    







        cur.execute("select NAME,FATHER,SURNAME,BIRTH_DATE from gr_details where gr_no={}".format(gr_no_value))
        data_gr_bonafide=cur.fetchall()

        
        cur.execute("select curr_std,curr_year from academic_detail where gr_no={}".format(gr_no_value))
        data_academic_bonafide=cur.fetchall()

        cur.execute("select address1,address2 from other_detail where gr_no={}".format(gr_no_value))
        data_other_bonafide=cur.fetchall()

        print(data_gr_bonafide[0])
        print(data_academic_bonafide[0])
        print(data_other_bonafide[0])


        q = "insert into bonafide values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(num_value,data_gr_bonafide[0][0],data_gr_bonafide[0][1],data_gr_bonafide[0][2],data_academic_bonafide[0][0],data_academic_bonafide[0][1],gr_no_value,data_gr_bonafide[0][3],data_gr_bonafide[0][3],data_other_bonafide[0][0],data_other_bonafide[0][1])
        cur.execute(q)
        mydb.commit()

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import inch

        from reportlab.lib.pagesizes import letter, A4
        #------------------------------------------------
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
        pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))



        my_path1= "CERTIFICATES\\ll.pdf"
        c1=canvas.Canvas(my_path1,pagesize=A4)
        c1.translate(inch,inch)
        c1.setLineWidth(2)
        c1.setStrokeColorRGB(0,0,0)
        c1.rect(-0.8*inch,3.7*inch,7.9*inch,6.5*inch,fill=0)
        c1.drawImage(r"CERTIFICATES\shool_logo.png",-40, 630)
        c1.setFont("VeraBd",18)
        c1.drawString(100,700,"AIRPORT SCHOOL - AHMEDABAD") 
        c1.setFont("Vera",9)
        c1.drawString(68,680,"AAI RESIDENTIAL QUARTERS, OPP. S.V.P.I. AIRPORT, SARDARNAGAR, AHMEDABAD- 382475")
        c1.drawString(185,667,"PHONE : 079-22864175, 22869014")
        c1.setFont("VeraBd",10)
        c1.drawString(218,650,"C.B.S.E BOARD")
        c1.drawString(187,630,"CBSE Affiliation No.430133")
        c1.line(-57,620,510,620)
        c1.setLineWidth(2)
        c1.setFont("VeraBI",13)
        c1.drawString(140,590,"BONAFIDE CERTIFICATE")
        c1.line(138,588,315,588)
        c1.setLineWidth(2)


        NAME_CERT = name_value
        total_name = 30

        left_side = 15
        right_side = 15

        length_name = len(NAME_CERT)
        lenth_name_remaining = total_name-length_name
        each_side = lenth_name_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(30,557," "*left_side+NAME_CERT+" "*right_side)


        c1.setFont("VeraIt",10)
        c1.drawString(-40,555,"Certified that __________________________________ S/O")
        c1.setFont("VeraBd",20)
        c1.drawString(221,553,"/")

        
        FATHER_CERT = data_gr_bonafide[0][1]
        total_father = 34

        left_side = 17
        right_side = 17

        length_father = len(FATHER_CERT)
        lenth_father_remaining = total_father-length_father
        each_side = lenth_father_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(252,557," "*left_side+FATHER_CERT+" "*right_side)


        c1.setFont("VeraIt",10)
        c1.drawString(225,555," D/O __________________________________ is a")

        
        STD_CERT = data_academic_bonafide[0][0]
        total_std = 18

        left_side = 9
        right_side = 9

        length_std = len(STD_CERT)
        lenth_std_remaining = total_std-length_std
        each_side = lenth_std_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(200,527," "*left_side+STD_CERT+" "*right_side)



        YEAR_CERT = data_academic_bonafide[0][1]
        total_year = 18

        left_side = 9
        right_side = 9

        length_year = len(str(YEAR_CERT))
        lenth_year_remaining = total_year-length_year
        each_side = lenth_year_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(350,527," "*left_side+str(YEAR_CERT)+" "*right_side)


        c1.setFont("VeraIt",10)
        c1.drawString(-40,525,"bonafide student of the school studying in Std : __________________ in the year __________________.")
        c1.drawString(-40,495,"As per the school records his / her details are :")

        GR_CERT = gr_no_value
        total_gr = 30

        left_side = 15
        right_side = 15

        length_gr = len(str(GR_CERT))
        lenth_gr_remaining = total_gr-length_gr
        each_side = lenth_gr_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(10,465," "*left_side+str(GR_CERT)+" "*right_side)
        

        c1.drawString(-40,465,"G.R.No. : ______________________________ ")



        DOB_CERT = data_gr_bonafide[0][3]
        total_dob = 28

        left_side = 14
        right_side = 14

        length_dob = len(str(DOB_CERT))
        lenth_dob_remaining = total_dob-length_dob
        each_side = lenth_dob_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(90,435," "*left_side+str(DOB_CERT)+" "*right_side)


        c1.drawString(-40,435,"Date of Birth (In Figure) : ____________________________")
        c1.drawString(90,405,date_birth_in_words_value)
        c1.drawString(23,405,"(In Words) : _________________________________________________________________________________ ")

        ADDRESS_1_CERT = data_other_bonafide[0][0]
        total_address1 = 84

        left_side = 42
        right_side = 42

        length_address1 = len(str(ADDRESS_1_CERT))
        lenth_address1_remaining = total_address1-length_address1
        each_side = lenth_address1_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(70,375," "*left_side+str(ADDRESS_1_CERT)+" "*right_side)



        c1.drawString(-40,375,"Residential address : ____________________________________________________________________________________ ")


        ADDRESS_2_CERT = data_other_bonafide[0][1]
        total_address1 = 84

        left_side = 42
        right_side = 42

        length_address1 = len(str(ADDRESS_2_CERT))
        lenth_address1_remaining = total_address1-length_address1
        each_side = lenth_address1_remaining//2

        left_side = each_side
        right_side = each_side

        c1.setFont("VeraIt",10)
        c1.drawString(70,345," "*left_side+str(ADDRESS_2_CERT)+" "*right_side)


        c1.drawString(-40,345,"                                   ____________________________________________________________________________________ ")
        c1.line(-57,320,510,320)
        c1.setLineWidth(2)

        c1.setFont("VeraBd",10)
        c1.drawString(0,303,date_value)
        c1.drawString(-40,303,"Date:")

        c1.drawString(-40,275,"Place: Ahmedabad")
        c1.line(380,283,470,283)
        c1.setLineWidth(2)
        c1.drawString(400,273,"Principal")

        c1.showPage()
        c1.save()








    SAVE_BTN=Button(MAIN_FRAME,text="SAVE",height=3,width=20,bg="lightgrey",activebackground='lightgrey', command = cert,font=('Arial', 10))
    SAVE_BTN.place(x=1100,y=500)









global BACKUP_FUNCTION
def BACKUP_FUNCTION():
    f1 = open(r"BACKUP\academic_detail.csv","w", newline="\n")
    writer1 = csv.writer(f1)
    cur.execute("select * from academic_detail")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f1.close()

    f2 = open(r"BACKUP\exmp_fees.csv","w", newline="\n")
    writer1 = csv.writer(f2)
    cur.execute("select * from exmp_fees")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f2.close()
    
    f3 = open(r"BACKUP\fee_details.csv","w", newline="\n")
    writer1 = csv.writer(f3)
    cur.execute("select * from fee_details")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f3.close()

    f4 = open(r"BACKUP\fee_tran.csv","w", newline="\n")
    writer1 = csv.writer(f4)
    cur.execute("select * from fee_tran")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f4.close()

    f5 = open(r"BACKUP\gr_check.csv","w", newline="\n")
    writer1 = csv.writer(f5)
    cur.execute("select * from gr_check")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f5.close()

    f6 = open(r"BACKUP\gr_details.csv","w", newline="\n")
    writer1 = csv.writer(f6)
    cur.execute("select * from gr_details")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f6.close()

    f7 = open(r"BACKUP\other_detail.csv","w", newline="\n")
    writer1 = csv.writer(f7)
    cur.execute("select * from other_detail")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f7.close()

    f8 = open(r"BACKUP\pending_fee_detail.csv","w", newline="\n")
    writer1 = csv.writer(f8)
    cur.execute("select * from pending_fee_detail")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f8.close()

    f9 = open(r"BACKUP\std_fees.csv","w", newline="\n")
    writer1 = csv.writer(f9)
    cur.execute("select * from std_fees")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f9.close()

    f10 = open(r"BACKUP\tran_details.csv","w", newline="\n")
    writer1 = csv.writer(f10)
    cur.execute("select * from tran_details")
    headings = cur.column_names
    data = cur.fetchall()
    # print(headings)
    # print(data)
    writer1.writerow(headings)
    writer1.writerows(data)
    f10.close()
BACKUP_FUNCTION()









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
GR_BTN.place(x=160,y=0)


image_fees= Image.open(r"ICONS\fees.png")
image_fees= image_fees.resize((55,55))
img_fees= ImageTk.PhotoImage(image_fees)
FEES_BTN=Button(MENU_FRAME,image = img_fees,bg='lightgrey',compound=TOP,text="FEES",command=FEES_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
FEES_BTN.place(x=260,y=0) 


image_fees_edit= Image.open(r"ICONS\edity1.png")
image_fees_edit= image_fees_edit.resize((55,55))
img_fees_edit= ImageTk.PhotoImage(image_fees_edit)
FEES_EDIT_BTN=Button(MENU_FRAME,image = img_fees_edit,bg='lightgrey',compound=TOP,text="FEES EDIT",command=FEES_EDIT_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
FEES_EDIT_BTN.place(x=360,y=0) 



image_fees_report= Image.open(r"ICONS\fee_report.png")
image_fees_report= image_fees_report.resize((55,55))
img_fees_report= ImageTk.PhotoImage(image_fees_report)
FEES_REPORT_BTN=Button(MENU_FRAME,image = img_fees_report,bg='lightgrey',compound=TOP,text="FEES REPORT",command=FEES_REPORT_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
FEES_REPORT_BTN.place(x=450,y=0) 



image_library= Image.open(r"ICONS\Library.png")
image_library= image_library.resize((55,55))
img_library= ImageTk.PhotoImage(image_library)
LIBRARY_BTN=Button(MENU_FRAME,image = img_library,bg='lightgrey',compound=TOP,text="LIBRARY",command=LIBRARY_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
LIBRARY_BTN.place(x=550,y=0)



image_certificate= Image.open(r"ICONS\certificate.png")
image_certificate= image_certificate.resize((55,55))
img_certificate= ImageTk.PhotoImage(image_certificate)
CERTIFICATES_BTN=Button(MENU_FRAME,image = img_certificate,bg='lightgrey',compound=TOP,text="CERTIFICATES",command=CERTIFICATES_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
CERTIFICATES_BTN.place(x=640,y=0)



image_backup= Image.open(r"ICONS\backup.png")
image_backup= image_backup.resize((55,55))
img_backup= ImageTk.PhotoImage(image_backup)
BACKUP_BTN=Button(MENU_FRAME,image = img_backup,bg='lightgrey',compound=TOP,text="BACKUP",command=BACKUP_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
BACKUP_BTN.place(x=740,y=0)



image_aboutus= Image.open(r"ICONS\about us.png")
image_aboutus= image_aboutus.resize((50,55))
img_aboutus= ImageTk.PhotoImage(image_aboutus)
ABOUTUS_BTN=Button(MENU_FRAME,image = img_aboutus,bg='lightgrey',compound=TOP,text="DETAILS",command=ABOUTUS_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
ABOUTUS_BTN.place(x=830,y=0)



image_exit= Image.open(r"ICONS\EXIT_menu.png")
image_exit= image_exit.resize((55,55))
img_exit= ImageTk.PhotoImage(image_exit)
EXIT_BTN=Button(MENU_FRAME,image = img_exit,bg='lightgrey',compound=TOP,text="EXIT",command=EXIT_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
EXIT_BTN.place(x=920,y=0)



image_schl_logo= Image.open(r"ICONS\school_logo.png")
img_schl_logo=image_schl_logo.resize((85,85))
photo_schl_logo= ImageTk.PhotoImage(img_schl_logo)
SCHL_BTN=Button(MENU_FRAME,image = photo_schl_logo,bg='lightgrey',compound=TOP,command=SCHL_FUNCTION,padx=2,pady=2,activebackground='lightgrey',relief=FLAT)
SCHL_BTN.place(x=0,y=0)




DATElbl=Label(MENU_FRAME,text="Date : ",bg='light grey',fg='#151B54',font=("Copperplate Gothic Bold",10))
DATElbl.place(x=1050, y=60)

label_date_now = Label(MENU_FRAME,text="Current Date",bg='light grey',fg='#151B54',font=("Copperplate Gothic Bold",10))
label_date_now.place(x=1110, y=60)

TIMElbl=Label(MENU_FRAME,text="Time : ",bg='light grey',fg='#151B54',font=("Copperplate Gothic Bold",10))
TIMElbl.place(x=1210, y=60)

label_time_now = Label(MENU_FRAME,text="Current Time",bg='lightgrey',fg='#151B54',font=("Copperplate Gothic Bold",10))
label_time_now.place(x=1260, y=60)

def y():
    current_date=datetime.datetime.today().strftime('%d-%m-%y')
    current_time=datetime.datetime.now().strftime('%H:%M:%S %p')
    label_date_now.config(text=current_date)
    label_time_now.config(text=current_time)
    label_time_now.after(100,y)
y()





root.mainloop()


