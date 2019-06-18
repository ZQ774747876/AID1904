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
with open('MM.jpg','rb') as fd:
    data=fd.read()
try:
    sql="insert into Image values(1,'MM.jpg','%s')"%data
    cur.execute(sql,[data])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()
