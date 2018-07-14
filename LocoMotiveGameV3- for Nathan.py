import tkinter as tk
from tkinter import *
#import numpy as np 
from PIL import ImageTk, Image
from routeCardsAidanwithfloor import createRandomRoute #Will need this file in same directory
import cv2
import math
import random
from functools import partial


#https://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/

playerList=[]
compList=[]


p1BlueNum=0
p1GreenNum=0
p1RedNum=0
p1PinkNum=0
p1OrangeNum=0
p1YellowNum=0
p1LocoNum=0
p1Routes=0
p1Carriages=0
p1CarriageRem=40
p1Turn=0
index = 0

xIndex=[778, 796, 805, 811, 835, 853, 869, 873, 863, 840, 852, 786,
        785, 770, 882, 904, 923, 936, 726, 758, 765, 774, 794, 956,
        973, 679, 657, 643, 647, 639, 610, 580, 573, 578, 583, 587,
        593, 597, 603, 559, 564, 568, 573, 578, 584, 590, 998, 1002,
        993, 974, 922, 896, 880, 871, 860, 816, 806, 785, 757, 728,
        701, 677, 837, 848, 847, 844, 948, 928, 900, 870, 820, 796,
        787, 932, 903, 886, 794, 797, 801, 873, 855, 826, 953, 943,
        925, 905, 878, 850, 820, 801, 799, 798, 810, 785, 758, 727,
        748, 756, 750, 714, 707, 682, 683, 651, 624, 852, 838, 822,
        690, 667, 637, 608, 578, 549, 578, 547, 609, 613, 603, 588,
        566, 544, 623, 646, 659, 665, 663, 703, 695, 678, 652, 625,
        536, 509, 485, 462, 442, 418, 393, 578, 547, 520, 500, 479,
        401, 431, 456, 365, 344, 315, 286, 391, 391, 377, 354, 330,
        283, 301, 252, 228, 207, 213, 242, 272, 290, 279, 287, 325,
        341, 357, 317, 332, 347, 313, 342, 388, 417, 445, 474, 502,
        387, 416, 445, 474, 502, 449, 478, 508, 524, 351, 374, 404,
        317, 289, 273, 264, 273]
yIndex=[114, 118, 146, 102, 120, 142, 168, 199, 226, 196, 224, 169,
        200, 224, 261, 284, 310, 336, 235, 263, 292, 321, 343, 378,
        404, 222, 202, 177, 147, 111, 103, 112, 147, 177, 208, 238,
        269, 299, 330, 148, 178, 209, 239, 270, 301, 332, 448, 477,
        506, 528, 359, 371, 395, 421, 448, 369, 399, 417, 427, 435,
        447, 463, 356, 385, 414, 445, 521, 497, 484, 474, 468, 483,
        513, 539, 546, 571, 559, 590, 623, 622, 645, 651, 567, 597,
        620, 640, 657, 669, 664, 668, 700, 731, 758, 662, 668, 551,
        572, 602, 631, 528, 500, 483, 557, 552, 538, 271, 297, 324,
        534, 515, 507, 508, 511, 516, 533, 531, 374, 401, 430, 456,
        477, 497, 354, 371, 400, 427, 456, 258, 286, 310, 323, 335,
        125, 136, 151, 171, 194, 214, 231, 356, 353, 342, 324, 301,
        244, 242, 258, 269,291, 303, 312, 270, 300, 325, 343, 360,
        333, 358, 340, 355, 385, 414, 448, 460, 389, 416, 446, 395,
        422, 450, 401, 428, 454, 483, 486, 467, 476, 485, 496, 504,
        478, 487, 496, 507, 515, 557, 561, 561, 537, 565, 546, 543,
        598, 595, 551, 506, 480]

t=0

class mainPlayingBoard(object):
    def __init__(self,parent):
        """Constructor"""
        self.root=parent
        self.root.title(" Main Loco Motive Playing Board")
        self.frame=Frame(parent)
        self.frame.pack(fill="both",expand=True)
        self.canvas=Canvas(self.frame, width=screenWidth, height=screenHeight,background="#DCDCDC")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_text((screenWidth-screenWidth/7*2), 20, fill="green", font="courier 25 bold",
                                text ="Loco Motive", width=screenWidth*0.73, anchor="nw")
        mapPic=Image.open("board2.png")
        picWidth=int(screenWidth/10*7.2)
        picHeight=int(screenHeight/10*8.5)
        resizedMap=mapPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageMap = ImageTk.PhotoImage(resizedMap.convert("RGB"))
        photoLabel1=Label(image=imageMap)
        photoLabel1.image=imageMap
        photoLabel1.pack()
        self.canvas.create_image(screenWidth*(-0.04),0, image=imageMap,anchor = NW)
        scoreboardPic=Image.open("scoreboard_template.png")
        picWidth=int(screenWidth/10*2.8)
        picHeight=int(screenHeight/10*2.7)
        resizedScoreboard=scoreboardPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageScoreboard = ImageTk.PhotoImage(resizedScoreboard)
        photoLabel2=Label(image=imageScoreboard)
        photoLabel2.image=imageScoreboard
        photoLabel2.pack()
        self.canvas.create_image(screenWidth-screenWidth/7*2.5,screenHeight/2, image=imageScoreboard,anchor = NW)
        blueCarPic=Image.open("carriage_blue.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedBlueCar=blueCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriageBlue = ImageTk.PhotoImage(resizedBlueCar)
        photoLabel3=Label(image=imageCarriageBlue)
        photoLabel3.image=imageCarriageBlue
        photoLabel3.pack()
        self.canvas.create_image(screenWidth*0.006,screenHeight*0.87, image=imageCarriageBlue,anchor = NW)
        yellowCarPic=Image.open("carriage_yellow.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedYellowCar=yellowCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriageYellow = ImageTk.PhotoImage(resizedYellowCar)
        photoLabel4=Label(image=imageCarriageYellow)
        photoLabel4.image=imageCarriageYellow
        photoLabel4.pack()
        self.canvas.create_image(screenWidth/11+screenWidth/22+10,screenHeight*0.87, image=imageCarriageYellow,anchor = NW)
        redCarPic=Image.open("carriage_red.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedRedCar=redCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriageRed = ImageTk.PhotoImage(resizedRedCar)
        photoLabel5=Label(image=imageCarriageRed)
        photoLabel5.image=imageCarriageRed
        photoLabel5.pack()
        self.canvas.create_image(screenWidth/11*2+screenWidth/22*2+10,screenHeight*0.87, image=imageCarriageRed,anchor = NW)
        greenCarPic=Image.open("carriage_green.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedGreenCar=greenCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriageGreen = ImageTk.PhotoImage(resizedGreenCar)
        photoLabel6=Label(image=imageCarriageGreen)
        photoLabel6.image=imageCarriageGreen
        photoLabel6.pack()
        self.canvas.create_image(screenWidth/11*3+screenWidth/22*3+10,screenHeight*0.87, image=imageCarriageGreen,anchor = NW)
        orangeCarPic=Image.open("carriage_orange.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedOrangeCar=orangeCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriageOrange = ImageTk.PhotoImage(resizedOrangeCar)
        photoLabel7=Label(image=imageCarriageOrange)
        photoLabel7.image=imageCarriageOrange
        photoLabel7.pack()
        self.canvas.create_image(screenWidth/11*4+screenWidth/22*4+10,screenHeight*0.87, image=imageCarriageOrange,anchor = NW)
        pinkCarPic=Image.open("carriage_pink.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedPinkCar=pinkCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriagePink = ImageTk.PhotoImage(resizedPinkCar)
        photoLabel8=Label(image=imageCarriagePink)
        photoLabel8.image=imageCarriagePink
        photoLabel8.pack()
        self.canvas.create_image(screenWidth/11*5+screenWidth/22*5+10,screenHeight*0.87, image=imageCarriagePink,anchor = NW)
        locoCarPic=Image.open("train_card.png")
        picWidth=int(screenWidth/10*0.91)
        picHeight=int(screenHeight/10*1.12)
        resizedLocoCar=locoCarPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageCarriageLoco = ImageTk.PhotoImage(resizedLocoCar)
        photoLabel9=Label(image=imageCarriageLoco)
        photoLabel9.image=imageCarriageLoco
        photoLabel9.pack()
        self.canvas.create_image(screenWidth/11*6+screenWidth/22*6+10,screenHeight*0.87, image=imageCarriageLoco,anchor = NW)
        self.canvas.create_text(screenWidth/11+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1BlueNum), width=1200, anchor="nw")
        self.canvas.create_text(screenWidth/11*2+screenWidth/22+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1YellowNum), width=1200, anchor="nw")
        self.canvas.create_text(screenWidth/11*3+screenWidth/22*2+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1RedNum), width=1200, anchor="nw")
        self.canvas.create_text(screenWidth/11*4+screenWidth/22*3+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1GreenNum), width=1200, anchor="nw")
        self.canvas.create_text(screenWidth/11*5+screenWidth/22*4+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1OrangeNum), width=1200, anchor="nw")
        self.canvas.create_text(screenWidth/11*6+screenWidth/22*5+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1PinkNum), width=1200, anchor="nw")
        self.canvas.create_text(screenWidth/11*7+screenWidth/22*6+10, screenHeight*0.91, fill="green", font="courier 25 bold",
                                text ="x "+str(p1LocoNum), width=1200, anchor="nw")
        self.b1 = tk.Button(self.root, text = " Carriage card",font=("courier", 15),  command =self.openDrawTrainCards,
                            anchor = 'w',width = 15,height = 2,activebackground = "#33B5E5")
        pickcarriagecard_button_window = self.canvas.create_window(screenWidth-screenWidth/7*2.5, screenHeight/15*1.5, anchor='nw', window=self.b1)    
        self.b2 = tk.Button(self.root, text = "   Route card",font=("courier", 15),  command = self.openDrawRouteCards,
                            anchor = 'w', width = 15,height = 2, activebackground = "#33B5E5")
        pickroute_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.3, screenHeight/15*1.5, anchor='nw', window=self.b2)
        self.b3 = tk.Button(self.root, text = " Claim a route",font=("courier", 15),  command = self.openClaimARoute,
                            anchor = 'w', width = 15,height = 2, activebackground = "#33B5E5")
        claimroute_button_window = self.canvas.create_window(screenWidth-screenWidth/7*2.5, screenHeight/15*3.5, anchor='nw', window=self.b3)
        self.b4 = tk.Button(self.root, text = "    End Turn",font=("courier", 15),  command = root.quit,
                            anchor = 'w', width = 15,height = 2, activebackground = "#33B5E5")
        endturn_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.3, screenHeight/15*3.5, anchor='nw', window=self.b4)
        howtoplay_button = tk.Button(self.root, text = "   How to Play",font=("courier", 15),  command = self.howToPlay,
                                     anchor = 'w', width = 18,height = 1, activebackground = "#33B5E5")
        howtoplay_button_window = self.canvas.create_window(screenWidth-screenWidth/7*2, screenHeight/15*5.5, anchor='nw', window=howtoplay_button)
        routesList=self.routesListInfo
        carriagesList=self.carriagesListInfo
        carriagesRemList=self.carriagesRemInfo
        x=0
        y=screenHeight*0.63
        while(x<len(playerList)):
            self.c.create_text(screenWidth*0.68,y, fill="white", font="courier 15 bold", text =str(routesList[x]), width=1200, anchor="nw")
            self.c.create_text(screenWidth*0.71,y, fill="white", font="courier 12 bold", text =str(playerList[x]), width=1200, anchor="nw")
            self.c.create_text(screenWidth*0.78,y, fill="white", font="courier 15 bold", text =str(carriagesList[x]), width=1200, anchor="nw")
            self.c.create_text(screenWidth*0.85,y, fill="white", font="courier 15 bold", text =str(carriagesRemList[x]), width=1200, anchor="nw")
            y+=screenHeight*0.0244
            x+=1

    def hide(self):
        """"""
        self.root.withdraw()

    def openDrawTrainCards(self):
        subFrame=drawTrainCards(self)

    def openDrawRouteCards(self):
        subFrame=drawRouteCards(self)

    def openClaimARoute(self):
        subFrame=claimeARoute(self)

    def howToPlay(self):
        ABOUT_TEXT = """HOW TO PLAY


    Choose number of human players 1-6
    Choose number of computer players (to make 2-6 players total)
    Each player given 40 train tracks of their colour.
    Each player given 3 route cards
    Each players can choose to discard 0, 1 route cards at the start.
    Must keep at least 2 to begin with.
    Each player given 5 train cards.
    Randomise who goes first.

    On player turn, they choose only one of the following plays:
    a.Pick up 2 more train cards
    b. Pick up 3 more route cards (can then discard 0,1 or 2 of newly
    picked up cards,must keep original route cards and at least one of new
    three picked up)
    c. Claim a route (exchange at least 1 locomotive card and the correct
    number of correct coloured carriage cards to place train carriages
     along the route of the matching colour)

    (The claim a route here is different to the original to make our game a bit different.
    So on our board, you would need a locomotive card and 7 yellow cards to claim Broome
    to Darwin. You would need a Locomotive card and 1 red card to claim Perth to Bunbury (Augusta))

    When a player claims a route the following points are awarded:
    1 carriage=1 point
    2 carriages=2 points
    3 carriages=4 points
    4 carriages=7 points
    5 carriages=10 points
    6 carriages=15 points
    7 carriages=20 points

    When a player completes a route they are awarded the number of points indicated on the route card.
    This is based on the distance between the cities regardless of the route taken.
    Points are added to the players score as they complete the route.

    The game ends when a player has 0, 1 or 2 carriages left.  
    Any uncompleted route card values are subtracted from the playerâ€™s score. 
    The player with the highest points wins."""
        toplevel = Toplevel()
        label1 = Label(toplevel, text=ABOUT_TEXT,font=("courier", 12,), height=0, width=120)
        label1.pack()
        toplevel.title("How To Play")
        c = Button(toplevel, text="Close Window", width=20, command=toplevel.destroy)
        c.pack(side='top',padx=5,pady=30)   

    def routesListInfo(self):
        numPlayers=len(playerList)
        routesList=[0]*numPlayers
        #print (playerList)
        return (routesList)        

    def carriagesListInfo(self):
        numPlayers=len(playerList)
        carriagesList=[0]*numPlayers
        #print (playerList)
        return(carriagesList)

    def carriagesRemInfo(self):
        numPlayers=len(playerList)
        carriageRemList=[40]*numPlayers
        #print (playerList)
        return(carriageRemList)


    def openStartMenu(self):
        """"""
        #self.hide()
        #subFrame=OtherFrame()
        #handler=lambda;self.onCloseOtherFrame(subFrame)
        #button=Tk.Button

    def show(self):
        """"""
        self.root.update()
        sel.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    screenWidth=root.winfo_screenwidth()
    screenHeight=(root.winfo_screenheight())-80
    root.geometry("%sx%s" %(screenWidth,screenHeight))
    app = mainPlayingBoard(root)
    root.mainloop()



        

class drawTrainCards(object):
    
    def __init__(self,original):
        toplevel=tk.Toplevel()
        self.original_frame=original
        self.root=toplevel
        self.frame=Frame(self.r)
        self.f.pack(fill="both",expand=True)
        if p1Turn==0:
            w=850
        else:
            w=340
        self.c = Canvas(self.f, width=w, height=240,background="#DCDCDC")
        self.c.pack(fill="both", expand=True)
        imageList=cardList()
        i=0
        x=20
        while (i<len(imageList)):
            image= ImageTk.PhotoImage(file=imageList[i])
            photoLabel=Label(image=image)
            photoLabel.image=image
            photoLabel.pack()
            self.c.create_image(x,20, image=image,anchor = NW)
            i+=1
            x+=170
        self.b = tk.Button(self.r, text = " OK",font=("courier", 15),  command = self.refresh, anchor = 'w', width = 5,height = 2, activebackground = "#33B5E5")
        button_window = self.c.create_window(w-75, 170, anchor='nw', window=self.b)
     
    def refresh(self):
        self.destroy()
        self.original_frame.hide()
        self.original_frame.update()
        self.original_frame.show()

class drawRouteCards(object):
    def __init__(self,position):
        self.position = position
