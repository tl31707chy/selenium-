from time import sleep
from base import Base,browser
driver=browser()
driver.get("https://www.baidu.com/")
zentao=Base(driver)
loc1=('id','su')
r1=zentao.is_value_in_element(loc1,'百度一下')
print(r1)

r2=zentao.is_value_in_element(loc1,'百度一下sss')
print(r2)
driver.quit()