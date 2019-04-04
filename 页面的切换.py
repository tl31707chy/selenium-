from time import sleep
from selenium import webdriver
from base import Base
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qq.com/")
QQ=Base(driver)
loc_news=('xpath','/html/body/div[1]/div[3]/div/ul/li[1]/a')
loc_video=('xpath','/html/body/div[1]/div[3]/div/ul/li[2]/a')
#QQ首页
home_page=driver.current_window_handle#获叏当前页面的句柄(首页)
all_1=driver.window_handles#获取所有页面
print(home_page)
print(all_1)
sleep(1)

#点击新闻
QQ.click(loc_news)
news=driver.current_window_handle#获叏当前页面的句柄（新闻）
all_2=driver.window_handles#获取所有页面
print(news)
print(all_2)

#切换到QQ首页
driver.switch_to.window(all_2[0])
QQ.click(loc_video)#点击视频
video=driver.current_window_handle#获叏当前页面的句柄（新闻）
all_3=driver.window_handles#获取所有页面
print(video)
print(all_3)

#切换到新闻
driver.switch_to.window(all_3[1])
sleep(2)

#切换到首页
driver.switch_to.window(all_3[0])
sleep(2)
#切换到视频
driver.switch_to.window(all_3[2])