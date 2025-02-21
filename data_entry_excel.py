import tkinter
from tkinter import *
from tkinter import ttk
import openpyxl
import os
from tkinter import messagebox
import sqlite3

window = tkinter.Tk()
window.title('Data entry form')

frame = Frame(window)# this frame comes within the window man
frame.pack()

# save
def save():

    accept = acc_status_var.get()
    if accept == 'ticked':

            first_name=first_name_entry.get()
            last_name=last_name_entry.get()
            age=age_entry.get()
            nationality=nationality_entry.get()
            registration=reg_status_var.get()
            comp=comp_entry.get()
            sem=sem_entry.get()


            if first_name:
                title = title_entry.get()
                reg_status=reg_status_var.get()

                conn=sqlite3.connect('data.db')
                c=conn.cursor()
                c.execute(""" CREATE TABLE IF NOT EXISTS Stud_data(
                            firstname text,
                            lastname text,
                            title text,
                            age int,
                            nationality text,
                            registration_status text,
                            num_courses int,
                            num_sem int)
                            
                            """)

                data_insert_query=''' INSERT INTO Stud_data(firstname,lastname,title,age,nationality,registration_status,
                                        num_courses,num_sem) Values(?,?,?,?,?,?,?,?)'''
                data_insert_tuple=(first_name,last_name,title,age,nationality,registration,comp,sem)

                c.execute(data_insert_query,data_insert_tuple)
                conn.commit()


                conn.close()

                print('your data is successfully uploaded into database')

                first_name_entry.delete(0,END)
                last_name_entry.delete(0,END)
                title_entry.delete(0,END)
                age_entry.delete(0,END)
                nationality_entry.delete(0,END)
                comp_entry.delete(0,END)
                sem_entry.delete(0,END)


                # to save values in excel
                filepath="C:/Users/Hebstin/PycharmProjects/tkinter/data_entry/love.xlsx"
                # filepath="C:\Users\Hebstin\PycharmProjects\tkinter\data_entry\love.xlsx"

                if not os.path.exists(filepath):
                    workbook=openpyxl.Workbook()
                    sheet=workbook.active
                    heading=['Firstname','lastname','title','age','Nationality','completed','sem']
                    sheet.append(heading)
                    workbook.save(filepath)

                workbook=openpyxl.load_workbook(filepath)
                sheet=workbook.active
                sheet.append([first_name,last_name,age,nationality,registration,comp,sem])
                workbook.save(filepath)



            else:
                messagebox.showwarning(title='Error', message='First name is required')

    else:
        messagebox.showwarning(title='Error',message='You have not accepted the terms')

# creating frame 1

user_info_frame1=LabelFrame(frame,text='user info')
user_info_frame1.grid(row=0,column=0)

# firstname (frame 1)

first_name_label=Label(user_info_frame1,text='firstname')
first_name_label.grid(row=0,column=0)

first_name_entry=Entry(user_info_frame1,)
first_name_entry.grid(row=1,column=0)

# last name(frame 1 )

last_name_label=Label(user_info_frame1,text='last name')
last_name_label.grid(row=0,column=1)



last_name_entry=Entry(user_info_frame1,)
last_name_entry.grid(row=1,column=1)

# title (frame 1 )

title_name_label=Label(user_info_frame1,text='title')
title_name_label.grid(row=0,column=2)

# for combo box you need to import ttk
title_entry=ttk.Combobox(user_info_frame1,values=['mis','misses'])
title_entry.grid(row=1,column=2)

# age(frame 1)

age_name_label=Label(user_info_frame1,text='Age')
age_name_label.grid(row=2,column=0)

age_entry=Spinbox(user_info_frame1,from_=18,to=100)
age_entry.grid(row=3,column=0)

# Nationality (frame 1)

nationality_name_label=Label(user_info_frame1,text='Nationality')
nationality_name_label.grid(row=2,column=1)

nationality_entry=ttk.Combobox(user_info_frame1,values=['india','american'])
nationality_entry.grid(row=3,column=1)


# setting size for frame 1 using for loop, we are getting all the children widget

for widget in user_info_frame1.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# creating frame 2

user_info_frame2=LabelFrame(frame,text='user info 2')
user_info_frame2.grid(row=1,column=0,sticky='news')

# registration (frame 2)

registration_name_label=Label(user_info_frame2,text='Registration status')
registration_name_label.grid(row=0,column=0)

# this checkbox comes with a varibale
reg_status_var=StringVar(value='Not registered')
registration_entry=Checkbutton(user_info_frame2,text='currently registered',
                               variable=reg_status_var,onvalue='Registered',
                               offvalue='Not registered')
registration_entry.grid(row=1,column=0)



# completed course(frame 2)

com_course_label=Label(user_info_frame2,text='Completed courses')
com_course_label.grid(row=0,column=1)

comp_entry=Spinbox(user_info_frame2,from_=0,to=100)
comp_entry.grid(row=1,column=1)

# semesters( frame 2)

sem_label=Label(user_info_frame2,text='Semester')
sem_label.grid(row=0,column=2)

sem_entry=Spinbox(user_info_frame2,from_=0,to=8)
sem_entry.grid(row=1,column=2)

# sizing the frame 2

for widget in user_info_frame2.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# creating frame 3

user_info_frame3=LabelFrame(frame,text='Terms and condition')
user_info_frame3.grid(row=2,column=0,sticky='news',padx=20,pady=20)

acc_status_var=StringVar(value='not ticked')
i_accept_entry=Checkbutton(user_info_frame3,text='I accept to the terms and conditions',variable=acc_status_var,onvalue='ticked',
                               offvalue='not ticked')
i_accept_entry.grid(row=0,column=0)


# Save button

save_button=Button(frame,text='Save data',command=save)
save_button.grid(row=3,column=0,sticky='news',pady=10,padx=20)

window.mainloop()