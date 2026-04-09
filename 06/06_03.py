inputa = input("请输入第一个集合的元素（空格分隔）：")
inputb = input("请输入第二个集合的元素（空格分隔）：") 
set_a = set(map(int, inputa.split()))
set_b = set(map(int, inputb.split()))
print("\n===== 集合运算结果 =====")
print(f"集合 A: {set_a}")
print(f"集合 B: {set_b}\n")
bing = set_a | set_b
jiao = set_a & set_b
achab = set_a - set_b
bchaa = set_b - set_a
duichengcha = set_a ^ set_b
print(f"并集 A ∪ B: {bing}")
print(f"交集 A ∩ B: {jiao}")
print(f"差集 A - B: {achab}")
print(f"差集 B - A: {bchaa}")
print(f"对称差 A ⊕ B: {duichengcha}\n")
print("集合关系判断：")
print(f"A == B: {set_a == set_b}")
print(f"A ⊆ B: {set_a.issubset(set_b)}")
print(f"B ⊆ A: {set_b.issubset(set_a)}")
