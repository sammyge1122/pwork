import requests
from bs4 import BeautifulSoup
import jieba
from collections import defaultdict

stop_words = {
    "的", "了", "在", "是", "我", "你", "他", "就",
    "都", "也", "不", "和", "有", "这", "那", "等",
    "吧", "吗", "呢", "啊", "哦", "一个", "我们", "你们"
}
print("===== 网页标题采集器 =====")
print("请输入网址（空行结束）：")
urls = []
while True:
    line = input().strip()
    if line == "":
        break
    urls.append(line)
print("\n正在采集...\n")
all_titles = []
print("结果：")
for url in urls:
    try:
        res = requests.get(url, timeout=5)
        
        res.encoding = res.apparent_encoding
        
        soup = BeautifulSoup(res.text, "html.parser")
        if soup.title:
            title = soup.title.string.strip()
        else:
            title = "无标题"
            
    except:
        title = "采集失败"

    print(f"{url} -> {title}")
    all_titles.append(title)
word_count = defaultdict(int)
for title in all_titles:

    words = jieba.cut(title)

    for word in words:
        word = word.strip()
        if len(word) > 1 and word not in stop_words and word != "":
            word_count[word] += 1
word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
print("\n标题词频统计：")
for word, count in word_count.items():
    print(f"{word}: {count}次")