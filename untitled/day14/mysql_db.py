"""
mysql数据库写操作练习
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
try:
    #插入数据
   # sql="insert into interest values(3,'joy','draw','8',5488.0,'画的鸡蛋还行')"
   #  name=input("name:")
   #  age=int(input("age:"))
   #  sex=input("sex:")
   #  score=float(input('score:'))
  #  sql="insert into student(name,age,sex,score)values('%s',%d,'%s',%f)"%(name,age,sex,score)
   # sql="insert into student(name,age, sex, score)values(%s,%s,%s,%s)";
   # sql="update student set age=22 where name='lily'"
    sql="delete from student where score<70"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()#返回到commit之前的状态
    print(e)

#关闭数据库
cur.close()
db.close()
