# from re import I

# i = 0
# o = int(input("數字"))
# sum = 0
# while i <= o:
#     print(i)
#     sum += i
#     i += 1

#     print(sum)
# while True:
#     print("1蘋果汁")
#     print("2柳橙汁")
#     print("3葡萄汁")
#     print("4exit")
#     ans = input("請輸入果汁編號:")
#     if ans == "4":
#         break
#     elif ans == "1":
#         print("1蘋果汁")
#     elif ans == "2":
#         print("柳橙汁")
#     elif ans == "3":
#         print("3葡萄汁")
#     else:
#         print("查無此商品")
# import random

# print(random.randrange(3))
# print(random.randrange(0, 10, 2))
# random.randint(1, 3)
# random.randint(1, 10)
# import random

# i = random.randint(1, 100)
# while True:
#     ans = int(input("number:"))
#     if ans < i:
#         print("帶帶大一點")
#     elif ans > i:
#         print("帶帶小一點")
#     elif ans == i:
#         print("猜中了")
#         break
# from re import T
import turtle
import time

turtle.speed(0)
turtle.penup()
for s in range(60):
    for i in range(13):
        turtle.forward(50)
        turtle.stamp()
        turtle.home()
        turtle.right(30 * i)
    turtle.home()
    turtle.right(6 * s)
    turtle.pendown()
    turtle.forward(50)
    time.sleep(2)
    turtle.home
    turtle.right(6 * s)
    turtle.clear()
    turtle.penup
turtle.down
