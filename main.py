import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
# import openpyxl

window=tkinter.Tk()
window.title('data entry form')

def enter_data():
    accepted=accept_var.get()

    if accepted=="Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        registration_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemestes = semesters_spinbox.get()

        print("First name: ", first_name, "last name: ", last_name)
        print("Title: ", title, "Age:", age, "Nationality: ", nationality)
        print("registration_status: ", registration_status, "numcourses: ", numcourses, "num_semester: ", numsemestes)
        print("------------------------------------------------------------")

    else:
        tkinter.messagebox.showwarning(title="", message="")


    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    title=title_combobox.get()
    age=age_spinbox.get()
    nationality=nationality_combobox.get()
    registration_status = reg_status_var.get()
    numcourses = numcourses_spinbox.get()
    numsemestes = semesters_spinbox.get()


    print("First name:", first_name, "last name", last_name)
    print("Title:", title,"Age:", age, "Nationality:", nationality, )
    print("registration_status", registration_status,"numcourses",numcourses, "num_semester",numsemestes)

frame=tkinter.Frame(window)
frame.pack()

#saving userinfo

user_info_frame=tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20, pady=20)

first_name_label=tkinter.Label(user_info_frame,text="first name")
first_name_label.grid(row=0,column=0)

last_name_label=tkinter.Label(user_info_frame, text="last name")
last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label=tkinter.Label(user_info_frame, text='title')
title_combobox=ttk.Combobox(user_info_frame, values=["","mr.","ms.","dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="age")
age_spinbox=tkinter.Spinbox(user_info_frame, from_=18,to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label=tkinter.Label(user_info_frame,text="nationality")
nationality_combobox=ttk.Combobox(user_info_frame, values=["Africa", "Antartica","india"] )

nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving course info
courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

registered_label=tkinter.Label(courses_frame,text="regisration status")

reg_status_var=tkinter.StringVar(value="Not registered")
registered_check=tkinter.Checkbutton(courses_frame, text="Currently registered", variable=reg_status_var, onvalue="Registered",offvalue="Not registered")

registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label=tkinter.Label(courses_frame,text="# completed courses")
numcourses_spinbox=tkinter.Spinbox(courses_frame,from_=0, to="infinity")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

semesters_label=tkinter.Label(courses_frame,text="# Semesters")
semesters_spinbox=tkinter.Spinbox(courses_frame,from_=0, to="infinity")
semesters_label.grid(row=0,column=2)
semesters_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#accept terms
terms_frame=tkinter.LabelFrame(frame,text="terms & conditions")
terms_frame.grid(row=2,column=0, sticky="news",padx=20,pady=20)

accept_var=tkinter.StringVar(value="Not accepted")
terms_check=tkinter.Checkbutton(terms_frame, text="i love you", variable=accept_var,onvalue="Accepted", offvalue="not accepted")
terms_check.grid(row=0,column=0)

button =tkinter.Button(frame,text="Enter data", command=enter_data)
button.grid(row=3,column=0, padx=20,pady=20)

window.mainloop()