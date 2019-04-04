from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
mouse=driver.find_element_by_link_text('设置')
ActionChains(driver).context_click(mouse).perform()