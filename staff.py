from tkinter import *
from Manager import *
from Emp import *

def staff():
    screen1=Tk()
    screen1.title("RESTAURANT PROJECT")
    screen1.overrideredirect(True)
    screen1.geometry("{0}x{1}+0+0".format(screen1.winfo_screenwidth(), screen1.winfo_screenheight()))

    frame1 = Frame(screen1)
    frame1.pack()
    welcome_text = Label(screen1,text="STAFF",fg="white", bg="black",font='Calibri 18 bold ')
    welcome_text.pack()


    Label(screen1,text="Please enter details below").pack()

    Label(screen1,text="ID * ").pack()
    entry1 = Entry(screen1)
    entry1.pack()

    Label(screen1,text="Password * ").pack()
    entry2 = Entry(screen1,show="*")
    entry2.pack()

    statusText = StringVar(screen1)
    message = Label(screen1, textvariable=statusText)
    message.pack()

    def getent():
        from tkinter import messagebox
        b=int(entry1.get())
        c=entry2.get()
        if b==1:
            if c=="123manage":
                Manager()
            else:
                root = Tk()
                root.withdraw()
                messagebox.showerror("Error", "Wrong Password or Id") 
                               
        elif b==2:
            if c=="123emp":
                Emp()
            else:
                root = Tk()
                root.withdraw()
                messagebox.showerror("Error", "Wrong Password or Id") 
               
        else:
            root = Tk()
            root.withdraw()
            messagebox.showerror("Error", "Wrong Password or Id")
          
                              
                    
    Label(screen1,text="").pack()

    button=Button(screen1,text="Click to Continue", command=getent, relief=RAISED)
    button.pack()
    def close_window ():
        screen1.destroy()
        
    Label(screen1,text="").pack()

    button=Button(screen1,text="BACK", command=close_window, relief=RAISED)
    button.pack()





