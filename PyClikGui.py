from tkinter import *
import pyautogui as pg  ##pip install pyautogui
import time

master=Tk()
master.title("SnowFlake")
master.geometry('300x165')
master.maxsize(300,165)
master.minsize(300,165)

def auto():
    a=1
    while(a!=0):
        time.sleep(5)
        pg.click(600,520)
        pg.typewrite("Create table new (")
        pg.typewrite("s.no, name) ")
        time.sleep(11)
        pg.click(700,400)
        pg.doubleClick(780,396)
        time.sleep(17)
        pg.doubleClick(400, 378)
        time.sleep(22)
        pg.click(500, 539)
        pg.doubleClick(600, 350)
        pg.typewrite("double ")

label1 = Label(master,text="Welcome User!!",padx=5,pady=5,font=("roboto",18,"bold"))
button1 = Button(master,text="Start!!",command=auto,padx=40,pady=5)
button2 = Button(master,text="End",command=master.quit,padx=58,pady=5)


label1.grid(row=0,column=0)
button1.grid(row=2,column=0)
button2.grid(row=3,column=0)

master.mainloop()