from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
mouse=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
sleep(1)
s=driver.find_element_by_id('nr')
Select(s).select_by_index(1) #每页显示20条
sleep(2)
Select(s).select_by_index(2) #每页显示50条
sleep(2)
Select(s).select_by_index(0) #每页显示10条
sleep(2)

# select_by_index() :通过索引定位
# select_by_value() :通过 value 值定位
# select_by_visible_text() :通过文本值定位
# deselect_all() ：取消所有选项
# deselect_by_index() ：取消对应 index 选项
# deselect_by_value() ：取消对应 value 选项
# deselect_by_visible_text() ：取消对应文本选项
# first_selected_option() ：返回第一个选项
# all_selected_options() ：返回所有的选项