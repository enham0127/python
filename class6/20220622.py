def two(a):
    print(a)


def one(b):
    j = input("請輸入想加入的果汁:")
    if j in b:
        print("!!此商品已存在清單內!!")
    else:
        b.append(j)


def three(b):
    j = input("請輸入想刪除的果汁:")
    if j in b:
        b.remove(j)
    else:
        print("!!此商品不存在清單內!!")


juice = []
select = [one, two, three]
while True:
    print("1. 想加入菜單的果汁\n2. 顯示出目前所有果汁\n3. 刪除果汁\n4. 離開系統")
    ans = int(input("請輸入功能編號:"))
    if ans == len(select) + 1:
        break
    select[ans - 1](juice)
