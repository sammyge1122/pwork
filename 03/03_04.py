def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b // GCD(a, b)


try:
    a=int (input("请输入第一个正整数："))
except ValueError:
    print("请输入正整数！")
    exit()
if a <= 0:
    print("请输入正整数！")
    exit()

try:
    b=int (input("请输入第二个正整数："))
except ValueError:
    print("请输入正整数！")
    exit()
if b <= 0:
    print("请输入正整数！")
    exit()

print(f"{a}和{b}的最大公约数是：{GCD(a, b)}")
print(f"{a}和{b}的最小公倍数是：{LCM(a, b)}")