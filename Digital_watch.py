
from tkinter import *
import time

window = Tk()
window.title('Digital clock')
window.geometry('600x400')

def myTime():
    hour = time.strftime('%I')
    minute = time.strftime("%M")
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime("%A")
    zone = time.strftime("%Z")


    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone

    mylabel.config(text=myText)
    mylabel2.config(text=myText2)
    mylabel.after(1000, myTime)


mylabel = Label(window, text= "", font= ('Arial' , 72), fg='white', background= 'gray')
mylabel.pack()
mylabel2 = Label(window, text="", font=("Arial", 24))
mylabel2.pack()

myTime()

window.mainloop()