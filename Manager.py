from tkinter import *
def Manager():
    def view():
        root1 = Tk()
        root1.title("Staff")
        frame1 = Frame(root1)
        frame1.grid()
        welcome_text = Label(root1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 18 bold ')
        welcome_text.grid(column=18)
        import mysql.connector
        Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
        mycursor=Mydb.cursor()
        mycursor.execute("SELECT * FROM MANAGER" )
        myrecords=mycursor.fetchall()
        for x in myrecords:
            Label(root1,text=x).grid(column=18)
    
    def view_income():
        root1 = Tk()
        root1.title("Staff")
        frame1 = Frame(root1)
        frame1.grid()
        welcome_text = Label(root1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 18 bold ')
        welcome_text.grid(column=18)
        import mysql.connector
        Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
        mycursor=Mydb.cursor()
        mycursor.execute("SELECT * FROM INCOME" )
        myrecords=mycursor.fetchall()
        for x in myrecords:
            Label(root1,text=x).grid(column=18)

    def insert():
        def function(EMP_ID,EMP_NAME,DESIGNATION,PHONE_NO,SALARY):
            import mysql.connector
            Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
            mycursor=Mydb.cursor()
            mySql_insert_query = """INSERT INTO MANAGER(EMP_ID,EMP_NAME,DESIGNATION,PHONE_NO,SALARY) 
                                          VALUES (%s, %s, %s,%s, %s) """
            recordTuple = (EMP_ID,EMP_NAME,DESIGNATION,PHONE_NO,SALARY)
            mycursor.execute(mySql_insert_query, recordTuple)
            Mydb.commit()
        root1 = Tk()
        root1.title("Staff")

        frame1 = Frame(root1)
        frame1.pack()
        Label(root1,text="").pack()
        welcome_text = Label(root1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 18 bold ')
        welcome_text.pack()
        
        L1 = Label(root1, text="EMP_ID")
        L1.pack()
        entry1 = Entry(root1, bd =5)
        entry1.insert(END, '0')
        entry1.pack()
        
        L2 = Label(root1, text="EMP_Name")
        L2.pack()
        entry2= Entry(root1, bd =5)
        entry2.insert(END, 'DEFAULT  TEXT')
        entry2.pack()
        
        L3 = Label(root1, text="DESIGNATION")
        L3.pack()
        entry3= Entry(root1, bd =5)
        entry3.insert(END, 'DEFAULT TEXT')
        entry3.pack()
        
        L4 = Label(root1, text="PHONE_NO")
        L4.pack()
        entry4 = Entry(root1, bd =5)
        entry4.insert(END, '0')
        entry4.pack()
        
        L5 = Label(root1, text="SALARY")
        L5.pack()
        entry5 = Entry(root1, bd =5)
        entry5.insert(END, '0')
        entry5.pack()

        statusText = StringVar(root1)
        message = Label(root1, textvariable=statusText)
        message.pack()
     
        def getent():
            Label(root1,text="RECORD INSERTED SUCESSFULLY....").pack()              
            a=int(entry1.get())
            b=entry2.get()
            c=entry3.get()
            d=int(entry4.get())
            e=int(entry5.get())
            function(a,b,c,d,e)

        button=Button(root1,text="INSERT", command=getent)
        button.pack()
          
    def update_salary():
        def function(SALARY,EMP_ID):
            import mysql.connector
            Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
            mycursor=Mydb.cursor()
            mySql_insert_query = """UPDATE MANAGER SET SALARY=%s WHERE EMP_ID=%s"""
            recordTuple = (SALARY,EMP_ID,)
            mycursor.execute(mySql_insert_query, recordTuple)
            Mydb.commit()
            
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
        L2 = Label(root1, text="Salary")
        L2.pack()
        entry2= Entry(root1, bd =5)
        entry2.insert(END, '0')
        entry2.pack()
          
        statusText = StringVar(root1)
        message = Label(root1, textvariable=statusText)
        message.pack()
  
        def getent():
            Label(root1,text="UPDATE SUCESSFULL....").pack()              
            a=int(entry1.get())
            b=int(entry2.get())
            function(b,a)
              
        button=Button(root1,text="UPDATE", command=getent)
        button.pack()

    def update_phone():
        def function(PHONE_NO,EMP_ID):
            import mysql.connector
            Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
            mycursor=Mydb.cursor()
            mySql_insert_query = """UPDATE MANAGER SET PHONE_NO=%s WHERE EMP_ID=%s"""
            recordTuple = (PHONE_NO,EMP_ID,)
            mycursor.execute(mySql_insert_query, recordTuple)
            Mydb.commit()
            
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
        L2 = Label(root1, text="PHONE_NO")
        L2.pack()
        entry2= Entry(root1, bd =5)
        entry2.insert(END, '0')
        entry2.pack()
          
        statusText = StringVar(root1)
        message = Label(root1, textvariable=statusText)
        message.pack()

            
        def getent():
            Label(root1,text="UPDATE SUCESSFULL....").pack()              
            a=int(entry1.get())
            b=int(entry2.get())
            function(b,a)
              
        button=Button(root1,text="UPDATE", command=getent)
        button.pack()
     
    def update_designation():
        def function(DESIGNATION,EMP_ID):
            import mysql.connector
            Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
            mycursor=Mydb.cursor()
            mySql_insert_query = """UPDATE MANAGER SET DESIGNATION=%s WHERE EMP_ID=%s"""
            recordTuple = (DESIGNATION,EMP_ID,)
            mycursor.execute(mySql_insert_query, recordTuple)
            Mydb.commit()
            
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
        L2 = Label(root1, text="DESIGNATION")
        L2.pack()
        entry2= Entry(root1, bd =5)
        entry2.insert(END, '0')
        entry2.pack()
          
        statusText = StringVar(root1)
        message = Label(root1, textvariable=statusText)
        message.pack()
    
        def getent():
            Label(root1,text="UPDATE SUCESSFULL....").pack()              
            a=int(entry1.get())
            b=entry2.get()
            function(b,a)
              
        button=Button(root1,text="UPDATE", command=getent)
        button.pack()
     
     
    def delete():
        def function(EMP_ID):
            import mysql.connector
            Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
            mycursor=Mydb.cursor()
            mySql_insert_query = """DELETE FROM MANAGER WHERE EMP_ID=%s"""
            recordTuple = (EMP_ID,)
            mycursor.execute(mySql_insert_query, recordTuple)
            Mydb.commit()
            
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
            Label(root1,text="DELETE SUCESSFULL....").pack()              
            a=int(entry1.get())
            function(a)
              
        button=Button(root1,text="DELETE", command=getent)
        button.pack()

    root = Tk()
    root.title("MANAGER")
    menubar = Menu(root)
    welcome_text= Label(root,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 24 bold ')
    welcome_text.pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="INSERT", command=insert)

    menubar.add_cascade(label="INSERT", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    
    editmenu.add_command(label="EXPENDITURE", command=view)

    editmenu.add_command(label="INCOME", command=view_income)
     
    menubar.add_cascade(label="VIEW", menu=editmenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="SALARY", command=update_salary)
    helpmenu.add_command(label="PHONE_NO", command=update_phone)
    helpmenu.add_command(label="DESIGNATION", command=update_designation)

    menubar.add_cascade(label="UPDATE", menu=helpmenu)

    menu = Menu(menubar, tearoff=0)
    menu.add_command(label="DELETE", command=delete)

    menubar.add_cascade(label="DELETE", menu=menu)

    root.config(menu=menubar)
    root.mainloop()
    