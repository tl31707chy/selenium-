import csv
# w 只能操作写入  r 只能读取   a 向文件追加
# w+ 可读可写   r+可读可写    a+可读可追加
# wb+写入进制数据
# w模式打开文件，如果而文件中有数据，再次写入内容，会把原来的覆盖掉
Rall=open("E:\\测试\\2.csv",mode="r")#创建文本或者打开文本
data1=Rall.read()#括号里填写字符长度   读取文本全部内容
print(data1)
Rall.close()

# Rfirst=open("E:\\测试\\1.txt",mode="r")
# data2=Rfirst.readline()#读取第一行数据
# print(data2)
# Rfirst.close()
#
# Relement=open("E:\\测试\\1.txt",mode="r")
# data3=Relement.readlines()#会把每一行的数据作为一个元素放在列表中返回，读取所有行的数据
# print(data3)
