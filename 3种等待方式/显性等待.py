from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait#显性等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *  #导入所有异常类
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
WebDriverWait(driver, 0.5, 0.5).until(EC.presence_of_element_located((By.NAME,'wd'))).send_keys('selenium')
driver.quit()

# 1.这里主要有三个参数：
# class WebDriverWait(object):driver, timeout, poll_frequency
# 2.driver:返回浏览器的一个实例，这个不用多说
# 3.timeout：超时的总时长
# 4.poll_frequency：循环去查询的间隙时间，默认 0.5 秒


# selenium中的wait模块的WebDriverWait()方法，配合until或者until_not方法，再辅助以一些判断条件，就可以构成这样一个场景：
# 每经过多少秒就查看一次locator的元素是否可见，如果可见就停止等待，如果不可见就继续等待直到超过规定的时间后，报超时异常；
# 当然也可以判断某元素是否在规定时间内不可见等等的各种场景吧，需要根据你自己实际的场景选择判断条件；

