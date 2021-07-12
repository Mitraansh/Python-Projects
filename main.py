from tkinter import *
from staff import *
from Restaurant import *
import time
from pygame import mixer
now = time.strftime("%H:%M:%S")
from tkinter import messagebox
try:
    screen1=Tk()
    screen1.title("RESTAURANT PROJECT")
    screen1.overrideredirect(True)
    screen1.geometry("{0}x{1}+0+0".format(screen1.winfo_screenwidth(), screen1.winfo_screenheight()))

    Label(screen1,text="").pack()
    welcome_text= Label(screen1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 24 bold ')
    welcome_text.pack()

    label = Label(text="",bg="black",fg="white",font='times 22 bold ')

    mixer.init()
    def play_music():
        mixer.music.load("song1.mp3")
        mixer.music.play()

    play_music()
    def clock():
        global label
        label.pack()
        label.place(x=1100,y=10)
        update_clock()

    def update_clock():
        global label,now
        now = time.strftime("%H:%M:%S")
        label.configure(text=now)
        screen1.after(1000,update_clock)

    clock()
         
    password=StringVar()
    ID=StringVar()

    Label(screen1,text="Please enter details below").pack()

    Label(screen1,text="ID * ").pack()
    Entry(screen1,textvariable=ID,relief=SUNKEN).pack()

    Label(screen1,text="Password * ").pack()
    Entry(screen1,textvariable=password,show="*",relief=SUNKEN).pack()

    def getent():
        b=int(ID.get())
        c=password.get()
        if b==1:
            if c=="123manage":
                staff()
            else:
                root = Tk()
                root.withdraw()
                messagebox.showerror("Error", "Wrong Password or Id")                 
        elif b==2:
            if c=="123":
                Restaurant()
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

    button=Button(screen1,text="EXIT", command=close_window, relief=RAISED)
    button.pack()

except:
    pass



