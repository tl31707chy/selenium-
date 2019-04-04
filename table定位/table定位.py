# 1.table 页面查看源码一般有这几个明显的标签：table、tr、th、td
# 2.<table>标示一个表格
# 3.<tr>标示这个表格中间的一个行
# 4.</th> 定义表头单元格
# 5.</td> 定义单元格标签，一组<td>标签将将建立一个单元格，<td>标签必须
# 放在<tr>标签内
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("D:\\接口\\1\\table.html")
sleep(1)
a1=driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[3]/td[3]').text
print(a1)
sleep(1)
driver.quit()
