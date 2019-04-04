from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
mouse=driver.find_element_by_link_text('设置')#这里元素根据具体情况
ActionChains(driver).double_click(mouse).perform()