from tkinter import *

def Emp():
    def view(EMP_ID):
        root1 = Tk()
        root1.title("Staff")
        frame1 = Frame(root1)
        frame1.grid()
        welcome_text = Label(root1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 18 bold ')
        welcome_text.grid(column=18)
        import mysql.connector
        Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
        mycursor=Mydb.cursor()
        mySql_insert_query = """SELECT * FROM MANAGER WHERE EMP_ID=%s"""
        recordTuple = (EMP_ID,)
        mycursor.execute(mySql_insert_query, recordTuple)
        myrecords=mycursor.fetchall()
        for x in myrecords:
            Label(root1,text=x).grid(column=18)
    
    root1 = Tk()
    root1.title("Staff")

    frame1 = Frame(root1)
    frame1.pack()
    welcome_text = Label(root1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 18 bold ')
    welcome_text.pack()
    L1 = Label(root1, text="EMP_ID")
    L1.pack()
    entry1 = Entry(root1, bd =5)
    entry1.insert(END, '0')
    entry1.pack()
          
    statusText = StringVar(root1)
    message = Label(root1, textvariable=statusText)
    message.pack()

            
    def getent():             
        a=int(entry1.get())
        view(a)
              
    button=Button(root1,text="Click to Continue", command=getent)
    button.pack()

    root1.mainloop()


