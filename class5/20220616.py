# from readline import append_history_file

# juice = ["apple juice", 'ornnge juice', 'grapes juice']
# while True:
#     print("1.", juice[0])
#     print("2.", juice[1])
#     print("3.", juice[2])
#     print("4. exit")
#     ans = int(input("which do you want?:"))
#     if ans == 4:
#         break
#     elif ans >= len(juice):
#         print("nothing")
#     else:
#         print(juice[ans - 1])
# append 新增元素到list的最後
# insert指定的元素插入指定的位置
# pop移除指定牽引的元素
# sort由小到大排序串列元素
# reverse顛倒串列的排序
# index找到串列中對應元素值得位置索引
menu = []
while True:
    x = (input("what do you want to add to the menu?:"))
    menu.append(x)
    print(menu)
