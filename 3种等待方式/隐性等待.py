from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('selenium')
driver.implicitly_wait(2)#隐性等待
driver.find_element_by_id('su').click()
driver.implicitly_wait(2)
driver.quit()

# driver.implicitly_wait()，隐性等待设置了一个时间，在一段时间内网页是否加载完成，
# 如果完成了，就进行下一步；在设置的时间内没有加载完成，则会报超时加载
# 缺点也是不智能，因为随着ajax技术的广泛应用，页面的元素往往都可以时间局部加载，
# 也就是在整个页面没有加载完的时候，可能我们需要的元素已经加载完成了，
# 那就么有必要再等待整个页面的加载，执行进行下一步，而隐性等待满足不了这一点；