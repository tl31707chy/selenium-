from selenium import webdriver
from time import sleep
import os
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('file:///E:/Driver/%E5%AD%A6%E4%B9%A0/%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0/uplad.html')
driver.find_element_by_css_selector('body > div > div > input[type="file"]').click()
sleep(2)
relesefile=r'E:\Driver\学习\文件上传\input.exe'
os.system(relesefile)
sleep(5)
driver.quit()

