from selenium import webdriver
from time import sleep
from base import Base,browser
driver=browser()
driver.get('D:\\接口\\练习\\选框.html')
zentao=Base(driver)
loc1=('id','c1')
r1=zentao.is_ElementExists(loc1)
print(r1)
loc_all=('xpath','.//*[@type="checkbox"]')
r2=zentao.is_ElementExists(loc_all)
print(r2)
driver.quit()