from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('测试')
driver.find_element_by_id('su').click()
driver.maximize_window()
driver.set_window_size(500,500)
js1 = "window.scrollTo(document.body.scrollWidth,0)"#滑动滚动条到最右端
js2 = "window.scrollTo(0,0)"#滑动到最左端
js3 = "window.scrollTo(200,0)"#向右移动200像素
sleep(2)
driver.execute_script(js1)
sleep(2)
driver.execute_script(js2)
sleep(2)
driver.execute_script(js3)
sleep(2)
driver.quit()


