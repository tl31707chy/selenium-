from selenium import webdriver
from time import sleep
from base import Base,browser
driver=browser()
driver.get('http://127.0.0.1:81/zentao/user-login.html')
zentao=Base(driver)
loc1=('xpath','//*[@id="login-form"]/form/table/tbody/tr[4]/td/a')
r1=zentao.is_text_in_element(loc1,'忘记密码')
print(r1)
r2=zentao.is_text_in_element(loc1,'3333')
print(r2)
driver.quit()