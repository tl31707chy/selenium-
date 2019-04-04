from selenium import webdriver
from time import sleep
import re
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
Source=driver.page_source
# "非贪婪匹配,re.S('.'匹配字符,包括换行
url_list = re.findall('href=\"(.*?)\"', Source, re.S)#爬取url
url_all=[]#建立列表
for url in url_list:#遍历爬取到的url
    if 'http' in url:#判断是否以http开头
        print(url)
        url_all.append(url)#是添加到列表中
print(url_all)
