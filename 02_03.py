y=int(input("请输入年份："))
m=int(input("请输入月份："))
d=int(input("请输入日期："))
if(y>2100 or y<1900):
    print("错误：年份必须在1900-2100之间！")
    exit()
if(m<1 or m>12):
    print("错误：月份必须在1-12之间！")
    exit()
if (d<1):
    print("错误：日期必须为正整数！")
    exit()
if(m in [1,3,5,7,8,10,12]):
    if(d<1 or d>31):
        print("错误：%d月只有31天！"%(m))
        exit()
elif(m in [4,6,9,11]):
    if(d<1 or d>30):
        print("错误：%d月份只有30天！"%(m))
        exit()
else:
    if((y%4==0 and y%100!=0) or (y%400==0)):
        if(d<1 or d>29):
            print("错误：%d年2月只有29天！"%(y))
            exit()
    else:
        if(d<1 or d>28):
            print("错误：%d年2月只有28天！"%(y))
            exit()
print("日期合法!")
if((y%4==0 and y%100!=0) or (y%400==0)):
    y2=29
else:
    y2=28
if(m==1):
    sum=0
elif(m==2):
    sum=31
elif(m==3):
    sum=31+y2
elif(m==4):
    sum=31+y2+31
elif(m==5):
    sum=31+y2+31+30
elif(m==6):
    sum=31+y2+31+30+31
elif(m==7):
    sum=31+y2+31+30+31+30
elif(m==8):
    sum=31+y2+31+30+31+30+31
elif(m==9):
    sum=31+y2+31+30+31+30+31+31
elif(m==10):
    sum=31+y2+31+30+31+30+31+31+30
elif(m==11):
    sum=31+y2+31+30+31+30+31+31+30+31
else:
    sum=31+y2+31+30+31+30+31+31+30+31+30
sum+=d
print("这是%d年的第%d天"%(y,sum))