from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#导入鼠标事件
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
mouse=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()