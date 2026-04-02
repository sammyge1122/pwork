print("===== 约瑟夫环问题 =====")
n = int(input("请输入总人数n："))
m = int(input("请输入报数间隔m："))
people = list(range(1, n + 1))
index = 0
i=1
while people:
    index = (index + m - 1) % len(people)
    last=people.pop(index)
    print(f"第{i}个出列的是：{last}号")
    i+=1
print(f"\n幸存者是：{last}号")
