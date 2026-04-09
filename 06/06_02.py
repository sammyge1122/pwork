students = {
    "1001": {"name": "张三", "age": 20, "score": 85},
    "1002": {"name": "李四", "age": 21, "score": 92},
    "1003": {"name": "王五", "age": 19, "score": 78}
}
def zhujiemian():
    print("===== 学生信息管理系统 =====")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 查找学生")
    print("4. 修改学生成绩")
    print("5. 显示所有学生")
    print("6. 统计信息")
    print("7. 退出")
zhujiemian()
while True:
    
    xz = input("请选择：")
    if xz == "1":
        xuehao = input("请输入学号：")
        if xuehao in students:
            print("学号已存在！")
            continue
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        students[xuehao] = {"name": name, "age": age, "score": score}
        print("添加成功！")
    elif xz == "2":
        xuehao = input("请输入学号：")
        if xuehao in students:
            del students[xuehao]
            print("删除成功！")
        else:
            print("学号不存在！")
    elif xz == "3":
        xuehao = input("请输入学号：")
        if xuehao in students:
            info = students[xuehao]
            print(f"学号: {xuehao}, 姓名: {info['name']}, 年龄: {info['age']}, 成绩: {info['score']}")
        else:
            print("学号不存在！")
    elif xz == "4":
        xuehao = input("请输入学号：")
        if xuehao in students:
            new_score = int(input("请输入新成绩："))
            students[xuehao]["score"] = new_score
            print("成绩修改成功！")
        else:
            print("学号不存在！")
    elif xz == "5":
        print("\n学号     姓名     年龄     成绩")
        print("----------------------------------------")
        for xuehao, info in sorted(students.items()):
            print(f"{xuehao}     {info['name']}     {info['age']}       {info['score']}")
    elif xz == "6":
        studentsnumber = len(students)
        if studentsnumber == 0:
            print("没有学生信息！")
            continue
        total_score = sum(info["score"] for info in students.values())
        pjf = total_score / studentsnumber
        maxi = max(students.items(), key=lambda x: x[1]["score"])
        mini = min(students.items(), key=lambda x: x[1]["score"])
        print("\n===== 统计信息 =====")
        print(f"学生人数：{studentsnumber}人")
        print(f"平均分：{pjf:.2f}")
        print(f"最高分：{maxi[1]['score']}（{maxi[1]['name']}）")
        print(f"最低分：{mini[1]['score']}（{mini[1]['name']}）")
    elif xz == "7":
        print("退出程序！")
        break
    else:        print("无效选择，请重新输入！")    