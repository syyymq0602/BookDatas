# -*- coding = utf-8 -*-
# @Time : 2020/11/24 17:38
# @Author :
# @File : PDF.py
# @Software : PyCharm

import camelot

# 从PDF文件中提取表格
tables = camelot.read_pdf('D://BrowserDownload//foo.pdf', pages='1', flavor='stream')

# 导出表格信息
tables.export("foo.csv", f='csv', compress=True)
