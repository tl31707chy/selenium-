import pymysql
connection=pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="k1",charset='utf8')

# 使用游标操作
cursor=connection.cursor()

# execute执行SQl语句
# 获取表的全部数据fetchall
q=cursor.execute('select * from class')
print(q)
# 使用fetchall查询全部数据
data1=cursor.fetchall()
print(data1)

# execute执行SQl语句
# 获取标的单条或者指定数据fetchall
p=cursor.execute('select * from class where cid=2')
print(p)
# 使用fetchone查询全部数据
data2=cursor.fetchone()
print(data2)

# 关闭数据库连接
connection.close()




