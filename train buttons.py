from tkinter import *
import random


root=Tk()

colorsTrain = ["green", "red","pink", "grey", "yellow", "orange", "blue", "maroon", "black"]
def drawTrain():
    colours = random.choice(colorsTrain)
    return colours


def function():
    global carriageText
    carriage1.config(highlightbackground=drawTrain())
    carriage2.config(highlightbackground=drawTrain())
    carriage3.config(highlightbackground=drawTrain())
    carriage4.config(highlightbackground=drawTrain())
    carriage5.config(highlightbackground=drawTrain())


carriagePick = Button(root,text ="Pick a Carriage",command = function)

carriage1 = Button(root,text ="carriage",highlightbackground='white')
carriage2 = Button(root,text ="carriage",highlightbackground='white')
carriage3 = Button(root,text ="carriage",highlightbackground='white')
carriage4 = Button(root,text ="carriage",highlightbackground='white')
carriage5 = Button(root,text ="carriage",highlightbackground='white')




carriagePick.pack()

carriage1.pack(side = LEFT)
carriage2.pack(side = LEFT)
carriage3.pack(side = LEFT)
carriage4.pack(side = LEFT)
carriage5.pack(side = LEFT)

root.geometry("300x250+250+250")
root.mainloop()