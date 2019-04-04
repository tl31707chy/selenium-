from selenium import webdriver
from time import sleep
from base import Base,browser
driver=browser()
driver.get('http://127.0.0.1:81/zentao/user-login.html')
zentao=Base(driver)
t1=zentao.is_title('用户登录 - 禅道')
print(t1)
t2=zentao.is_title_contains('禅道')
print(t2)
t3=zentao.is_title_contains('你')
print(t3)
driver.quit()