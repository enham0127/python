from tkinter import *
from tkinter.tix import ListNoteBook


def goodfun():
    display.config(text=int(entry_data.get()))


win = Tk()
win.title('hahahahha')
sw = True
bty = Button(win, text="結果", command=goodfun)
bty.pack()
entry_data = Entry(win)
entry_data.pack()

display = Label(win, text="2.54", fg='#C900FF', bg="#C9FFE2")
display.pack()
sw = True
win.mainloop()
