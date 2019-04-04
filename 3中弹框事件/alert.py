from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("D:\\接口\\1\\弹框.html")
driver.find_element_by_id('alert').click()
sleep(2)
alert=driver.switch_to_alert().text
print(alert)
driver.switch_to_alert().accept()
sleep(2)
driver.quit()