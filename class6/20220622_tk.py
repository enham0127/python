from tkinter import *
from tkinter.tix import ListNoteBook


def hahah():
    global sw
    print("hello")
    if sw:
        label.config(text='hi', fg='red')
    else:
        label.config(text='hi', fg='white')
    sw = not (sw)


sw = True
win = Tk()
win.title('hahahahha ')
btn = Button(win, text="click me", command=hahah)
btn.pack()
label = Label(win, text='', bg='#FFAD4E', fg='white')
label.pack()

win.mainloop()
