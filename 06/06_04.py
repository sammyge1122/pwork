import re
from collections import Counter
print("请输入英文文本（输入空行结束）：")
wb = []
while True:
    wbh = input()
    if wbh == "":
        break
    wb.append(wbh)
text = "\n".join(wb)
words = re.sub(r'[^\w\s]', '', text).lower().split()
lword = len(words)
sword = len(set(words))
wordc = Counter(words)
wordc10 = wordc.most_common(10)

print("\n===== 单词频率统计 =====")
print(f"总单词数：{lword}")
print(f"不同单词数：{sword}\n")
print("前10高频词：")
for word, count in wordc10:
    print(f"{word}: {count}次")