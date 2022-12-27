import random
import math
secret=random.randint(0,99)
guess=0
tries = 0 # 尝试次数赋初值
#给定猜测次数 n
n=6
# 打招呼
print('嗨，你好！今天我们来玩一个猜数游戏。')
print('这个数字在 0－99 之间，我给你 6 次机会。')
#得到玩家猜的数，并判断大小，最多允许 n 次
while tries<n and guess!=secret:
    tries+=1 # 尝试次数加 1
    guess = int(input("请输入你猜的数："))
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print("恭喜你,答对了！猜了", tries, "次，")
#如果给出猜测的次数内没有猜对，则提示机会用完了，再来一次。
if tries == n and guess != n:
    print("机会用完了，再来一次！")