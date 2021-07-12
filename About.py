from tkinter import*

def about():
    def close_window ():
        screen1.destroy()
    screen1=Tk()
    screen1.title("About")
    screen1.overrideredirect(True)
    screen1.geometry("{0}x{1}+0+0".format(screen1.winfo_screenwidth(), screen1.winfo_screenheight()))

    Label(screen1,text="").pack()
    welcome_text = Label(screen1,text="MRK'S RESTAURANT",fg="white", bg="black",font='Calibri 20 bold ')
    welcome_text.pack()

    a=Label(screen1,text='''WAY-BACK
     Family Recipe
     It all started way back in the mid twentieth century, when a small part of our family ventured out in Rajasthan and came to the city of Delhi. \nThey brought along with them an ancestral wealth recipes of traditional Indian Sweets developed over generations by our forefathers.
           
       
     THE PEHLI DUKAAN
     First Venture
     1950 saw the beginning of a new landmark in Delhi. Every evening a small shop of freshly made Sweets, Bhujia and other Namkeens was setup in Chandni Chowk. \nDelhiwallas loved the taste of what we offered. They started calling us MRK ka restaurant and a new brand was born.


     JOURNEY KI KAHANI
     Going to Delhi
     Our journey that started from Chandni Chowk has taken us to places.Fame of our quality Sweets and Namkeens soon spread far and wide and our market presence \nexpanded with opening of new outlets one after the other.
      
      
     DESH SE VIDESH TAK
     Our presence today
     The Company’s pursuit of excellence has earned it national and international reach. Today our brand  is not only a household name in India with 85 outlets, but has a global presence \nwith 26 of its outlets operating in UAE, Nepal, New Zealand, Singapore and USA. 


     SWAAD KA SAMMAN
     Awards
     Our constantly endeavours to benchmark its products, services and processes to global standards. Our quality has brought us awards and accolades time to time.\n We made a hattrick by being declared the Best Restaurant of Delhi in 2012, 2013 and 2014 by Times Food Awards.


      MRK FOODS PVT. LTD
     A-28 Lawrence Road
     Industrial Area, New Delhi,
     Delhi 110035, INDIA

     ''',font='times 12')
    a.pack()

    button6=Button(screen1,text="BACK",fg="white", bg="black",font='Calibri 14',relief='raised',activebackground='blue',command=close_window)
    button6.pack()
    button6.place(x=1850,y=1800)

