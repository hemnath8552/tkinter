from tkinter import *
import sqlite3
root=Tk()

#create a database or connect to one
conn=sqlite3.connect('address_book.db')

#creating a cursor
c=conn.cursor()

# creating a table
# c.execute(""" CREATE TABLE addresses(
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer)
#           """)

# create delete function

def save():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = del_box.get()

    c.execute(""" UPDATE addresses SET
        first_name=:first,
        last_name=:last,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode
    
        WHERE oid =:oid""",

              {'first': f_name_edi.get(),
               'last':last_name_edi.get(),
               'address':address_edi.get(),
               'city':city_edi.get(),
               'state':state_edi.get(),
               'zipcode':zip_edi.get(),

               'oid':record_id

               })

    conn.commit()

    conn.close()

    f_name_edi.delete(0, END)
    last_name_edi.delete(0, END)
    address_edi.delete(0, END)
    city_edi.delete(0, END)
    zip_edi.delete(0, END)
    state_edi.delete(0, END)


def update():
    #creating a total new window
    editor = Tk()
    editor.title('Update')

    f_name_lab = Label(editor, text='First name')
    f_name_lab.grid(row=0, column=0, pady=(10, 0))

    l_name_lab = Label(editor, text='Last name')
    l_name_lab.grid(row=1, column=0)

    address_lab = Label(editor, text='Address')
    address_lab.grid(row=2, column=0)

    city_lab = Label(editor, text='City')
    city_lab.grid(row=3, column=0)

    state_lab = Label(editor, text='State')
    state_lab.grid(row=4, column=0)

    zip_lab = Label(editor, text='Zip')
    zip_lab.grid(row=5, column=0)

    global f_name_edi
    global last_name_edi
    global address_edi
    global city_edi
    global state_edi
    global zip_edi

    # Create text boxes
    f_name_edi = Entry(editor, width=30)
    f_name_edi.grid(row=0, column=1, padx=20)

    last_name_edi = Entry(editor, width=30)
    last_name_edi.grid(row=1, column=1, padx=20)

    address_edi = Entry(editor, width=30)
    address_edi.grid(row=2, column=1, padx=20)

    city_edi = Entry(editor, width=30)
    city_edi.grid(row=3, column=1, padx=20)

    state_edi = Entry(editor, width=30)
    state_edi.grid(row=4, column=1, padx=20)

    zip_edi= Entry(editor, width=30)
    zip_edi.grid(row=5, column=1, padx=20)

    save_btn = Button(editor, text='save edited record', command=submit)
    save_btn.grid(row=6, column=1)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id=del_box.get()

    c.execute("SELECT * FROM addresses WHERE oid= "+ record_id)
    records = c.fetchall()
    for record in records:
        f_name_edi.insert(0,record[0])
        last_name_edi.insert(0, record[1])
        state_edi.insert(0, record[2])
        city_edi.insert(0, record[3])
        address_edi.insert(0, record[4])
        zip_edi.insert(0, record[5])

    save_btn = Button(editor, text='save edited record', command=save)
    save_btn.grid(row=6, column=1)

    conn.commit()

    conn.close()

def delete():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    # delete a record
    c.execute("DELETE from addresses WHERE oid="+ del_box.get())

    del_box.delete(0,END)


    conn.commit()

    conn.close()


# create submit function

def submit():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
              }
              )

    conn.commit()

    conn.close()

    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)
    state.delete(0, END)

def query():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM addresses" )
    records=c.fetchall()
    print(records)

    # Loop through the results
    print_records=''
    for record in records:
        print_records+=str(record)+"\n"

    query_label=Label(root,text=print_records)
    query_label.grid(row=15,column=1)

    conn.commit()

    conn.close()

# create text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

zipcode=Entry(root,width=30)
zipcode.grid(row=4,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=5,column=1,padx=20)

del_box=Entry(root,)
del_box.grid(row=9,column=1)

# create textbox label
f_name_label=Label(root,text='First name:')
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text='last name:')
l_name_label.grid(row=1,column=0)

address_label=Label(root,text='Address:')
address_label.grid(row=2,column=0)

city_label=Label(root,text='City:')
city_label.grid(row=3,column=0)

zipcode_label=Label(root,text='Zipcode:')
zipcode_label.grid(row=4,column=0)

state_label=Label(root,text='State')
state_label.grid(row=5,column=0)

del_box_label=Label(root,text='ID no')
del_box_label.grid(row=9,column=0)

# create submit button
submit_button=Button(root,text='Add records',command=submit)
submit_button.grid(row=6,column=1)


# create button to show what is in the database
que_button=Button(root,text='Show records',command=query)
que_button.grid(row=13,column=1)

# to delete required we need the oid number first and then the delete button
#


delete_button=Button(root,text='Delete this record',command=delete)
delete_button.grid(row=11,column=1)


upd_button=Button(root,text="Update record",command=update)
upd_button.grid(row=12,column=1)

# to commit changes
conn.commit()

# close our connection
conn.close()

root.mainloop()