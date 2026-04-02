ye=5000
jr=2000
print("===== 欢迎使用简易ATM =====")
print("当前余额：",ye,"元")
qk=int(input("请输入取款金额："))
if qk%100!=0:
    print("取款失败：取款金额必须是100的倍数！")
    exit()
if qk>ye:
    print("取款失败：余额不足！")
    exit()
if qk>jr:
    print("取款失败：单日取款限额为2000元！")
    exit()
if qk<=0:
    print("取款失败：取款金额必须为正数！")
    exit()
ye-=qk
jr-=qk
print("取款成功！\n取款金额：",qk,"\n剩余余额：",ye,"元\n今日剩余额度：",jr,"元")