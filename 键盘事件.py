from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)#模拟回车键
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')#全选
sleep(1)
driver.find_element_by_id('kw').send_keys('appium')
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')#全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')#复制
sleep(1)
driver.find_element_by_id('kw').send_keys('python')
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')#全选
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE )#删除
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')#粘贴
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')#粘贴
sleep(2)
driver.quit()

# 其它常见的键盘操作：
# 键盘 F1 刡 F12：send_keys(Keys.F1) 把 F1 改成对应的快捷键
# 复刢 Ctrl+C：send_keys(Keys.CONTROL,'c')
# 粘贴 Ctrl+V：send_keys(Keys.CONTROL,'v')
# 全选 Ctrl+A：send_keys(Keys.CONTROL,'a')
# 剪凿 Ctrl+X：send_keys(Keys.CONTROL,'x')
# 刢表键 Tab: send_keys(Keys.TAB)