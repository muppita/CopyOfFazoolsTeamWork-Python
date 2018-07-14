from tkinter import *

master = Tk()
e=Entry(master)
e.pack()
e.focus_set()
def callback():
    print (e.get())
b = Button(master, text="Enter", width=30, command=callback,)
b.pack()

mainloop()
e = Entry(master, width=200)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
