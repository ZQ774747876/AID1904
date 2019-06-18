"""
gevent_server 基于协程的tcp并发

"""
import gevent
from gevent import monkey
monkey.path_all()#在导入socket前执行
from socket import  *
#创建TCP套接字
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(s)
while True:
    c,addr=s.accept()
    print("connect from ",addr)
   # handle(c)#循环方案
   gevent.spawn()
s.close()
