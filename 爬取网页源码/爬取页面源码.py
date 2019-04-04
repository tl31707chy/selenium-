from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
#获取源码
Source=driver.page_source
print(Source)

driver.quit()