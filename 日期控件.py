from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.12306.cn/index/")
sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/i').click()
js='document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
driver.find_element_by_xpath('//*[@id="train_date"]').send_keys('2019-04-09')
