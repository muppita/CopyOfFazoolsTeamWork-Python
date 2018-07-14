import math
import random
import numpy as np #you guys will have to download this
import cv2 #you guys will have to download this
import os
path=os.getcwd()
print(path)
def createRandomRoute():
    #print(path)
    destinationList=["Weipa","Cooktown","Mackay","Bundaberg","Brisbane","Sydney","MtIsa","Bourke","Broken Hill","Canberra","Melbourne","Hobart","Portland","Adelaide","Ceduna","Coober Pedy","Alice Springs","Karumba","Burketown","Nhulunbuy","Darwin","Halls Creek","Newman","Kalgoorlie","Esperance","Albany","Bunbury","Perth","Carnarvon","Mt Magnet","Karratha","Broom"]
    town1=random.randint(0,31)
    town2=random.randint(0,31)
    while town2==town1:
        town2=random.randint(0,31)
    town1Name=destinationList[town1]
    town2Name=destinationList[town2]
    #print (town1Name,town2Name)
    card=cv2.imread(path+"/Terra_Australis_Small.png")
    #routeCard=cv2.namedWindow("routeCard",cv2.WINDOW_NORMAL)
    #cv2.waitKey(0)
    h=len(card)
    w=len(card[0])
    #print(h,w)
    x1List=[135,143,149,166,170,166,140,146,135,153,137,143,126,118,91,109,100,127,119,109,93,73,44,54,66,48,37,35,26,39,35,57]
    y1List=[18,32,46,68,78,103,66,89,102,112,125,146,123,104,98,90,66,45,44,24,22,52,71,90,104,112,109,100,83,89,60,48]
    x2List=[135,143,149,166,170,166,140,146,135,153,137,143,126,118,91,109,100,127,119,109,93,73,44,54,66,48,37,35,26,39,35,57]
    y2List=[18,32,46,68,78,103,66,89,102,112,125,146,123,104,98,90,66,45,44,24,22,52,71,90,104,112,109,100,83,89,60,48]

    #print(len(x1List))
    #print(len(y1List))
    #print(len(destinationList))
    pixel=card[x1List[town1],y1List[town1]]
    #print(pixel)
    x1=x1List[town1]
    y1=y1List[town1]
    x2=x2List[town2]
    y2=y2List[town2]
    card[y1-3:y1+3,x1-3:x1+3]=(0,0,0)
    card[y2-3:y2+3,x2-3:x2+3]=(0,0,0)
    
    
    #cv2.imwrite("C:/Users/Emily/Desktop/BITS/Route cards/routeCard.png",card)
    #card2=cv2.imread("C:/Users/Emily/Desktop/BITS/Route cards/routeCard.png")
    #cv2.imshow("routeCard",card2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #points value
    xValue=abs(x1-x2)
    yValue=abs(y1-y2)
    points=math.ceil((math.sqrt(xValue**2+yValue**2))/7)
    #print(points)            
    text1=destinationList[town1]
    text2="to "+destinationList[town2]
    text3=str(points)
    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    startText1=(13,25)
    startText2=(13,135)
    startText3=(163,27)
    fontScale=0.5
    fontColor=(20,20,20)
    thickness=1
    lineType=4
    cv2.putText(card,text1,startText1,font,fontScale,fontColor,thickness,lineType)
    cv2.putText(card,text2,startText2,font,fontScale,fontColor,thickness,lineType)
    cv2.putText(card,text3,startText3,font,fontScale,fontColor,thickness,lineType)
    cv2.circle(card,(175,22),13,(20,20,20),1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return card
       


createRandomRoute()
       
