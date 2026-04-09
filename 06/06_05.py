users = {
    "user1": {"password": "pass123", "locked": False, "ec": 0},
    "user2": {"password": "abc456", "locked": False, "ec": 0},
    "user3": {"password": "xyz789", "locked": False, "ec": 0}
}

def zhujiemian():
    print("===== 用户登录验证系统 =====")
    print("1. 注册")
    print("2. 登录")
    print("3. 修改密码")
    print("4. 显示所有用户")
    print("5. 退出")
zhujiemian()
while True:
    
    xz = input("请选择：")
    if xz == "1":
        print("\n注册新用户：")
        username = input("用户名：")
        if username in users:
            print("用户名已存在！")
            continue
        password = input("密码：")
        if len(password) < 6:
            print("密码长度至少6位！")
            continue
        users[username] = {"password": password, "locked": False, "ec": 0}
        print("注册成功！")
    elif xz == "2":
        print("\n登录：")
        username = input("用户名：")
        if username not in users:
            print("用户名不存在！")
            continue
        if users[username]["locked"]:
            print("账户已锁定！请联系管理员。")
            continue
        password = input("密码：")
        if password == users[username]["password"]:
            print(f"登录成功！欢迎回来，{username}")
            users[username]["ec"] = 0  # 重置失败计数器
        else:
            print("密码错误！")
            users[username]["ec"] += 1
            if users[username]["ec"] >= 3:
                users[username]["locked"] = True
                print("账户已锁定！连续3次登录失败。")
    elif xz == "3":
        print("\n修改密码：")
        username = input("用户名：")
        if username not in users:
            print("用户名不存在！")
            continue
        old_password = input("原密码：")
        if old_password != users[username]["password"]:
            print("原密码错误！")
            continue
        new_password = input("新密码：")
        if len(new_password) < 6:
            print("新密码长度至少6位！")
            continue
        users[username]["password"] = new_password
        print("密码修改成功！")
    elif xz == "4":
        print("\n所有用户列表（不显示密码）：")
        for user in users:
            print(user)
    elif xz == "5":
        print("退出系统。再见！")
        break
    else:
        print("无效选择，请重新输入。")