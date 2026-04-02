import re
print("===== 文本清洗与单词统计器 =====")
name=input("请输入文件名：")
f = open(name, "r", encoding="utf-8")
content = f.read()
f.close()
content = content.lower()
content = re.sub(r'[^\w\s]', '', content)
content = re.sub(r'[\d]', '', content)
words = content.split()
print(f"文件读取成功！共{len(words)}个单词。")
print()
print(f"总单词数：{len(words)}")
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"不同单词数：{len(word_count)}")
print()
word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
word_count = dict(list(word_count.items())[:20])
print("前20高频词：")
for word,count in word_count.items():
    print(f"{word}: {count}")