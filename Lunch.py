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
    recordTuple = (RandomNumber,"L",formatted_date,name,QTY,TOTAL)
    mycursor.execute(mySql_insert_query, recordTuple)
    Mydb.commit()

      
def Lunch():
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
    welcome_text = Label(root1,text="LUNCH",fg="white", bg="black",font='Calibri 18 bold ')
    welcome_text.pack()
    welcome_text.place(x=600,y=10)

    label = Label(root1, text="INDIAN")
    label.pack()
    label.place(x=100,y=100)
            
    label1 = Label(root1, text="Veg")
    label1.pack()
    label1.place(x=10,y=150)
    
    L1 = Label(root1, text="Masala Bhindi")
    L1.pack()
    L1.place(x=10,y=200)
    entry1 = Entry(root1, bd =5)
    entry1.insert(END, '0')
    entry1.pack()
    entry1.place(x=110,y=200)

    L2 = Label(root1, text="Chana Kulcha")
    L2.pack()
    L2.place(x=10,y=250)
    entry2 = Entry(root1, bd =5)
    entry2.insert(END, '0')
    entry2.pack()
    entry2.place(x=110,y=250)
            
    label2 = Label(root1, text="Non Veg")
    label2.pack()
    label2.place(x=10,y=300)
      
    L3= Label(root1, text="Shahi Egg Curry")
    L3.pack()
    L3.place(x=10,y=350)
    entry3 = Entry(root1, bd =5)
    entry3.insert(END, '0')
    entry3.pack()
    entry3.place(x=110,y=350)

    L4 = Label(root1, text="Low Fat Dahi \n Chicken")
    L4.place(x=10,y=400)
    entry4 = Entry(root1, bd =5)
    entry4.insert(END, '0')
    entry4.pack()
    entry4.place(x=110,y=400)
      
    label3 = Label(root1, text="CONTINENTAL")
    label3.pack()
    label3.place(x=550,y=100)

    label4 = Label(root1, text="Veg")
    label4.pack()
    label4.place(x=500,y=150)

    L5 = Label(root1, text="Rolls")
    L5.pack()
    L5.place(x=500,y=200)
    entry5 = Entry(root1, bd =5)
    entry5.insert(END, '0')
    entry5.pack()
    entry5.place(x=600,y=200)
       
    L6 = Label(root1, text="Oatmeal")
    L6.pack()
    L6.place(x=500,y=250)
    entry6 = Entry(root1, bd =5)
    entry6.insert(END, '0')
    entry6.pack()
    entry6.place(x=600,y=250)
           
    label5 = Label(root1, text="Non Veg")
    label5.pack()
    label5.place(x=500,y=300)

    L7 = Label(root1, text="Fried Eggs")
    L7.pack()
    L7.place(x=500,y=350)
    entry7 = Entry(root1, bd =5)
    entry7.insert(END, '0')
    entry7.pack()
    entry7.place(x=600,y=350)

    L8 = Label(root1, text="Boiled Eggs")
    L8.pack()
    L8.place(x=500,y=400)
    entry8 = Entry(root1, bd =5)
    entry8.insert(END, '0')
    entry8.pack()
    entry8.place(x=600,y=400)
      
    label6 = Label(root1, text="CHINIESE")
    label6.pack()
    label6.place(x=1050,y=100)
    label7 = Label(root1, text="Veg")
    label7.pack()
    label7.place(x=1000,y=150)

    L9 = Label(root1, text="Pepper Steak w. \n onion")
    L9.pack()
    L9.place(x=1000,y=200)
    entry9 = Entry(root1, bd =5)
    entry9.insert(END, '0')
    entry9.pack()
    entry9.place(x=1100,y=200)
    
    L10 = Label(root1, text="Broccoli w. garlic \n sauce")
    L10.pack()
    L10.place(x=1000,y=250)
    entry10 = Entry(root1, bd =5)
    entry10.insert(END, '0')
    entry10.pack()
    entry10.place(x=1100,y=250)
                 
    label8 = Label(root1, text="Non Veg")
    label8.pack()
    label8.place(x=1000,y=300)
            
    L11 = Label(root1, text="Chow Mein \n Chicken")
    L11.pack()
    L11.place(x=1000,y=350)
    entry11 = Entry(root1, bd =5)
    entry11.insert(END, '0')
    entry11.pack()
    entry11.place(x=1100,y=350)
    
    L12= Label(root1, text="Sesame Chicken")
    L12.pack()
    L12.place(x=1000,y=400)
    entry12 = Entry(root1, bd =5)
    entry12.insert(END, '0')
    entry12.pack()
    entry12.place(x=1100,y=400)

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
        g=int(entry7.get())
        h=int(entry8.get())
        i=int(entry9.get())
        j=int(entry10.get())
        k=int(entry11.get())
        l=int(entry12.get())

        root2 = Tk()
        root2.title("Order")
        root2.geometry("1800x1050")

        frame1 = Frame(root2)
        frame1.grid()
        welcome_text = Label(root2,text="BILL",fg="white", bg="black",font='Calibri 18 bold ')
        welcome_text.grid(column=1,ipadx=700)
                  
        Label(root2,text=" ").grid(column=1)
        Label(root2,text=" ").grid(column=1)
        global RandomNumber
        y="Order Id:"
        z="  "
        x=RandomNumber
        Label(root2,text=(y+z+str(x))).grid(column=1)
        Label(root2,text=" ").grid(column=1)
        Label(root2,text=" ").grid(column=1)
        Label(root2,text=" ").grid(column=1)

        if a== 0:
            pass
        elif a!= "csv":
            Insert_item("Masala Bhindi",a,a*82)
            food.append(a*82)
            z="                      "
            x=a*82
            y="Masala Bhindi"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
            
        if b== 0:
            pass
        elif b!= "csv":           
            Insert_item("Chana Kulcha",b,b*160)
            food.append(b*160)
            z="                     "
            x=b*160
            y="Chana Kulcha"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
                        
        if c== 0:
            pass
        elif c!= "csv":
            Insert_item("Shahi Egg Curry",c,c*175)
            food.append(c*175)
            z="                 "
            x=c*175
            y="Shahi Egg Curry"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
                                   
        if d== 0:
            pass
        elif d!= "csv":
            Insert_item("Low Fat Dahi Chicken",d,d*162)
            food.append(d*162)
            z="        "
            x=d*162
            y="Low Fat Dahi Chicken"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
                       
        if e== 0:
            pass
        elif e!= "csv":
            Insert_item("Rolls",e,e*50)
            food.append(e*50)
            z="                                     "
            x=e*50
            y="Rolls"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
               
        if f== 0:
            pass
        elif f!= "csv":
            Insert_item("Oatmeal",f,f*64)
            food.append(f*64)
            z="                               "
            x=f*64
            y="Oatmeal"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)

        if g== 0:
            pass
        elif g!= "csv":
            Insert_item("Fried Eggs",g,g*78)
            food.append(g*78)
            z="                            "
            x=g*78
            y="Fried Eggs"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)

        if h== 0:
            pass
        elif h!= "csv":
            Insert_item("Boiled Eggs",h,h*82)
            food.append(h*82)
            z="                          "
            x=h*82
            y="Boiled Eggs"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
        if i==0:
            pass
        elif i!= "csv":
            Insert_item("Pepper Steak w. onion",i,i*56)
            food.append(i*56)
            z="        "
            x=i*56
            y="Pepper Steak w. onion"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
                         
        if j== 0:
            pass
        elif j!= "csv":
            Insert_item("Broccoli w. garlic sauce",j,j*58)
            food.append(j*58)
            z="       "
            x=j*58
            y="Broccoli w. garlic sauce"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
                        
        if k== 0:
            pass
        elif k!= "csv":
            Insert_item("Chow Mein Chicken",k,k*94)
            food.append(k*94)
            z="            "
            x=k*94
            y="Chow Mein Chicken"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)
                        
        if l== 0:
            pass
        elif l!= "csv":
            Insert_item("Sesame Chicken",l,l*176)
            food.append(l*176)
            z="                 "
            x=l*176
            y="Sesame Chicken"
            w="Rs"
            v=" "
            Label(root2,text=(y+z+str(x)+v+w)).grid(column=1)

        t="                            "
        u=sum(food)*5/100
        v="TAX GST"
        l="Rs"
        o=" "
        Label(root2,text=(v+t+str(u)+o+l)).grid(column=1)
        q=sum(food)+u
        r="Total cost"
        m="                           "
        j="____________________________________"
        Label(root2,text=(j)).grid(column=1)
        Label(root2,text=(r+m+str(q)+o+l)).grid(column=1)

        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)
        Label(root2,text=" ").grid(column=16)

        Button(root2, text="Payment", command= restart_program).grid(column=1)

        mainloop()

    button=Button(root1,text="Back", command=close_window)
    button.pack()
    button.place(x=580,y=550)
         
    button=Button(root1,text="Continue", command=Continue)
    button.pack()
    button.place(x=570,y=500)

    mainloop()

