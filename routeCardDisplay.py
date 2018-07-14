import numpy as np 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from routeCardsAidanwithfloor import createRandomRoute #Will need this file in same directory
import cv2 

#list to be replaced with an actual list of players held routecards
playerXRouteCard = []
playerXRouteCardSmall = [None]*40
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())
playerXRouteCard.append(createRandomRoute())

root =tk.Tk()
w = Canvas(root, width=500, height=700)
w.pack()

arraySize = len(playerXRouteCard)

panel1 = None
panel2 = None
panel3 = None
panel4 = None
panel5 = None

index = 0

# Converting cv2 image objects to ImageTk objects for whole array
for x in range(0,arraySize) :
    b,g,r = cv2.split(playerXRouteCard[x])
    playerXRouteCard[x] = cv2.merge((r,g,b))
    im = Image.fromarray(playerXRouteCard[x])
    playerXRouteCard[x] = ImageTk.PhotoImage(image=im)
    i = im.resize((100, 76), Image.ANTIALIAS)
    playerXRouteCardSmall[x] = ImageTk.PhotoImage(image=i)

class nextButton:
    def __init__(self):
        
        self.nextButton = Button(w, text="->", command = self.nextButtonPress)
        self.nextButton.pack(side=LEFT, padx = 10)
        
    def nextButtonPress(self):
        global index
        if  index < 15 :
            index += 5
            refreshCards()
        else:
            self.nextButton.config(background="red")
        refreshCards()

    def refresh(self):
        self.nextButton.config(background = "gray")

class previousButton:
    def __init__(self):
        
        self.previousButton = Button(w, text="<-", command = self.previousButtonPress)
        self.previousButton.pack(side=LEFT, padx = 10)
        
    def previousButtonPress(self):
        global index
        if  index > 0 :
            index -= 5
            refreshCards()
        else:
            self.previousButton.config(background="red")

class panel:
    def __init__(self, position):
        global index
        self.position = position
        self.panel  = Button(w, image=playerXRouteCardSmall[position + index])
        self.panel.bind("<Enter>", self.maximize)
        self.panel.bind("<Leave>", self.minimize)
        self.panel.pack(side=LEFT)

    def maximize(self, event):
        self.panel.config(image=playerXRouteCard[self.position + index])

    def minimize(self, event) :
        self.panel.config(image=playerXRouteCardSmall[self.position + index])
    def refresh(self):
        self.panel.config(image=playerXRouteCardSmall[self.position + index])
        
    
def refreshCards() :
    panel1.refresh()
    panel2.refresh()
    panel3.refresh()
    panel4.refresh()
    panel5.refresh()

previous = previousButton()
panel1 = panel(0)
panel2 = panel(1)
panel3 = panel(2)
panel4 = panel(3)
panel5 = panel(4)
next = nextButton()
