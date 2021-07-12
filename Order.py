from tkinter import *
from Desserts import*
from Breakfast import *
from Snacks import*
from Beverages import *
from Breads import*
from Dinner import *
from Lunch import *

def order():
    def close_window ():
        root.destroy()
    root = Tk()
    root.title("Order")
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    frame = Frame(root)
    frame.pack()
    welcome_text = Label(root,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 24 bold ')
    welcome_text.pack()
    
    first_button=Button(root,text=" BREAKFAST ",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Breakfast)
    first_button.pack()
    first_button.place(x=0,y=200)
    button2=Button(root,text="    LUNCH    ",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Lunch)
    button2.pack()
    button2.place(x=140,y=200)
    button3=Button(root,text="   DINNER   ",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Dinner)
    button3.pack()
    button3.place(x=280,y=200)
    button4=Button(root,text="   SNACKS   ",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Snacks)
    button4.pack()
    button4.place(x=420,y=200)
    button5=Button(root,text="BEVERAGES",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Beverages)
    button5.pack()
    button5.place(x=20,y=350)
    button6=Button(root,text="   BREADS   ",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Breads)
    button6.pack()
    button6.place(x=160,y=350)
    button7=Button(root,text="  DESSERT  ",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=Desserts)
    button7.pack()
    button7.place(x=300,y=350)
    button7=Button(root,text="BACK",fg="white", bg="black",font='Calibri 16',relief='raised',activebackground='blue',command=close_window)
    button7.pack()
    button7.place(x=150,y=500)

    canvas = Canvas(root, bg = "#000000")
    photo=PhotoImage(master=canvas,file="rsz_photo6.png")
    label=Label(root,image=photo)
    label.pack()
    label.place(x=650,y=240)
    mainloop()

