from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
#获取页面标题
title=driver.title
print(title)
# 获取元素的文本
text=driver.find_element_by_id('setf').text
print(text)
# 获取元素的标签
input=driver.find_element_by_id('kw').tag_name
print(input)
# 获取元素的其它属性
a=driver.find_element_by_id('kw').get_attribute('class')
print(a)
# 获取输入框内的文本值
driver.find_element_by_id('kw').send_keys('selenium')
b=driver.find_element_by_id('kw').get_attribute('value')
print(b)
#获取浏览器名称
c=driver.name
print(c)
sleep(2)
driver.quit()