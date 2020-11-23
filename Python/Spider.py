# -*- coddeing = utf-8 -*-
# @Time : 2020/11/22 20:08
# @Author :
# @File : Spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析 获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excle操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?Start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影top250.xls"
    saveData(datalist,savepath)


# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 匹配换行符
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*?)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []  # 保存一部电影的所有信息
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                etitle = titles[1].replace("/", "")
                data.append(etitle)
            else:
                data.append(titles[0])
                data.append(' ')

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())  # 去掉前后空格

            datalist.append(data)

    print(datalist)
    # 2.解析数据
    return datalist


# 得到指定一个url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36 (KHTML, likeGecko) Chrome / 87.0.4280.66 Safari /537.36 Edg / 87.0.664.41"
    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 3.保存数据
def saveData(datalist,savepath):
    print("saving.....")
    book = xlwt.Workbook(encoding="utf-8", style_compression = 0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok = True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评分数", "概况", "相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


if __name__ == "__main__":
    main()
