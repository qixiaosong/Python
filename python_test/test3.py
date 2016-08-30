n = 7
g = -1
print("数字猜字游戏：")
while g != n:
    g = int(input("请输入你猜的数字："))
    if g == n:
        print("恭喜你，猜对了")
    elif g < n:
        print("猜小了")
    elif g > n:
        print("猜大了")
input("对了会enter退出")
