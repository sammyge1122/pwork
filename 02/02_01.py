a=int(input("请输入秒数："))
if (a<0):
    print("时间不能为负数！")
    exit()
h=int(a)//3600
m=(int(a)%3600)//60
s=int(a)%60
print("转换结果：",h,"小时",m,"分钟",s,"秒")