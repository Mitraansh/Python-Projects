from tkinter import *
def menu():
    def close_window ():
        root.destroy()
    root = Tk()
    root.title("Menu")
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    button6=Button(root,text="BACK",fg="white", bg="black",font='Calibri 18',relief='raised',activebackground='blue',command=close_window)
    button6.pack(fill= X )
    scrollbar = Scrollbar(root)
    scrollbar.pack(side = RIGHT, fill = Y )

    test = Text(root,width=1000, height=2000, yscrollcommand = scrollbar.set )
    with open("MENU.txt", "r") as f:
        test.insert(INSERT,f.read())
    test.pack()
    scrollbar.config( command = test.yview )

    mainloop()