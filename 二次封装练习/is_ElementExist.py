from selenium import webdriver
from time import sleep
from base import Base,browser
driver=browser()
driver.get('D:\\接口\\练习\\选框.html')
zentao=Base(driver)
loc1=('id','c1')
r1=zentao.is_ElementExist(loc1)
sleep(2)
driver.quit()