import csv
csv_file = csv.reader(open("E:\\测试\\6.csv","r"))
print(csv_file)
for line in csv_file:
    print(line)
#csv文件只能通过另存为的方式进行