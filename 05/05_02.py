n=int(input("请输入学生人数："))
students=[]
for i in range(n):
    name=input(f"请输入第{i+1}个学生姓名：")
    score=int(input(f"请输入第{i+1}个学生成绩："))
    students.append((name,score))
ssum=sum(score for _,score in students)
savge=ssum/n
smax=max(students,key=lambda x:x[1])
smin=min(students,key=lambda x:x[1])
print("\n===== 成绩统计结果 =====")
print(f"总分：{ssum}")
print(f"平均分：{savge:.2f}")
print(f"最高分：{smax[1]}（{smax[0]}）")
print(f"最低分：{smin[1]}（{smin[0]}）")
print("\n===== 成绩排名（从高到低）=====")
ssorted=sorted(students,key=lambda x:x[1],reverse=True)
i=1
sfrom=[0,0,0,0,0]
for (name,score) in ssorted:
    print(f"{i}. {name}: {score}分")
    i+=1
print("\n===== 分数段统计 =====")  
for (name,score) in students:
    if score>=90:
        sfrom[0]+=1
    elif score>=80:
        sfrom[1]+=1
    elif score>=70:
        sfrom[2]+=1
    elif score>=60:
        sfrom[3]+=1
    else:
        sfrom[4]+=1
print(f"90-100分: {sfrom[0]}人")
print(f"80-89分: {sfrom[1]}人") 
print(f"70-79分: {sfrom[2]}人")
print(f"60-69分: {sfrom[3]}人")
print(f"60分以下: {sfrom[4]}人")
scores=[score for _,score in students]
print(f"\n所有成绩：{scores}")