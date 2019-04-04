from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from base import Base,browser
driver=browser()
driver.get("https://www.baidu.com/")
zentao=Base(driver)
loc_set=('link text','设置')
loc_souset=('link text','搜索设置')
mouse=zentao.find_element(loc_set)
ActionChains(driver).move_to_element(mouse).perform()
zentao.click(loc_souset)

loc1=('xpath','//*[@id="nr"]/option[1]')
loc2=('xpath','//*[@id="nr"]/option[3]')
r1=zentao.is_Selected(loc1)
print(r1)
r2=zentao.is_Selected(loc2)
print(r2)

loc3=('id','nr')
s=zentao.find_element(loc3)
sleep(2)
Select(s).select_by_index(2) #每页显示50条
r3=zentao.is_Selected(loc2)
print(r3)
