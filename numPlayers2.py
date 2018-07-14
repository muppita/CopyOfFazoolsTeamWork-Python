from tkinter import *
import sys

playerList=[]
compList=[]
    
class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Human Player Name")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        
     
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
    
class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="Add Human Player",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="Add Computer Player",command=self.addComputer)
        self.b2.pack()
        self.b3=Button(master,text="Start",command=self.entryValue)
        self.b3.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"
        playerList.append(self.w.value)
        return playerList

    def addComputer(self):
        compList.append("Computer")
        compNum=len(compList)
        compPlayer="Computer "+str(compNum)
        playerList.append(compPlayer)
     
    def entryValue(self):
        print (playerList)
        


if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
    
#player=entryValue(self)
#print (player)
