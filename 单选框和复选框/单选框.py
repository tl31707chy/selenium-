from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("D:\\接口\\1\\选框.html")
sleep(2)
# 没点击操作前，判断选项框状态
s = driver.find_element_by_id("boy").is_selected()
print(s)
driver.find_element_by_id("boy").click()
# 点击后，判断元素是否为选中状态
r = driver.find_element_by_id("boy").is_selected()
print(r)
sleep(2)
driver.quit()