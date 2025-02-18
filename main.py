import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root", password="sql@#123", database="python_db")


def insert(name,age,city):
    res= con.cursor()
    sql= "insert into users (name,age,city) values (%s,%s,%s)"
    user =(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data inserted Successfully")

def update(name,age,city,id):
    res = con.cursor()
    sql = "update users set name=%s, age=%s, city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()
    print("Data updated Successfully")

def select():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))
    # res=con.cursor()


def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data deleted Successfully")


while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Show Data")
    print("4. Delete Data")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter Name:")
        age=input("Enter Age:")
        city=input("Enter City:")
        insert(name,age,city)
    elif choice==2:
        id=input("Enter the id:")
        name=input("Enter Name:")
        age=input("Enter Age:")
        city=input("Enter City:")
        update(name,age,city,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("Enter the ID to delete:")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("Invalid Selection please try again")