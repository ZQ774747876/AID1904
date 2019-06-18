import pymysql
import re
f=open('dict.txt')

db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   passwd='123456',
                   database='stu',
                   charset='utf8')
cur=db.cursor()

sql="insert into words(word,mean)values(%s,%s)"
for line in f:
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
   
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()
f.close()
cur.close()
db.close()