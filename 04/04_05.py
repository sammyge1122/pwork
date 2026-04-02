import re
print("===== 日志文件分析器 =====")
f = open("access.log", "r", encoding="utf-8")
print("读取日志文件：access.log")
content = f.read()
f.close()
ip_count = {}
status_count = {}
url_count = {}
cout=0
for tiao in re.finditer(r'^(\d+\.\d+\.\d+\.\d+).*\[(.*?)\].*"(GET|POST|PUT|DELETE) (.*?) HTTP.*" (\d+)' , content, re.MULTILINE):
    cout+=1
    ip = tiao.group(1)
    time = tiao.group(2)
    method = tiao.group(3)
    url = tiao.group(4)
    status = tiao.group(5)
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1
    if status in status_count:
        status_count[status] += 1
    else:
        status_count[status] = 1
    if url in url_count:
        url_count[url] += 1
    else:
        url_count[url] = 1
ip_count = dict(sorted(ip_count.items(), key=lambda item: item[1], reverse=True))
status_count = dict(sorted(status_count.items(), key=lambda item: item[1], reverse=True))
url_count = dict(sorted(url_count.items(), key=lambda item: item[1], reverse=True))
print(f"共分析{cout}条日志记录")
print(f"IP访问统计（前5）：")
for ip, count in list(ip_count.items())[:5]:
    print(f"  {ip}: {count}")
print(f"状态码统计：")
for status, count in list(status_count.items()):
    print(f"  {status}: {count}")
print(f"热门请求路径（前5）：")
for url, count in list(url_count.items())[:5]:
    print(f"  {url}: {count}")

f = open("log_analysis.txt", "w", encoding="utf-8")
f.write(str(ip_count))
f.write(str(status_count))
f.write(str(url_count))
f.close()