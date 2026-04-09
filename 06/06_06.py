friends = {
    "张三": {"李四", "王五", "赵六"},
    "李四": {"张三", "王五", "小明"},
    "王五": {"张三", "李四", "小红"},
    "赵六": {"张三", "小红", "小明"},
    "小明": {"李四", "赵六"},
    "小红": {"王五", "赵六"}
}

def zhujiemian():
    print("===== 共同好友推荐系统 =====")
    print("1. 显示好友列表")
    print("2. 显示共同好友")
    print("3. 推荐好友")
    print("4. 找出共同好友最多的一对")
    print("5. 退出")
zhujiemian()
while True:
    
    xz = input("请选择：")
    if xz == "1":
        username = input("请输入用户名：")
        if username in friends:
            print(f"{username}的好友：{friends[username]}")
        else:
            print("用户不存在！")
    elif xz == "2":
        user1 = input("请输入第一个用户名：")
        user2 = input("请输入第二个用户名：")
        if user1 in friends and user2 in friends:
            gthy = friends[user1] & friends[user2]
            print(f"{user1}和{user2}的共同好友：{gthy}")
        else:
            print("用户不存在！")
    elif xz == "3":
        username = input("请输入用户名：")
        if username in friends:
            gthytj = {}
            for user, user_friends in friends.items():
                if user != username and user not in friends[username]:
                    c = len(friends[username] & user_friends)
                    if c > 0:
                        gthytj[user] = c
            if gthytj:
                sgthytj = sorted(gthytj.items(), key=lambda x: -x[1])
                print(f"推荐给{username}的好友：")
                for rec_user, count in sgthytj:
                    print(f"{rec_user}（共同好友数：{count}）")
            else:
                print("没有推荐的好友！")
        else:
            print("用户不存在！")
    elif xz == "4":
        max = 0
        maxp = None
        users = list(friends.keys())
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                c = len(friends[users[i]] & friends[users[j]])
                if c > max:
                    max = c
                    maxp = (users[i], users[j])
        if maxp:
            print(f"共同好友最多的一对用户：{maxp[0]}和{maxp[1]}，共同好友数：{max}")
        else:
            print("没有用户对！")
    elif xz == "5":
        print("退出系统。")
        break
    else:
        print("无效选择，请重新输入！")
