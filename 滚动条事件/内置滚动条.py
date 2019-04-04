from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('file:///E:/Driver/%E5%AD%A6%E4%B9%A0WEB/%E6%BB%9A%E5%8A%A8%E6%9D%A1%E4%BA%8B%E4%BB%B6/%E5%86%85%E7%BD%AE%E6%BB%9A%E5%8A%A8%E6%9D%A1%E9%A1%B5%E9%9D%A2.html')
js1='document.getElementsByClassName("scroll")[0].scrollTop=10000'
js2='document.getElementsByClassName("scroll")[0].scrollTop=0'
js3='document.getElementsByClassName("scroll")[0].scrollLeft=10000'
js4='document.getElementsByClassName("scroll")[0].scrollLeft=0'
# 就是这么简单，修改这个元素的scrollTop就可以
# document.getElementsByClassName("scroll")[0].scrollHeight // 获取滚动条高度
# document.getElementsByClassName("scroll")[0].scrollWidth // 获取横向滚动条宽度
# document.getElementsByClassName("scroll")[0].scrollLeft=xxx // 控制横向滚动条位置
# document.getElementsByClassName("scroll")[0].scrollTop=xxx//控制纵向滚动条位置
sleep(2)
driver.execute_script(js1)#向下
sleep(2)
driver.execute_script(js2)#向上
sleep(2)
driver.execute_script(js3)#向右
sleep(2)
driver.execute_script(js4)#向左
sleep(2)
driver.quit()
