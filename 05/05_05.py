import random
lst = [random.randint(1, 20) for _ in range(30)]
print("原始列表：", lst)
print("\n===== 去重结果 =====")
setlist = list(set(lst))
print("使用集合去重（顺序可能变化）：", setlist)
seen = set()
seelist = []
for num in lst:
    if num not in seen:
        seelist.append(num)
        seen.add(num)
print("保持顺序去重：", seelist)
print("\n===== 排序结果 =====")
sortf = sorted(seelist)
sortt = sorted(seelist, reverse=True)
print("升序：", sortf)
print("降序：", sortt)
print("\n===== 元素出现次数统计 =====")
countd = {}
for num in lst:
    countd[num] = countd.get(num, 0) + 1
for num, count in countd.items():    
    print(f"{num}: {count}次")
print("\n===== 出现次数最多的元素 =====")
max_count = max(countd.values())
most_frequent = [num for num, count in countd.items() if count == max_count]
for num in most_frequent:
    print(f"元素 {num} 出现 {max_count}次")