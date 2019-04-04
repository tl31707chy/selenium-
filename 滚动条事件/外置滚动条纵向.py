from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('测试')
driver.find_element_by_id('su').click()
js1 = "window.scrollTo(0, document.body.scrollHeight)"#滑动滚动条到底部
js2 = "window.scrollTo(0,0)"#滑动到顶部
js3 = "window.scrollTo(0,200)"#向下移动200像素
js4 = "arguments[0].scrollIntoView();"#滑动滚动条到某个指定的元素"
sleep(2)
driver.execute_script(js1)
sleep(2)
driver.execute_script(js2)
sleep(2)
driver.execute_script(js3)
sleep(2)
a=driver.find_element_by_xpath('//*[@id="rs"]/div')
driver.execute_script(js4,a)
sleep(2)
driver.quit()
