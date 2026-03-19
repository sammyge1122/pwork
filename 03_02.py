import random
y = random.randint(1, 100)
print("(我已经想好了一个1-100之间的数字)")
n=0
while 1:
    try:
        x = int(input("请输入你的猜测："))
    except ValueError:
        print("输入有误，请重新输入！")
        continue
    if x < 1 or x > 100:
        print("输入有误，请重新输入！")
        continue
    n+=1
    if x < y:
        print("猜小了!")
    elif x > y:
        print("猜大了!")
    else:
        print(f"恭喜猜中！\n你一共猜了{n}次")
        break
