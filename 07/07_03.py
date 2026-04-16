def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"将盘{n}从{source}移动到{target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"将盘{n}从{source}移动到{target}")
    hanoi(n - 1, auxiliary, target, source)

def hanoi_steps(n):
    return 2 ** n - 1

n=int(input("请输入圆盘数量（1-8）："))
print("\n===== 汉诺塔移动步骤 =====")
hanoi(n, 'A', 'C', 'B')
steps = hanoi_steps(n)
print(f"\n总移动步数：{steps}")
print(f"验证：2^{n} - 1 = {steps},正确！")