from selenium import webdriver
from time import sleep
from base import Base,browser
driver=browser()
driver.get('http://127.0.0.1:81/zentao/user-login.html')
zentao=Base(driver)
loc_submit=('id','submit')
r1=zentao.is_alert()
print(r1)
zentao.click(loc_submit)
r2=zentao.is_alert()
print(r2)
print(r2.text)
r2.accept()
sleep(2)
driver.quit()