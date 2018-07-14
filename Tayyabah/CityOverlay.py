from tkinter import *
from HoverInfo import HoverInfo
class CityOverlay(Frame):
   def __init__(self, parent=None):
      Frame.__init__(self, parent)
      self.grid()
      self.lbl = Label(self, text='city name')
      self.lbl.grid()

      self.hover = HoverInfo(self, 'City info', self.hover)



app = CityOverlay()
app.master.title('test')
app.mainloop()
