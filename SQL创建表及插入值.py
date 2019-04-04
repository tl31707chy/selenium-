import  pymysql
connection=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='k1',charset='utf8')
# 用游标操作数据
cursor=connection.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("drop table IF exists student")
# 创建表
sql = """create table student (id int,name char(20),age int,sex char(20),birthday char(20))"""
cursor.execute(sql)
# 插入数据
sql="""insert into student  value ('1','张三','24','男','1995-02-19')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   connection.commit()
except:
   #回滚,以防有任何错误
   connection.rollback()

# 关闭数据库连接
connection.close()