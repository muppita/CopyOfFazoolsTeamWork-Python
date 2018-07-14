from tkinter import *
import random


root=Tk()

colorsTrain = ["green", "red","pink", "grey", "yellow", "orange", "blue", "maroon", "black"]
def drawTrain():
    colours = random.choice(colorsTrain)
    return colours

def function():
    global carriageText
    carriage1colour = drawTrain()
    carriage2colour = drawTrain()
    carriage3colour = drawTrain()
    carriage4colour = drawTrain()
    carriage5colour = drawTrain()
    carriage1.config(background=carriage1colour, highlightbackground =carriage1colour)
    carriage2.config(background=carriage2colour, highlightbackground =carriage2colour)
    carriage3.config(background=carriage3colour, highlightbackground =carriage3colour)
    carriage4.config(background=carriage4colour, highlightbackground =carriage4colour)
    carriage5.config(background=carriage5colour, highlightbackground =carriage5colour)



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


