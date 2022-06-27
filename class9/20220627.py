from tkinter import *


def two():
    global juice
    t = ""
    for i in juice:
        t += i + "\n"
    display4.config(text=t)


def one():
    global juice
    if entry.get() in juice:
        # print("!!此商品已存在清單內!!")
        display4.config(text="!!此商品已存在清單內!!")
    else:
        juice.append(entry.get())
        t = ""
        for i in juice:
            t += i + "\n"
        display4.config(text=t)


def three():
    global juice
    if entry.get() in juice:
        juice.remove(entry.get())
        t = ""
        for i in juice:
            t += i + "\n"
        display4.config(text=t)
    else:
        # print("!!此商品不存在清單內!!")
        display4.config(text="!!此商品不存在清單內!!")


juice = []
# select = [one, two, three]
# while True:
#     print("1. 想加入菜單的果汁\n2. 顯示出目前所有果汁\n3. 刪除果汁\n4. 離開系統")
#     ans = int(input("請輸入功能編號:"))
#     if ans == len(select) + 1:
#         break
#     select[ans - 1](juice)

win = Tk()
win.title('hi')
display1 = Button(win, text="輸入菜單", command=one)
display1.grid(row=0, column=0)
display2 = Button(win, text="顯示菜單", command=two)
display2.grid(row=1, column=0)
display3 = Button(win, text="移除", command=three)
display3.grid(row=2, column=0)
# btn = Button(win, text="結果", command=nofun)
# btn.grid(row=2, column=2)
display4 = Label(win, text="test")
display4.grid(row=0, rowspan=2, column=1)
entry = Entry(win)
entry.grid(row=2, column=1)
win.mainloop()