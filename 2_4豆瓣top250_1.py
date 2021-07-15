# 拿到网页源代码 requests
# re提取信息
import requests
import re
import csv
import itertools
from tqdm import tqdm

result1 = []
for i in tqdm(range(0, 250, 25)):
    url = f"https://movie.douban.com/top250?start={i}&filter="
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/91.0.4472.124 Safari/537.36"
    }
    resp = requests.get(url, headers=header)
    page_content = resp.text
    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?', re.S)
    result0 = obj.finditer(page_content)
    result = itertools.chain(result1, result0)
    result1 = result
    resp.close()

fp = open("data1.csv", mode="w", encoding="utf8", newline="")
csvwriter = csv.writer(fp)

for it in result:
    # print(it.group("name"), end=" ")
    # print(it.group("score"), end="分 ")
    # print(it.group("year").strip(), end=" ")
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

fp.close()
print("over!")
# resp.close()
