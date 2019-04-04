from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('selenium')
sleep(2)
driver.find_element_by_id('kw').submit()
sleep(2)
driver.quit()