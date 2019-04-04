from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("G:\\资料\\Python\\selenium基本操作\\单选框和复选框\\选框.html")
sleep(1)
driver.find_element_by_id('c1').click()#勾选第一个
sleep(1)
driver.find_element_by_id('c1').click()#取消第一个
sleep(1)
all=driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in all:
    i.click()
sleep(2)
driver.quit()