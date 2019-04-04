from selenium import webdriver
from time import sleep#强制等待
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('selenium')
sleep(2)#强制等待2秒
driver.quit()