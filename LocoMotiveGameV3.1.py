import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np 
from PIL import ImageTk, Image
from routeCardsAidanwithfloor import createRandomRoute #Will need this file in same directory
import cv2
import math
import random
from functools import partial



#https://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/
#http://zetcode.com/gui/tkinter/layout/

playerList=[]
compList=[]
cardList=[]
keptRouteCardList=[]
discardList=[]
carriagesList=[]
carriageRemList=[]
routesList=[]
turn=0






blueNum1=0
greenNum1=0
redNum1=0
pinkNum1=0
orangeNum1=0
yellowNum1=0
locoNum1=0
p1BlueNum=[0]
p1GreenNum=[0]
p1RedNum=[0]
p1PinkNum=[0]
p1OrangeNum=[0]
p1YellowNum=[0]
p1LocoNum=[0]
p1Routes=0
p1Carriages=0
p1CarriageRem=40
resizedMap=""


p1Turn=0
cardClick=0
index = 0
scoreClick=0

routeScoresList = {
    'BroomeDarwin':7,
    'KarrathaBroome':4,
    'NewmanBroome':5,
    'KarrathaNewman':2,
    'NewmanLeonora':3,
    'MtmagnetNewman':3,
    'SharkbayMtmagnet':2,
    'MtmagnetLeonora':2,
    'PerthMtmagnet':2,
    'AugustaPerth':1,
    'AugustaAlbany':2,
    'AlbanyEsperance':3,
    'EsperanceBordervillage':4,
    'LeonoraEsperance':5,
    'EsperanceAlicesprings':6,
    'HallscreekAlicesprings':5,
    'BroomeHallscreek':3,
    'DarwinAlicesprings':7,
    'DarwinNhulunbuy':3,
    'NhulunbuyBurketown':4,
    'AlicespringsBurketown':5,
    'BurketownKarumba':1,
    'AlicespringsCooberpedy':5,
    'BordervillageAdelaide':6,
    'CooberpedyAdelaide':3,
    'AdelaidePortland':4,
    'CooberpedyMtisa':7,
    'KarumbaMtisa':4,
    'PortlandMelbourne':2,
    'KarumbaCapeyork':6,
    'CapeyorkCooktown':2,
    'CooktownMackay':2,
    'CapeyorkMackay':6,
    'MtisaMackay':3,
    'MackayBundaberg':4,
    'MtisaBourke':4,
    'BourkeBundaberg':5,
    'BundabergBrisbane':2,
    'MilduraBourke':3,
    'MelbourneMildura':3,
    'HobartMelbourne':4,
    'MelbourneCanberra':3,
    'MelbourneSydney':7,
    'CanberraSydney':3,
    'BourkeSydney':4,
    'SydneyBrisbane':4
}

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
claimedSpacesX=[3000,-100]
claimedSpacesY=[3000,-100]
player1Colour="smallRedTrak.png"


class mainPlayingBoard(object):
    def __init__(self,parent):
        """Constructor"""
        root.isStopped = False
        self.root=parent
        self.root.title(" Main Loco Motive Playing Board")
        self.frame=Frame(parent)
        self.frame.pack(fill="both",expand=True)
        self.canvas=Canvas(self.frame, width=screenWidth, height=screenHeight,background="#DCDCDC")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_text((screenWidth-screenWidth/7*1.5), 20, fill="black", font="courier 25 bold",
                                text ="Loco Motive", width=screenWidth*0.73, anchor="nw")
        global resizedMap
        mapPic=Image.open("board2.png")
        picWidth=int(screenWidth/10*6.8)
        picHeight=int(screenHeight/10*8.5)
        resizedMap=mapPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageMap = ImageTk.PhotoImage(resizedMap)
        photoLabel1=Label(image=imageMap)
        photoLabel1.image=imageMap
        photoLabel1.pack()
        self.canvas.create_image(0,0, image=imageMap,anchor = NW)
        scoreboardPic=Image.open("scoreboard_template.png")
        picWidth=int(screenWidth/10*2.8)
        picHeight=int(screenHeight/10*2.7)
        resizedScoreboard=scoreboardPic.resize((picWidth, picHeight),Image.ANTIALIAS)
        imageScoreboard = ImageTk.PhotoImage(resizedScoreboard)
        photoLabel2=Label(image=imageScoreboard)
        photoLabel2.image=imageScoreboard
        photoLabel2.pack()
        self.canvas.create_image(screenWidth-screenWidth/7*2.1,screenHeight/20*11, image=imageScoreboard,anchor = NW)
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
        #self.canvas.create_text(screenWidth/11+10, screenHeight*0.91, fill="green", font="courier 25 bold",
         #                       text ="x "+str(p1BlueNum), width=1200, anchor="nw")
        #self.canvas.create_text(screenWidth/11*2+screenWidth/22+10, screenHeight*0.91, fill="green", font="courier 25 bold",
        #                        text ="x "+str(p1YellowNum), width=1200, anchor="nw")
        #self.canvas.create_text(screenWidth/11*3+screenWidth/22*2+10, screenHeight*0.91, fill="green", font="courier 25 bold",
        #                        text ="x "+str(p1RedNum), width=1200, anchor="nw")
        #self.canvas.create_text(screenWidth/11*4+screenWidth/22*3+10, screenHeight*0.91, fill="green", font="courier 25 bold",
         #                       text ="x "+str(p1GreenNum), width=1200, anchor="nw")
        #self.canvas.create_text(screenWidth/11*5+screenWidth/22*4+10, screenHeight*0.91, fill="green", font="courier 25 bold",
         #                       text ="x "+str(p1OrangeNum), width=1200, anchor="nw")
        #self.canvas.create_text(screenWidth/11*6+screenWidth/22*5+10, screenHeight*0.91, fill="green", font="courier 25 bold",
         #                       text ="x "+str(p1PinkNum), width=1200, anchor="nw")
        #self.canvas.create_text(screenWidth/11*7+screenWidth/22*6+10, screenHeight*0.91, fill="green", font="courier 25 bold",
          #                      text ="x "+str(p1LocoNum), width=1200, anchor="nw")
        self.b1 = tk.Button(self.root, text = " Carriage card",font=("courier", 15),  command =self.drawTrainCards,
                            anchor = 'w',width = 15,height = 2,activebackground = "#33B5E5")
        pickcarriagecard_button_window = self.canvas.create_window(screenWidth-screenWidth/7*2.2, screenHeight/15*1.5, anchor='nw', window=self.b1)    
        self.b2 = tk.Button(self.root, text = "   Route card",font=("courier", 15),  command = self.drawRouteCards,
                            anchor = 'w', width = 15,height = 2, activebackground = "#33B5E5")
        pickroute_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.1, screenHeight/15*1.5, anchor='nw', window=self.b2)
        self.b3 = tk.Button(self.root, text = " Claim a route",font=("courier", 15),  command = self.claimARoute,
                            anchor = 'w', width = 15,height = 2, activebackground = "#33B5E5")
        claimroute_button_window = self.canvas.create_window(screenWidth-screenWidth/7*2.2, screenHeight/15*3.2, anchor='nw', window=self.b3)
        self.b4 = tk.Button(self.root, text = "    End Turn",font=("courier", 15),  command = root.quit,
                            anchor = 'w', width = 15,height = 2, activebackground = "#33B5E5")
        endturn_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.1, screenHeight/15*3.2, anchor='nw', window=self.b4)
        howtoplay_button = tk.Button(self.root, text = "   How to Play",font=("courier", 15),  command = self.howToPlay,
                                     anchor = 'w', width = 18,height = 1, activebackground = "#33B5E5")
        howtoplay_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.6, screenHeight/15*5.9, anchor='nw', window=howtoplay_button)
        quit_button = tk.Button(self.root, text = "      Quit",font=("courier", 15),  command = self.askQuit,
                                     anchor = 'w', width = 18,height = 1, activebackground = "#33B5E5")
        quit_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.6, screenHeight/15*7, anchor='nw', window=quit_button)
        routecards_button = tk.Button(self.root, text = "  View Current Routes", font=("courier", 15),  command = self.displayRouteCards,
                                     anchor = 'w', width = 22,height = 1, activebackground = "#33B5E5")
        routecards_button_window = self.canvas.create_window(screenWidth-screenWidth/7*1.7, screenHeight/15*4.9, anchor='nw', window=routecards_button)
        
        
         #self.after(1000,self.update())

    

    def askQuit(self):
        if messagebox.askokcancel("Are you sure you want to quit?"):
            root.isStopped=True
            #global keptRouteCardList
            #print (keptRouteCardList)
            
            root.destroy()
            root.quit()
            
        
    def hide(self):
        """"""
        self.root.withdraw()

    def button_callback(self,toplevel,button_num):
        toplevel.destroy()
        global numButton
        numButton=button_num
        #print(button_num)
        allRoutesFunctionsList=[capeYToWeipa,capeToCooktown,capeYToMackay,cooktownToMackay,weipaToKarumba,MackayToBundy,
                                karumbaToBurketown,karumbaToMtIsa,bundyToBrisbane,burketownToNhulunbuy,nhulunbuyToDarwin,
                                darwinToAliceA,darwinToAliceB,brisbaneToSydney,bundyToBourke,mtIsaToCooberPedy,mtIsaToBourke,
                                sydneyToBourke,bourkeToBrokenHill,sydneyToCanberra,brokenHillToMelbs,canberraToMelbs,sydneyToMelbs,
                                melbsToHobart,melbsToPortland,adelaideToPortland,adelaideToCooberPedy,adelaideToCeduna,mackayToMtIsa,
                                adelaideToBorderVillage,cedunaToBorderVillage,aliceToBorderVillage,aliceToCooberPedy,burketownToAlice,
                                darwinToBroome,aliceToHallsCreek,broomeToHallsCreek,broomeToKaratha,broomeToNewman,karathaToNewman,
                                karathaToExmouth,exmouthToCarnarvan,carnarvanToMtMagnet,newmanToMtMagnet,newmanToKarlgoolieA,
                                newmanToKarlgoolieB,mtMagnetToKarlgoolie,karlgoolieToBorberVillageA,karlgoolieToBorberVillageB,
                                esperanceToBorderVillage,albanyToEsperance,albanyToBunbury,perthToBunbury,perthToMtMagnet]
        f=allRoutesFunctionsList[numButton]
        f()
        #if numButton==0:
            #print ("Yes")
          #  capeYToWeipa()

    def claimARoute(self):
        
        toplevel=Toplevel()
        toplevel.title("Which route would you like to claime?")
        self.root=toplevel
        self.frame=Frame(self.root)
        self.frame.grid()
        self.label=Label(self.frame, text="")
        self.label.grid(row=0, column=0, columnspan=5)
        self.list_of_button_ids=[]
        allRoutesList=allRoutes()
        i=0
        while (i<len(allRoutesList)):
            button = Button(self.frame, text=str(allRoutesList[i]), width = 27, height = 4, padx = 2, pady = 1,command=lambda i=i:self.button_callback(toplevel,i))
            #command=lambda i=i:self.button_callback(parent,canvas,i) - does same as command above
            this_row, this_col=divmod(i, 9)
            button.grid(row=this_row+1, column=this_col)
            self.list_of_button_ids.append(button)
            i+=1
    



    

        

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
    c. Claim a route (exchange the correct number of correct coloured carriage
    cards to place train carriages along the route of the matching colour. Grey routes require LocoMotive cards.)

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
    Any uncompleted route card values are subtracted from the player’s score. 
    The player with the highest points wins."""
        toplevel = Toplevel()
        label1 = Label(toplevel, text=ABOUT_TEXT,font=("courier", 12,), height=0, width=120)
        label1.pack()
        toplevel.title("How To Play")
        c = Button(toplevel, text="Close Window", width=20, command=toplevel.destroy)
        c.pack(side='top',padx=5,pady=30)   

    


    def drawRouteCards(self):
        
        toplevel = Toplevel()
        global p1Turn
        #if p1Turn==0:
        w=720
        #else:
         #   w=340
        label1=Label(toplevel,text="Route Cards Drawn",font=("courier", 12,),width=w, height=280)
        #self.original_frame=original
        toplevel.root=toplevel
        
        #print(self)
        
        toplevel.canvas = Canvas(toplevel, width=w, height=280,background="#DCDCDC")
        #toplevel.canvas.pack(fill="both", expand=True)
        toplevel.frame=Frame(toplevel.root)
        #toplevel.frame.pack(fill="both",expand=True)
        imageList=randomRouteCardList()
        print (imageList)
        #i=0
        #x=20
        #column=0
        #while (i<len(imageList)):
        route_image_1= imageList[0]
        photoLabel=Label(toplevel,image=route_image_1)
        photoLabel.image=route_image_1
            #photoLabel.pack()
            #routeCard=toplevel.canvas.create_image(x,20, image=image,anchor = NW)
        photoLabel.grid(row=0, column=0,columnspan=2, sticky=NW)
            #i+=1
            #x+=220
            #column+=2
        route_image_2= imageList[1]
        photoLabel=Label(toplevel,image=route_image_2)
        photoLabel.image=route_image_2
            #photoLabel.pack()
            #routeCard=toplevel.canvas.create_image(x,20, image=image,anchor = NW)
        photoLabel.grid(row=0, column=2,columnspan=2, sticky=NW)
        route_image_3= imageList[2]
        photoLabel=Label(toplevel,image=route_image_3)
        photoLabel.image=route_image_3
            #photoLabel.pack()
            #routeCard=toplevel.canvas.create_image(x,20, image=image,anchor = NW)
        photoLabel.grid(row=0, column=4,columnspan=2, sticky=NW)
        #toplevel.b_ok = tk.Button(toplevel.root, text = " OK",font=("courier", 15),  command = toplevel.root.destroy, anchor = 'w', width = 5,height = 2, activebackground = "#33B5E5")
        #ok_button_window = toplevel.canvas.create_window(w-75, 200, anchor='nw', window=toplevel.b_ok)
        options1=["Keep","Discard"]
        variable1=StringVar(toplevel)
        variable1.set(options1[0])
        options2=["Keep","Discard"]
        variable2=StringVar(toplevel)
        variable2.set(options2[0])
        options3=["Keep","Discard"]
        variable3=StringVar(toplevel)
        variable3.set(options3[0])
        #menu1=OptionMenu(toplevel,variable,*options)
        #menu_button_window = toplevel.canvas.create_window(w+100, 200, anchor='nw', window=menu1)
        #menu1.pack()
        #i=0
        
        #column=0
        #while(i<len(imageList)):
        keep_button_1=tk.Radiobutton(toplevel,text="Keep", value="Keep", command=keep1(imageList[0],variable1),variable=variable1)
        keep_button_1.grid(row=1,column=0)
        discard_button_1=tk.Radiobutton(toplevel,text="Discard", value="Discard", command=keep1(imageList[0],variable1),variable=variable1)
        discard_button_1.grid(row=2,column=0)
        keep_button_2=tk.Radiobutton(toplevel,text="Keep", value="Keep", command=keep2(imageList[1],variable2),variable=variable2)
        keep_button_2.grid(row=1,column=2)
        discard_button_2=tk.Radiobutton(toplevel,text="Discard", value="Discard", command=keep2(imageList[1],variable2),variable=variable2)
        discard_button_2.grid(row=2,column=2)
        keep_button_3=tk.Radiobutton(toplevel,text="Keep", value="Keep", command=keep3(imageList[2],variable3),variable=variable3)
        keep_button_3.grid(row=1,column=4)
        discard_button_3=tk.Radiobutton(toplevel,text="Discard", value="Discard", command=keep3(imageList[2],variable3),variable=variable3)
        discard_button_3.grid(row=2,column=4)
        toplevel.b_ok = tk.Button(toplevel.root, text = " OK",font=("courier", 15),  command = toplevel.root.destroy, anchor = 'w', width = 5,height = 1, activebackground = "#33B5E5")
        toplevel.b_ok.grid(row=2,column=5)
        p1Turn+=1

    def openStartMenu(self):
        """"""
        #self.hide()
        subFrame=OtherFrame()
        handler=lambda:self.onCloseOtherFrame(subFrame)
        button=Tk.Button(subFrame, text="Close", command=handler)
        btn.pack()

    def show(self):
        """"""
        self.root.update()
        sel.root.deiconify()

    def drawTrainCards(self):
        
        toplevel = Toplevel()
        global p1Turn
        if p1Turn==0:
            w=850
        else:
            w=340
        label1=Label(toplevel,text="Train Cards Drawn",font=("courier", 12,),width=w, height=240)
        #self.original_frame=original
        toplevel.root=toplevel
        toplevel.frame=Frame(toplevel.root)
        toplevel.frame.pack(fill="both",expand=True)
        #print(self)
        
        toplevel.canvas = Canvas(toplevel.frame, width=w, height=240,background="#DCDCDC")
        toplevel.canvas.pack(fill="both", expand=True)
        imageList=cardList()
        i=0
        x=20
        while (i<len(imageList)):
            image= ImageTk.PhotoImage(file=imageList[i])
            photoLabel=Label(image=image)
            photoLabel.image=image
            photoLabel.pack()
            toplevel.canvas.create_image(x,20, image=image,anchor = NW)
            i+=1
            x+=170
        toplevel.b = tk.Button(toplevel.root, text = " OK",font=("courier", 15),  command = toplevel.root.destroy, anchor = 'w', width = 5,height = 2, activebackground = "#33B5E5")
        button_window = toplevel.canvas.create_window(w-75, 170, anchor='nw', window=toplevel.b)
        global cardClick
        cardClick+=1
        p1Turn+=1
        #self.value=self.root.get()
        #root.update_idletasks()
        #self.canvas.after(1000,self.canvas.update)
        #print(p1BlueNum,p1GreenNum,p1RedNum,p1PinkNum,p1OrangeNum,p1YellowNum,p1LocoNum)



    def displayRouteCards(self):
        # Aidan - call your class function here
        print("Needs stuff here")
        
        


#add you clesses and functions here.  The list you want to display is keptRouteCardList.
        #It's currently creating a list of route cards but it's not working properly.  It's
        #working enough to make your stuff work though.


def allRoutes():
    allRoutesList=["Cape York to Weipa","Cape York to Cooktown","CapeYork to Mackay","Cooktown to Mackay",
                   "Weipa to Karumba","Mackay to Bundaberg","Karumba to Burketown","Karumba to Mt Isa",
                   "Bundaberg to Brisbane", "Burketown to Nhulunbuy", "Nhulunbuy to Darwin","Darwin to Alice Springs Grey",
                   "Darwin to Alice Springs Blue","Brisbane to Sydney","Bundaberg to Bourke","Mt Isa to Coober Pedy",
                   "Mt Isa to Bourke","Sydney to Bourke","Bourke to Broken Hill","Sydney to Canberra","Broken Hill to Melbourne",
                   "Canberra to Melbourne","Sydney to Melbourne","Melbourne to Hobart","Melbourne to Portland",
                   "Adelaide to Portland","Adelaide to Coober Pedy","Adelaide to Ceduna","Mackay to Mt Isa",
                   "Adealide to Border Village","Ceduna to Border Village","Alice Springs to Border Village",
                   "alice Springs to Coober Pedy","Burketown to Alice Springs","Darwin to Broome","Alice Springs to Halls Creek",
                   "Broome to Halls Creek","Broome to Karatha","Broome to Newman","Karatha to Newman","Karatha to Exmouth",
                   "Exmouth to Carnarvon","Carnarvon to Mt Magnet","Newman to Mt Magnet","Newman to Karlgoolie 1",
                   "Newman to Karlgoolie 2","Mt Magnet to Karlgoolie","Karlgoolie to Border Village Yellow",
                   "Karlgoolie to Border Village Red","Esperance to Border Village","Albany to Esperance","Albany to Bunbury",
                   "Perth to Bunbury","Perth to Mt Magnet"]
    #print(len(allRoutesList))
    return (allRoutesList)

def allRouteFunctions(i):
    allRoutesFunctionsList=["capeYToWeipa()","capeToCooktown()","capeYToMackay()","cooktownToMackay()","weipaToKarumba","mackayToBundy()","Karumba to Burketown","Karumba to Mt Isa","Bundaberg to Brisbane", "Burketown to Nhulunbuy", "Nhulunbuy to Darwin","Darwin to Alice Springs Blue","Darwin to Alice Springs Grey","Brisbane to Sydney","Bundaberg to Bourke","Mt Isa to Coober Pedy","Mt Isa to Bourke","Sydney to Bourke","Bourke to Broken Hill","Sydney to Canberra","Broken Hill to Melbourne","Canberra to Melbourne","Sydney to Melbourne","Melbourne to Hobart","Melbourne to Portland","Adelaide to Portland","Adelaide to Coober Pedy","Adelaide to Ceduna","Mackay to Mt Isa","Adealide to Border Village","Ceduna to Border Village","Alice Springs to Border Village","alice Springs to Coober Pedy","Burketown to Alice Springs","Darwin to Broome","Alice Springs to Halls Creek","Broome to Halls Creek","Broome to Karatha","Broome to Newman","Karatha to Newman","Karatha to Exmouth","Exmouth to Carnarvon","Carnarvon to Mt Magnet","Newman to Mt Magnet","Newman to Karlgoolie 1","Newman to Karlgoolie 2","Mt Magnet to Karlgoolie","Karlgoolie to Border Village Yellow","Karlgoolie to Border Village Red","Esperance to Border Village","Albany to Esperance","Albany to Bunbury","Perth to Bunbury","Perth to Mt Magnet"]
    action=allRoutesFunctionsList[i]


def keep1(image,variable1):
    global keptRouteCardList
    kept=variable1.get()
    if kept=="Keep":
        keptRouteCardList.append(image)
        
    if kept=="Discard":
        keptRouteCardList.remove(image)

def keep2(image,variable2):
    global keptRouteCardList
    kept=variable2.get()
    if kept=="Keep":
        keptRouteCardList.append(image)
        
    if kept=="Discard":
        keptRouteCardList.remove(image)

def keep3(image,variable3):
    global keptRouteCardList
    kept=variable3.get()
    if kept=="Keep":
        keptRouteCardList.append(image)
        
    if kept=="Discard":
        keptRouteCardList.remove(image)


    
    

class startWindow(object):
    def __init__(self,parent):
        #tk.Toplevel.__init__(self)
        top=Toplevel()
        self.myParent=parent
        self.r=top
        self.r.title("Start Menu")
        self.frame=Frame(self.r)
        self.frame.pack(fill="both",expand=True)
        self.r.lift()
        self.r.attributes("-topmost", True)
        self.b=Button(self.frame,text="Add Human Player",command=self.popup)
        self.b.pack()
        self.b2=Button(self.frame,text="Add Computer Player",command=self.addComputer)
        self.b2.pack()
        self.b3=Button(self.frame,text="Start",command=self.hide)
        self.b3.pack()
        

    def popup(self):
        self.w=popupWindow(self.r)
        self.b["state"] = "disabled" 
        self.r.wait_window(self.w.top)
        self.b["state"] = "normal"
        global PlayerList
        playerList.append(self.w.value)
        print (playerList)

    def hide(self):
        """"""
        self.r.destroy()
        #parent=mainPlayingBoard()
        #parent.update()
        #self.value=self.master.get()
        #self.master.destroy()

    def addComputer(self):
        compList.append("Computer")
        compNum=len(compList)
        compPlayer="Computer "+str(compNum)
        global playerList
        playerList.append(compPlayer)
        #print(playerList)
     
    def entryValue(self):
        print (playerList)
        numPlayers=len(playerList)
        routesList=[0]*numPlayers
        carriagesList=[0]*numPlayers
        carriageRemList=[40]*numPlayers
        #print (routesList)
        #print(carriagesList)
        #print(carriageRemList)

class popupWindow(object):
    def __init__(self,master):
        self.top=Toplevel(master)
        self.top.attributes("-topmost", True)
        self.l=Label(self.top,text="Human Player Name")
        self.l.pack()
        self.e=Entry(self.top)
        self.e.pack()
        self.b=Button(self.top,text='Ok',command=self.cleanup)
        self.b.pack()
        
     
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()


def capeYToWeipa(): #1
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))
    global carriagesList
    global carriageRemList
    carriagesList[turn]+=1
    carriageRemList[turn]-=1
    global p1LocoNum
    global cardClick
    p1LocoNum[cardClick]-=1
    
    print (carriageRemList[scoreClick])
    print(carriagesList[scoreClick])
    scoreClick+=1

    
    

def capeToCooktown(): #2
    claimedSpacesX.append(int(math.floor(screenWidth*0.468)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.473)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.150)))
    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1LocoNum[cardClick]-=2

def capeYToMackay(): #3
    claimedSpacesX.append(int(math.floor(screenWidth*0.476)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.108)))
    
    claimedSpacesX.append(int(math.floor(screenWidth*0.493)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.125)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.503)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.150)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.511)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.178)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.518)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.208)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.511)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.242)))
    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=6
    carriageRemList[turn]-=6
    p1LocoNum[cardClick]-=6

def cooktownToMackay(): #4
    claimedSpacesX.append(int(math.floor(screenWidth*0.484)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.200)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.493)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.230)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1LocoNum[cardClick]-=2

def weipaToKarumba(): #5
    claimedSpacesX.append(int(math.floor(screenWidth*0.448)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.1685)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.448)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.205)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.438)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.229)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1OrangeNum[cardClick]-=3

def MackayToBundy(): #6
    claimedSpacesX.append(int(math.floor(screenWidth*0.511)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.272)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.526)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.292)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.536)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.322)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.546)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.352)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1LocoNum[cardClick]-=4
    
def karumbaToBurketown(): #7
    claimedSpacesX.append(int(math.floor(screenWidth*0.410)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.242)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=1
    carriageRemList[turn]-=1
    p1LocoNum[cardClick]-=1
    
def karumbaToMtIsa(): #8
    claimedSpacesX.append(int(math.floor(screenWidth*0.430)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.272)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.435)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.300)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.440)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.330)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.455)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.360)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1RedNum[cardClick]-=4

def bundyToBrisbane(): #9
    claimedSpacesX.append(int(math.floor(screenWidth*0.559)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.395)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.569)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.420)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1YellowNum[cardClick]-=2

def burketownToNhulunbuy(): #10
    claimedSpacesX.append(int(math.floor(screenWidth*0.380)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.229)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.365)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.207)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.358)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.182)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.359)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.152)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1PinkNum[cardClick]-=4
    
def nhulunbuyToDarwin(): #11
    claimedSpacesX.append(int(math.floor(screenWidth*0.357)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.112)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.337)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.103)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.317)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.112)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def darwinToAliceA(): #12
    claimedSpacesX.append(int(math.floor(screenWidth*0.302)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.147)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.305)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.182)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.308)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.216)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.313)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.252)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.314)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.282)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.317)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.312)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.320)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.347)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=7
    carriageRemList[turn]-=7
    p1LocoNum[cardClick]-=7

def darwinToAliceB(): #13
    claimedSpacesX.append(int(math.floor(screenWidth*0.313)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.142)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.316)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.177)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.320)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.211)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.326)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.247)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.327)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.277)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.332)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.307)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.334)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.342)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=7
    carriageRemList[turn]-=7
    p1BlueNum[cardClick]-=7

def brisbaneToSydney(): #14
    claimedSpacesX.append(int(math.floor(screenWidth*0.587)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.470)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.590)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.500)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.587)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.530)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.572)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.558)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1BlueNum[cardClick]-=4

def bundyToBourke(): #15
    claimedSpacesX.append(int(math.floor(screenWidth*0.536)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.372)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.521)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.385)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.511)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.410)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.505)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.440)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.498)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.467)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1OrangeNum[cardClick]-=5

def mtIsaToCooberPedy(): #16
    claimedSpacesX.append(int(math.floor(screenWidth*0.470)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.385)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.465)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.415)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.450)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.435)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.430)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.445)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.410)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.455)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.396)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.465)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.380)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.482)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=7
    carriageRemList[turn]-=7
    p1YellowNum[cardClick]-=7
    

def mtIsaToBourke():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1PinkNum[cardClick]-=4

def sydneyToBourke():

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1RedNum[cardClick]-=4
    

def bourkeToBrokenHill():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1GreenNum[cardClick]-=3

def sydneyToCanberra():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1OrangeNum[cardClick]-=3

def brokenHillToMelbs():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def canberraToMelbs():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def sydneyToMelbs():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=7
    carriageRemList[turn]-=7
    p1GreenNum[cardClick]-=7

def melbsToHobart():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1BlueNum[cardClick]-=4

def melbsToPortland():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1YellowNum[cardClick]-=2

def adelaideToPortland():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1RedNum[cardClick]-=4

def adelaideToCooberPedy():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def adelaideToCeduna():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1OrangeNum[cardClick]-=3

def mackayToMtIsa():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1BlueNum[cardClick]-=3

def adelaideToBorderVillage():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=6
    carriageRemList[turn]-=6
    p1PinkNum[cardClick]-=6

def cedunaToBorderVillage():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1LocoNum[cardClick]-=2

def aliceToBorderVillage():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=6
    carriageRemList[turn]-=6
    p1RedNum[cardClick]-=6

def aliceToCooberPedy():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1LocoNum[cardClick]-=5

def burketownToAlice():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1GreenNum[cardClick]-=5

def darwinToBroome():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=7
    carriageRemList[turn]-=7
    p1YellowNum[cardClick]-=7

def aliceToHallsCreek():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1PinkNum[cardClick]-=5

def broomeToHallsCreek():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3


def broomeToKaratha():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1GreenNum[cardClick]-=4



def broomeToNewman():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1OrangeNum[cardClick]-=5

def karathaToNewman():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1LocoNum[cardClick]-=2

def karathaToExmouth():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1OrangeNum[cardClick]-=2

def exmouthToCarnarvan():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1GreenNum[cardClick]-=2

def carnarvanToMtMagnet():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1YellowNum[cardClick]-=2

def newmanToMtMagnet():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1PinkNum[cardClick]-=3

def newmanToKarlgoolieA():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def newmanToKarlgoolieB():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def mtMagnetToKarlgoolie():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1LocoNum[cardClick]-=2

def karlgoolieToBorberVillageA():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1YellowNum[cardClick]-=5

def karlgoolieToBorberVillageB():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=5
    carriageRemList[turn]-=5
    p1RedNum[cardClick]-=5

def esperanceToBorderVillage():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=4
    carriageRemList[turn]-=4
    p1BlueNum[cardClick]-=4

def albanyToEsperance():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=3
    carriageRemList[turn]-=3
    p1LocoNum[cardClick]-=3

def albanyToBunbury():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1BlueNum[cardClick]-=2

def perthToBunbury():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=1
    carriageRemList[turn]-=1
    p1RedNum[cardClick]-=1

def perthToMtMagnet():
    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    claimedSpacesX.append(int(math.floor(screenWidth*0.453)))
    claimedSpacesY.append(int(math.floor(screenHeight*0.120)))

    global carriagesList
    global carriageRemList
    global p1LocoNum
    global cardClick
    carriagesList[turn]+=2
    carriageRemList[turn]-=2
    p1GreenNum[cardClick]-=2
    

def randomRouteCardList():
    playerXRouteCard = []
    playerXRouteCardSmall = [None]*3
    playerXRouteCard.append(createRandomRoute())
    playerXRouteCard.append(createRandomRoute())
    playerXRouteCard.append(createRandomRoute())
    arraySize = len(playerXRouteCard)
    for x in range(0,arraySize) :
        b,g,r = cv2.split(playerXRouteCard[x])
        playerXRouteCard[x] = cv2.merge((r,g,b))
        im = Image.fromarray(playerXRouteCard[x])
        playerXRouteCard[x] = ImageTk.PhotoImage(image=im)
        i = im.resize((200, 152), Image.ANTIALIAS)
        playerXRouteCardSmall[x] = ImageTk.PhotoImage(image=i)
    return(playerXRouteCardSmall)


def cardList():
    card1="carriage_blue.png"
    card2="carriage_yellow.png"
    card3="carriage_red.png"
    card4="carriage_green.png"
    card5="carriage_orange.png"
    card6="carriage_pink.png"
    card7="train_card.png"
    cardList=[card1,card2,card3,card4,card5,card6,card7]
    if p1Turn==0:
        maxCards=5
    else:
        maxCards=2
    drawnList=[]
    x=0
    while (x<maxCards):
        drawnCard=random.choice(cardList)
        drawnList.append(drawnCard)
        x+=1
    addCards(drawnList)     
    #print(drawnList)
    return(drawnList)    

def addCards(drawnList):
    i=0
    while(i<len(drawnList)):
        if drawnList[i]=="carriage_blue.png":
            global blueNum1
            blueNum1+=1
        if drawnList[i]=="carriage_green.png":
            global greenNum1
            greenNum1+=1
        if drawnList[i]=="carriage_red.png":
            global redNum1
            redNum1+=1
        if drawnList[i]=="carriage_pink.png":
            global pinkNum1
            pinkNum1+=1
        if drawnList[i]=="carriage_orange.png":
            global orangeNum1
            orangeNum1+=1
        if drawnList[i]=="carriage_yellow.png":
            global yellowNum1
            yellowNum1+=1
        if drawnList[i]=="train_card.png":
            global locoNum1
            locoNum1+=1
        i+=1
    p1BlueNum.append(blueNum1)
    p1GreenNum.append(greenNum1)
    p1RedNum.append(redNum1)
    p1YellowNum.append(yellowNum1)
    p1OrangeNum.append(orangeNum1)
    p1PinkNum.append(pinkNum1)
    p1LocoNum.append(locoNum1)
    
    

def routesListInfo():
    global playerList
    numPlayers=len(playerList)
    global routesList
    routesList=[0]*numPlayers
    #print (playerList)
    return (routesList)        

def carriagesListInfo():
    global playerList
    numPlayers=len(playerList)
    global carriagesList
    carriagesList=[0]*numPlayers
    #print (playerList)
    return(carriagesList)

def carriagesRemInfo():
    global playerList
    numPlayers=len(playerList)
    global carriageRemList
    carriageRemList=[40]*numPlayers
    #print (playerList)
    return(carriageRemList)



def update(self):
    while True:
        global claimedSpacesX
        global claimedSpacesY
        global resizedMap    
        global carriagesList
        global routesList
        global carriageRemList
        global playerList
        #print (playerList)
        #print (routesList)
        start=0
        while (start==0):
        
            p1BlueNumText=self.canvas.create_text(screenWidth/11+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            
            p1YellowNumText=self.canvas.create_text(screenWidth/11*2+screenWidth/22+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            p1RedNumText=self.canvas.create_text(screenWidth/11*3+screenWidth/22*2+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            p1GreenNumText=self.canvas.create_text(screenWidth/11*4+screenWidth/22*3+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            p1OrangeNumText=self.canvas.create_text(screenWidth/11*5+screenWidth/22*4+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            p1PinkNumText=self.canvas.create_text(screenWidth/11*6+screenWidth/22*5+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            p1LocoNumText=self.canvas.create_text(screenWidth/11*7+screenWidth/22*6+10, screenHeight*0.91, fill="black", font="courier 25 bold",
                                text ="x ", width=1200, anchor="nw")
            start=1
        x=0
        y=screenHeight*0.647
        if not playerList:
            self.canvas.create_text(screenWidth*0.75,y, fill="white", font="courier 13 ", text =" ", width=1200, anchor="nw")
            routesScore=self.canvas.create_text(screenWidth*0.72,y, fill="white", font="courier 13 bold", text =" ", width=1200, anchor="nw")
            carriagesScore=self.canvas.create_text(screenWidth*0.84,y, fill="white", font="courier 13 bold", text =" ", width=1200, anchor="nw")
            carriageRemScore=self.canvas.create_text(screenWidth*0.91,y, fill="white", font="courier 13 bold", text =" ", width=1200, anchor="nw")
            y+=screenHeight*0.0243
            x+=1

        y=screenHeight*0.647
        x=0
        #if(x<len(playerList)):
            
         #   routesList=routesListInfo()
         #   carriagesList=carriagesListInfo()
         #   carriagesRemList=carriagesRemInfo()
         #   print (playerList)
         #   print (routesList)
         #   self.canvas.create_text(screenWidth*0.75,y, fill="white", font="courier 15 bold", text =str(routesList[x]), width=1200, anchor="nw")
         #   self.canvas.create_text(screenWidth*0.78,y, fill="white", font="courier 12 bold", text =str(playerList[x]), width=1200, anchor="nw")
         #   self.canvas.create_text(screenWidth*0.87,y, fill="white", font="courier 15 bold", text =str(carriagesList[x]), width=1200, anchor="nw")
         #   self.canvas.create_text(screenWidth*0.94,y, fill="white", font="courier 15 bold", text =str(carriagesRemList[x]), width=1200, anchor="nw")
         #   y+=screenHeight*0.0244
         #   x+=1
         #   if not root.isStopped:
         #       self.canvas.update()
        
        i=0
        while (cardClick>=0):
            self.canvas.after(500)
            self.canvas.itemcget(p1BlueNumText,'text')
            self.canvas.itemconfigure(p1BlueNumText, text= "x "+str(p1BlueNum[cardClick]))
            self.canvas.itemcget(p1RedNumText,'text')
            self.canvas.itemconfigure(p1RedNumText, text= "x "+str(p1RedNum[cardClick]))
            self.canvas.itemcget(p1GreenNumText,'text')
            self.canvas.itemconfigure(p1GreenNumText, text= "x "+str(p1GreenNum[cardClick]))
            self.canvas.itemcget(p1YellowNumText,'text')
            self.canvas.itemconfigure(p1YellowNumText, text= "x "+str(p1YellowNum[cardClick]))
            self.canvas.itemcget(p1OrangeNumText,'text')
            self.canvas.itemconfigure(p1OrangeNumText, text= "x "+str(p1OrangeNum[cardClick]))
            self.canvas.itemcget(p1PinkNumText,'text')
            self.canvas.itemconfigure(p1PinkNumText, text= "x "+str(p1PinkNum[cardClick]))
            self.canvas.itemcget(p1LocoNumText,'text')
            self.canvas.itemconfigure(p1LocoNumText, text= "x "+str(p1LocoNum[cardClick]))
            routesList=routesListInfo()
            carriagesList=carriagesListInfo()
            carriagesRemList=carriagesRemInfo()
            
            for z in range(len(playerList)):

                self.canvas.itemcget(routesScore,'text')
                self.canvas.itemconfigure(routesScore, text= str(routesList[z]))
                #self.canvas.create_text(screenWidth*0.72,y, fill="white", font="courier 13 bold", text =str(routesList[z]), width=1200, anchor="nw")
                self.canvas.create_text(screenWidth*0.75,y, fill="white", font="courier 13 bold", text =str(playerList[z]), width=1200, anchor="nw")
                self.canvas.itemcget(carriagesScore,'text')
                self.canvas.itemconfigure(carriagesScore, text= str(carriagesList[z]))
                #self.canvas.create_text(screenWidth*0.84,y, fill="white", font="courier 13 bold", text =str(carriagesList[z]), width=1200, anchor="nw")
                self.canvas.itemcget(carriageRemScore,'text')
                self.canvas.itemconfigure(carriageRemScore, text= str(carriageRemList[z]))
                #self.canvas.create_text(screenWidth*0.91,y, fill="white", font="courier 13 bold", text =str(carriagesRemList[z]), width=1200, anchor="nw")
                y+=screenHeight*0.0243
                #print(carriagesList[z])
                #print(carriageRemList[z])
            y=screenHeight*0.647
            for i in range(len(claimedSpacesX)):
                redTrak = Image.open('smallRedTrak.png')
                area = (claimedSpacesX[i], claimedSpacesY[i])
                resizedMap.paste(redTrak,area,redTrak)
                mapImage= ImageTk.PhotoImage(resizedMap)
                photoLabel=Label(image=mapImage)
                photoLabel.image=mapImage
                photoLabel.pack()
                self.canvas.create_image(0,0, image=mapImage,anchor = NW)
                i+=1
                
            
            x+=1
            
            self.canvas.update()

        self.canvas.update()



if __name__ == "__main__":
    root = tk.Tk()
    screenWidth=root.winfo_screenwidth()
    screenHeight=(root.winfo_screenheight())-80
    root.geometry("%sx%s" %(screenWidth,screenHeight))
    app = mainPlayingBoard(root)
    if not playerList:
            startWindow(root)
    
    if not root.isStopped:
        update(app)
    root.mainloop()
    



        



class drawRouteCards(object):
    def __init__(self,position):
        self.position = position








