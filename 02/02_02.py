h1=float(input("请输入身高（米）："))
h2=float(input("请输入体重（公斤）："))
if(h1<0.5 or h1>2.5):
    print("身高输入不合理（0.5-2.5米之间）！")
    exit()
if(h2<10 or h2>300):
    print("体重输入不合理（10-300公斤之间）！")
    exit()
bmi=h2/(h1**2)
print("您的BMI指数为：%.2f"%(bmi))
if bmi<18.5:
    print("评估结果：体重过轻")
elif bmi<24:
    print("评估结果：正常范围\n建议：保持当前生活方式")
elif bmi<28:
    print("评估结果：超重")  
else:
    print("评估结果：肥胖")