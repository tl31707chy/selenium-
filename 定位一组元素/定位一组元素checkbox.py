from selenium import webdriver
from time import sleep
import os# os 模块为 python 语言标准库中的 os 模块包含普遍的操作系统功能。主要用于操作本地目录文件。
driver=webdriver.Chrome()
driver.maximize_window()
# 打开本地网页
# path.abspath()方法用于获取当前路径下的文件。另外脚本中还使用到 for 循环，对 inputs 获取的一组元素
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
driver.implicitly_wait(5)
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')


#然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
# 进行循环，在 python 语言中循环变量（input）可以不用事先声明直接使用。
for input in inputs:
   if input.get_attribute('type') == 'checkbox':
      input.click()


# 打印当前页面上 type 为 checkbox 的个数
# len 为 python 语言中的方法，用于返回一个对象的长度（或个数）。
# 选择所有的 type 为 checkbox 的元素
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))

# pop 也为 python 语言中提供的方法，用于删除指定们位置的元素，pop()为空默认选择最一个元素。
# 把页面上最后1个 checkbox 的勾给去掉
driver.find_elements_by_css_selector('#c3').pop().click()
sleep(3)
# 把页面上第一个1个 checkbox 的勾给去掉
driver.find_elements_by_xpath('//*[@id="c1"]').pop().click()
sleep(2)
driver.quit()


