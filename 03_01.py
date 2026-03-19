def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

def factorial(n):
    for i in range(1,n):
        n*=i
    return n

while 1:
    print("请选择功能：\n1. 计算1到n的累加和\n2. 计算n的阶乘\n3. 退出")
    try:
        gn=int(input("请输入选择（1-3）："))
    except ValueError:
        print("输入有误，请重新输入！")
        continue
    match gn:
        case 1:
            while 1:
                try:
                    n=int(input("请输入n："))
                except ValueError:
                    print("输入有误，请重新输入！")
                    continue
                if n>0:
                    break
                else:
                    print("输入有误，请重新输入！")
            print(f"1到{n}的累加和 ={sum(n)}")
        case 2:
            while 1:
                try:
                    n=int(input("请输入n："))
                except ValueError:
                    print("输入有误，请重新输入！")
                    continue
                if n>0:
                    break
                else:
                    print("输入有误，请重新输入！")
            print(f"{n}的阶乘 ={factorial(n)}")
        case 3:
            print("程序结束")
            break
        case _:
            print("输入有误，请重新输入！")