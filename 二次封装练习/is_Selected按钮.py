from selenium import webdriver
from time import sleep
from base import Base,browser
driver=browser()
driver.get('D:\\接口\\练习\\选框.html')
zentao=Base(driver)

loc1=('id','c1')
r1=zentao.is_Selected(loc1)
print(r1)
zentao.click(loc1)
r2=zentao.is_Selected(loc1)
print(r2)
sleep(1)

loc2=('id','girl')
r3=zentao.is_Selected(loc2)
print(r3)
zentao.click(loc2)
r4=zentao.is_Selected(loc2)
print(r4)
sleep(2)
driver.quit()