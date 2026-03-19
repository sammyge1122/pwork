print("===== 学生成绩管理系统 =====\n1. 录入成绩\n2. 查看平均分\n3. 查看最高分和最低分\n4. 显示所有成绩\n5. 退出")
cj=[]
while 1:
    try:
        gn=int(input("请选择（1-5）："))
    except ValueError:
        print("输入有误，请重新输入！")
        continue
    match gn:
        case 1:
            while 1:
                try:
                    score=int(input("请输入成绩（0-100，输入-1结束）："))
                except ValueError:
                    print("输入有误，请重新输入！")
                    continue
                if score==-1:
                    print("返回主菜单")
                    break
                if 0<=score<=100:
                    cj.append(score)
                    print(f"已录入：{score}")
                else:
                    print("输入有误，请重新输入！")
        case 2:
            if len(cj)==0:
                print("暂无成绩")
            else:
                print(f"平均分：{sum(cj)/len(cj):.2f}")
        case 3:
            if len(cj)==0:
                print("暂无成绩")
            else:
                print(f"最高分：{max(cj)}，最低分：{min(cj)}")
        case 4:
            if len(cj)==0:
                print("暂无成绩")
            else:
                print("当前成绩：", end="")
                print(cj)
        case 5:
            print("感谢使用，再见！")
            break