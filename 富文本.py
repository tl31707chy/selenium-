from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window()
sleep(2)
iframe=driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
sleep(1)
driver.find_element_by_name('email').send_keys('18782048160')
driver.find_element_by_name('password').send_keys('1995tanglei')
driver.find_element_by_xpath('//*[@id="dologin"]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="_mail_component_59_59"]/span[2]').click()
sleep(1)
#切换到富文本iframe
write=driver.find_element_by_class_name('APP-editor-iframe')
driver.switch_to.frame(write)
#定位富文本里body
driver.find_element_by_class_name('nui-scroll').send_keys('123456')
sleep(2)
driver.quit()