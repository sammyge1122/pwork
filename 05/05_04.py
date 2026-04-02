import random
n=int(input("请输入学生人数："))
students={}
for i in range(n):
    name=input(f"请输入第{i+1}个学生姓名：")
    age=int(input(f"请输入第{i+1}个学生年龄："))
    city=input(f"请输入第{i+1}个学生城市：")
    score=random.randint(60,100)
    students[(name,age,city)]=score
print("\n===== 学生信息字典 =====")
for key,value in students.items():
    print(f"{key}: {value}分")
print("\n===== 按姓名查找 =====")
findname=input("请输入学生姓名：")
found=False
for key,value in students.items():
    if key[0]==findname:
        print(f"找到：姓名：{key[0]}，年龄：{key[1]}，城市：{key[2]}，成绩：{value}分")
        found=True
        break
if not found:
    print("未找到该学生信息。")
print("\n===== 城市人数统计 =====")
citycount={}
for key in students.keys():
    city=key[2]
    citycount[city]=citycount.get(city,0)+1
for city,count in citycount.items():
    print(f"{city}: {count}人")
print("\n===== 年龄最大的学生 =====")
max_age=-1
old=None
for key,value in students.items():
    if key[1]>max_age:
        max_age=key[1]
        old=(key,value)
print(f"姓名：{old[0][0]}，年龄：{old[0][1]}，城市：{old[0][2]}，成绩：{old[1]}分")
print("\n===== 演示：元组作为字典键 =====")
print("元组可以作为字典键，因为它是不可变的。")
print("尝试用列表作为键会报错：TypeError: unhashable type: 'list'")
# students[[name,age,city]]=score  # 这行代码会报错，因为列表是可变的，不能作为字典的键
