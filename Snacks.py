from tkinter import *
import random
from datetime import datetime
import sys
import os
from tkinter import messagebox

Nums = range(1, 99999)
RandomNumber = random.choice(Nums)

now =datetime.utcnow()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

def Insert_item(name,QTY,TOTAL):
    import mysql.connector
    Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
    mycursor=Mydb.cursor()
    mySql_insert_query = """INSERT INTO INCOME(ORDER_ID, ORDER_TYPE,ORDER_DATE,ITEM_NAME,QTY,TOTAL) 
                                VALUES (%s, %s, %s,%s, %s, %s) """
    global RandomNumber,formatted_date
    recordTuple = (RandomNumber,"SN",formatted_date,name,QTY,TOTAL)
    mycursor.execute(mySql_insert_query, recordTuple)
    Mydb.commit()

      
def Snacks():
    def Continue():
        MsgBox =messagebox.askquestion ('Payment','Are you sure',icon = 'warning')
        if MsgBox == 'yes':
            getent()
        else:
            pass
    def close_window ():
        root1.destroy()
    root1 = Tk()
    root1.title("Order")
    root1.overrideredirect(True)
    root1.geometry("{0}x{1}+0+0".format(root1.winfo_screenwidth(), root1.winfo_screenheight()))

    frame1 = Frame(root1)
    frame1.pack()
    welcome_text = Label(root1,text="SNACKS",fg="white", bg="black",font='Calibri 18 bold ')
    welcome_text.pack()
    welcome_text.place(x=580,y=10)
    
    L1 = Label(root1, text="Brownie Brittle")
    L1.pack()
    L1.place(x=10,y=200)
    entry1 = Entry(root1, bd =5)
    entry1.insert(END, '0')
    entry1.pack()
    entry1.place(x=130,y=200)

    L2 = Label(root1, text="Deep Dark Sea Salt \n Truffles")
    L2.pack()
    L2.place(x=10,y=400)
    entry2 = Entry(root1, bd =5)
    entry2.insert(END, '0')
    entry2.pack()
    entry2.place(x=130,y=400)
      
    L3= Label(root1, text="Chocolate Hazelnut \n & Almond Butter \n Squeeze")
    L3.pack()
    L3.place(x=500,y=200)
    entry3 = Entry(root1, bd =5)
    entry3.insert(END, '0')
    entry3.pack()
    entry3.place(x=620,y=200)

    L4 = Label(root1, text="Snacks Mango Tango \n Almond Mix")
    L4.pack()
    L4.place(x=500,y=400)
    entry4 = Entry(root1, bd =5)
    entry4.insert(END, '0')
    entry4.pack()
    entry4.place(x=620,y=400)

    L5 = Label(root1, text="Honey Graham Sticks")
    L5.pack()
    L5.place(x=1000,y=200)
    entry5 = Entry(root1, bd =5)
    entry5.insert(END, '0')
    entry5.pack()
    entry5.place(x=1120,y=200)
       
    L6 = Label(root1, text="Tropical Fruit Snacks")
    L6.pack()
    L6.place(x=1000,y=400)
    entry6 = Entry(root1, bd =5)
    entry6.insert(END, '0')
    entry6.pack()
    entry6.place(x=1120,y=400)
           
    statusText = StringVar(root1)
    message = Label(root1, textvariable=statusText)
    message.pack()

    def getent():
        def restart_program():
            python = sys.executable
            os.execl(python, python, * sys.argv)
                        
        food=list()
        a=int(entry1.get())
        b=int(entry2.get())
        c=int(entry3.get())
        d=int(entry4.get())
        e=int(entry5.get())
        f=int(entry6.get())

        root2 = Tk()
        root2.title("Order")
        root2.geometry("1800x1050")

        frame1 = Frame(root2)
        frame1.grid()
        welcome_text = Label(root2,text="BILL",fg="white", bg="black",font='Calibri 18 bold ')
        welcome_text.grid(column=16,ipadx=700)
                  
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        global RandomNumber
        y="Order Id:"
        z="  "
        x=RandomNumber
        Label(root2,text=(y+z+str(x))).grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)

        if a== 0:
            pass
        elif a!= "csv":
            Insert_item("Brownie Brittle",a,a*48)
            food.append(a*48)
            z="                                                                "
            x=a*48
            y="Brownie Brittle"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=16)
            
        if b== 0:
            pass
        elif b!= "csv":           
            Insert_item("Deep Dark Sea Salt Truffles",b,b*76)
            food.append(b*76)
            z="                                            "
            x=b*76
            y="Deep Dark Sea Salt Truffles"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=16)
                        
        if c== 0:
            pass
        elif c!= "csv":
            Insert_item("Choco Haze & Almond Squeeze",c,c*44)
            food.append(c*44)
            z="            "
            x=c*44
            y="Chocolate Hazelnut & Almond Butter Squeeze"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=16)
                                   
        if d== 0:
            pass
        elif d!= "csv":
            Insert_item("Snacks Mango Tango Almond Mix",d,d*48)
            food.append(d*48)
            z="                                "
            x=d*48
            y="Snacks Mango Tango Almond Mix"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=16)
                       
        if e== 0:
            pass
        elif e!= "csv":
            Insert_item("Honey Graham Sticks",e,e*82)
            food.append(e*82)
            z="                                                     "
            x=e*82
            y="Honey Graham Sticks"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=16)
               
        if f== 0:
            pass
        elif f!= "csv":
            Insert_item("Tropical Fruit Snacks",f,f*73)
            food.append(f*73)
            z="                                                      "
            x=f*73
            y="Tropical Fruit Snacks"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=16)
            
            
        t="                                                                     "
        u=sum(food)*5/100
        v="TAX GST"
        l="Rs"
        o=" "
        Label(root2,text=(v+t+str(u)+o+l)).grid(column=16)
        q=sum(food)+u
        r="Total cost"
        m="                                                                  "
        j="_________________________________________________________________"
        Label(root2,text=(j)).grid(column=16)
        Label(root2,text=(r+m+str(q)+o+l)).grid(column=16)

        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)

        Button(root2, text="Payment", command= restart_program).grid(column=16)

        mainloop()

    button=Button(root1,text="Back", command=close_window)
    button.pack()
    button.place(x=580,y=550)
         
    button=Button(root1,text="Continue", command=Continue)
    button.pack()
    button.place(x=570,y=500)

    mainloop()

