"""This is for you somya,sucker"""
from Tkinter import *
import tkMessageBox
import random
main=Tk()
main.minsize(width=666,height=444)
#main.mainloop()

#now we need to create labels to display numbers
label1=Label(main,text="Begin",font=("Courier", 20))
label2=Label(main,text="Begin",font=("Courier", 20))
label3=Label(main,text="Begin",font=("Courier", 20))
label1.grid()
label2.grid()
label3.grid()
#fucntion to generate random numbers
def randomGen():
    label1["text"]=random.randint(0,9)
    label2["text"]=random.randint(0,9)
    label3["text"]=random.randint(0,9)
#definig a global variable should be avoided
    global id1
    id1=main.after(200, randomGen)
#function to set numbers

#fucntion to stop the roulette and compare the values of three labels
def numbercheck():
    main.after_cancel(id1)
    if label1["text"]==label2["text"]==label3["text"]:
        tkMessageBox.showinfo("3 out of 3","You won,you sexy bastard..!")
    elif label1["text"]==label2["text"] or label3["text"]==label2["text"] or label1["text"]==label3["text"]:
        tkMessageBox.showinfo("2 out of 3","Almost there, better luck next time")
    else:
        tkMessageBox.showinfo("none out of 3","Luck is not on your side ..!")
#defining the start and stop buttons
startButton=Button(main,text="start",command=randomGen)
stopButton=Button(main,text="stop",command=numbercheck)
startButton.grid()
stopButton.grid()

#main.after(1,randomGen())







main.mainloop()
