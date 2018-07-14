import sys
from tkinter import *

app = Tk()
app.title("How to Play")
app.geometry("100x300+200+200")

ABOUT_TEXT = """HOW TO PLAY


Choose number of human players 1-6
Choose number of computer players (to make 2-6 players total)
Each player given 40 train tracks of their colour
Each player given 3 route cards
Each players can choose to discard 0, 1 route cards at the start. Must keep at least 2 to begin with.
Each player given 5 train cards.
Randomise who goes first.
On player turn, they choose only one of the following plays:

a.Pick up 2 more train cards
b. Pick up 3 more route cards (can then discard 0,1 or 2 of newly picked up cards,
must keep original route cards and at least one of new three picked up)
     c.	Claim a route (exchange at least 1 locomotive card and the correct
number of correct coloured carriage cards to place train carriages along the route of the matching colour)

(The claim a route here is different to the original to make our game a bit different.
So on our board, you would need a locomotive card and 7 yellow cards to claim Broome to Darwin.
You would need a Locomotive card and 1 red card to claim Perth to Bunbury (Augusta))

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
b = Button(app, text="Close Window", width=20, command=app.destroy)
b.pack(side='bottom',padx=0,pady=0)

def clickAbout():
    toplevel = Toplevel()
    label1 = Label(toplevel, text=ABOUT_TEXT,font=("courier", 13,), height=0, width=120)
    label1.pack()
    c = Button(toplevel, text="Close Window", width=20, command=app.destroy)
    c.pack(side='bottom',padx=0,pady=0)






button1 = Button(app, text="How to Play ", width=20, command=clickAbout)


button1.pack(side='bottom',padx=5,pady=5)

app.mainloop()
