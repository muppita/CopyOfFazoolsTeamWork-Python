from tkinter import *

#  1. Define player menu functions first

def requestDiscardAmount():
    label = Label(root, text = 'Enter number of cards you want to discard')
    label.pack()
    e = Entry(root)
    e.pack()
    b = Button(root, text = 'Discard', command = printEntry(e.get()))
    b.pack()
    
def printEntry(x):
    lab = Label(root, text = x)
    lab.pack()

def playerTurnMenu():

    # Show menu title
    title = Label(root, text = 'Player Turn Menu')
    title2 = Label(root, text = 'Choose 1 option')
    title.pack(fill = X)
    title2.pack(fill = X)

    # Show buttons for player turn actions
    button1 = Button(root,text = 'Pick up a route card')
    button2 = Button(root,text = 'Discard a route card', command = requestDiscardAmount)
    button3 = Button(root,text = 'Draw from train card deck')
    button4 = Button(root,text = 'Draw from train card stack')
    button5 = Button(root,text = 'Claim a route')
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

#  2. Player menu run loop below

root = Tk()

playerTurnMenu()

root.mainloop()
