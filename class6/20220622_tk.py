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


def hello():
    print(type(entry_data.get()))
    label.config(text=entry_data.get(), fg="black")


sw = True
win = Tk()
win.title('hahahahha ')
btn = Button(win, text="click me", command=hahah)
btn.pack()
label = Label(win, text='', bg='#FFAD4E', fg='white')
label.pack()
entry_data = Entry(win)
entry_data.pack()

btn2 = Button(win, text='顯示輸入的文字', command=hello)
btn2.pack()
win.mainloop()
