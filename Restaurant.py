from tkinter import *
from menu import*
from Order import *
from About import *
from View import *


def Restaurant():
    def close_window ():
        screen.destroy()

    screen=Tk()
    screen.title("RESTAURANT PROJECT")
    screen.overrideredirect(True)
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))

    C = Canvas(screen, bg="blue", height=1100, width=1800)
    filename = PhotoImage(master=C,file = "photo4r.png")
    background_label = Label(screen, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    canvas = Canvas(screen, bg = "#000000")
    photo=PhotoImage(master=canvas,file="th.png")
    photo1=PhotoImage(master=canvas,file="rsz_9photo1.png")
    photo2=PhotoImage(master=canvas,file="rsz_1photo3.png")
    label=Label(screen,image=photo)
    label.pack()
    label.place(x=460,y=460)
    label1=Label(screen,image=photo1)
    label1.pack()
    label1.place(x=0,y=460)
    label2=Label(screen,image=photo2)
    label2.pack()
    label2.place(x=930,y=460)

    welcome_text = Button(screen,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 24 bold ',state=DISABLED)
    welcome_text.pack()
    welcome_text.place(x=550,y=10)

    button3=Button(screen,text=" MENU",fg="white", bg="black",font='Calibri 20',relief='raised',activebackground='blue',command=menu)
    button3.pack()
    button3.place(x=600,y=170)
    button4=Button(screen,text="ORDER",fg="white", bg="black",font='Calibri 20',relief='raised',activebackground='blue',command=order)
    button4.pack()
    button4.place(x=600,y=240)
    button4=Button(screen,text="ABOUT",fg="white", bg="black",font='Calibri 20',relief='raised',activebackground='blue',command=about)
    button4.pack()
    button4.place(x=600,y=100)

    button5=Button(screen,text="  VIEW  ",fg="white", bg="black",font='Calibri 20',relief='raised',activebackground='blue',command=view)
    button5.pack()
    button5.place(x=600,y=310)
    
    button6=Button(screen,text="    EXIT    ",fg="white", bg="black",font='Calibri 18',relief='raised',activebackground='blue',command=close_window)
    button6.pack()
    button6.place(x=600,y=380)

    mainloop()


