a=float(input("请输入系数a："))
b=float(input("请输入系数b："))
c=float(input("请输入系数c："))

if a==0:
    if b==0:
        print("方程无意义！")
    else:
        x=-c/b
        print("方程：%.1fx + %.1f = 0"%(b,c))
        print("一元一次方程，根：x=%.2f"%(x))
else:
    delta=b**2-4*a*c
    print("方程：%.1fx² + %.1fx + %.1f = 0"%(a,b,c))
    print("判别式：%.2f"%(delta))
    if delta<0:
        print("方程无实数解！")
    elif abs(delta)<1e-10:
        x=-b/(2*a)
        print("两个相等的实根：x=%.2f"%(x))
    elif delta>0:
        x1=(-b+delta**0.5)/(2*a)
        x2=(-b-delta**0.5)/(2*a)
        print("两个不相等的实根：x1=%.2f，x2=%.2f"%(x1,x2))