"""
select 语句
"""
import pymysql
#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   passwd='123456',
                   database='stu',
                   charset='utf8')
#获取游标(用于进行数据操作的对象，承载操作结果）
cur=db.cursor()
#执行sql语句
sql="select * from student where sex='m'"
cur.execute(sql)
one_row=cur.fetchone()
print(one_row)
many_row=cur.fetchmany(2)
print(many_row)
all_row=cur.fetchall()
print(all_row)