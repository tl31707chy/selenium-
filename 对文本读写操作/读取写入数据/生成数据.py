# w 只能操作写入  r 只能读取   a 向文件追加
# w+ 可读可写   r+可读可写    a+可读可追加
# wb+写入进制数据
# w模式打开文件，如果而文件中有数据，再次写入内容，会把原来的覆盖掉
i=1
myFile=open("E:\\测试\\data.txt",mode="w")
myFile.write("username,password\n")
while i<=5000:
    print(i)
    myFile.write("admin"+str(i)+",123456\n")
    i=i+1
