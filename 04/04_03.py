name=input("请输入姓名：")
name=" ".join(name.strip().split()).title()
print(f"处理后的姓名：{name}")
xz=input("是否检查前缀？(y/n)：")
if xz=="y":
    qz=input("请输入要检查的前缀：")
    if name.startswith(qz):
        print(f"结果：True（以{qz}开头）")
    else:
        print(f"结果：False（不以{qz}开头）")
xz=input("是否检查后缀？(y/n)：")
if xz=="y":
    hz=input("请输入要检查的后缀：")
    if name.endswith(hz):
        print(f"结果：True（以{hz}结尾）")
    else:
        print(f"结果：False（不以{hz}结尾）")
xz=input("是否替换字符？(y/n)：")
if xz=="y":
    old=input("请输入要替换的字符：")
    new=input("请输入替换后的字符：")
    name=name.replace(old,new)
    print(f"替换结果：{name}")
xz=input("请选择称呼（1-先生，2-女士）：")
if xz=="1":
    name="尊敬的"+name+"先生"
elif xz=="2":
    name="尊敬的"+name+"女士"
print(f"完整问候：{name}")