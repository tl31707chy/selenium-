from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("D:\\接口\\1\\弹框.html")
driver.find_element_by_id('confirm').click()
sleep(2)
confirm=driver.switch_to_alert().text
print(confirm)
driver.switch_to_alert().accept()#接受
# driver.switch_to_alert().dismiss()#取消
sleep(2)
driver.quit()