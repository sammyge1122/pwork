print("水仙花数：")
for i in range(100,1000):
    a=i//100
    b=(i%100)//10
    c=i%10
    if i==a**3+b**3+c**3:
        print(f"{i}是水仙花数")

print()

print("完全数：")
for i in range(1,10001):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(f"{i}是完全数,它的因子是：",end="")
        for j in range(1,i):
            if i%j==0:
                print(j,end="+")
        print(f"\b={i}")