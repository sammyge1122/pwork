s=input("请输入一个字符串：")
s=s.lower()
freq={}
for ch in s:
    if ch!=' ':
        freq[ch]=freq.get(ch,0)+1
sorted_freq=sorted(freq.items(),key=lambda x:(-x[1],x[0]))
print("\n字符频率统计结果：")
for ch,count in sorted_freq:
    print(f"{ch}: {count}次")