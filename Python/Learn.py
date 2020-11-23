import urllib.request
import re
from bs4 import  BeautifulSoup

url = "https://movie.douban.com/"
headers ={
    "User-Agent":"ddddd"
}

req = urllib.request.Request(url = url,headers=headers)
response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# 正则表达式

m=re.findall(".*","CCCaaaaaAAAA")
print(m)
print(re.sub("a","Q","axsdawda"))