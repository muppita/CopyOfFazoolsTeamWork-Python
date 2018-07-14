entries = []
varEntry = StringVar()
entry = Entry(frame, textvariable=varEntry)
entry.pack()
entry.bind('Return',addToList)

def addToList():
    entries.append(varEntry)
