from tkinter import *
def view():
    root1 = Tk()
    root1.title("Order")

    frame1 = Frame(root1)
    frame1.grid()
    welcome_text = Label(root1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 18 bold ')
    welcome_text.grid(column=18)
    ID=StringVar()

    Label(root1,text="Order Id :").grid(column=18)
    Entry(root1,textvariable=ID).grid(column=18)

    def getent():
        b=int(ID.get())
        import mysql.connector
        Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
        mycursor=Mydb.cursor()
        mySql_insert_query ="""select ORDER_ID,ORDER_TYPE,ORDER_DATE,ITEM_NAME,QTY,TOTAL\
                              from INCOME where ORDER_ID=%s"""
        recordtuple=[b]
        mycursor.execute(mySql_insert_query,recordtuple)
        for ORDER_ID,ORDER_TYPE,ORDER_DATE,ITEM_NAME,QTY,TOTAL in mycursor:
            a="ORDER_ID:"
            b=ORDER_ID
            c=" "
            Label(root1,text=(a+c+str(b))).grid(column=18)
            d="ORDER_TYPE:"
            e=ORDER_TYPE
            Label(root1,text=(d+c+str(e))).grid(column=18)
            f="ORDER_DATE:"
            g=ORDER_DATE
            Label(root1,text=(f+c+str(g))).grid(column=18)
            h="ITEM_NAME:"
            i=ITEM_NAME
            Label(root1,text=(h+c+str(i))).grid(column=18)
            j="QTY:"
            k=QTY
            Label(root1,text=(j+c+str(k))).grid(column=18)
            l="TOTAL:"
            m=TOTAL
            Label(root1,text=(l+c+str(m))).grid(column=18)
                        
    button=Button(root1,text="Click to Continue", command=getent)
    button.grid(column=18)

