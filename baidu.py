import requests
import re
import csv

url = 'https://movie.douban.com/top250'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}
resp = requests.get(url, headers=header)
page_content = resp.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)

result = obj.finditer(page_content)
f = open('data.csv', mode='w')
csvwriter = csv.writer(f)

for it in result:
    #print(it.group("name"))
    dic = it.groupdict()
    csvwriter.writerow(dic.values()
                       
f.close()
print("over!")