js = 'document.getElementsByClassName("el-select-dropdown__item")['+str(m)+'].click();'

js = 'document.getElementsByClassName("el-select-dropdown__item")['15'].click();' #15为clas的索引   括号里为class的值
self.driver.execute_script(js)
