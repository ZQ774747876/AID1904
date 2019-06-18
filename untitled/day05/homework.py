#输入文件名
# filename=input("file:")
# try:
#     fr=open(filename,'rh')
# except FileNotFoundError as e:
#     print(e)
# else:
#     fw=open('file.jag','wb')
#
# while True:
#     data=fr.read(1024)
#     if not data:
#         break
#     fw.write(data)
import time
f=open('log.txt','a+')
n=0
f.seek(0,0)#
for line in f:
    n+=1
while True:
    n+=1
    time.sleep(1)
    s="%d.  %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()#随时看到文件变化