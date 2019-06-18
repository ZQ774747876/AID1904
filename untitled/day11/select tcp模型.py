"""
select tcp服务模型
"""
from socket import *
from select import  select
#创建一个监听套接字作为关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)
#设置关注列表
rlist=[s]
wlist=[]
xlist=[]
#监控IO
while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    #遍历3个返回列表，处理IO
    for r in rs:
        if r is s:
           c,addr=r.accept()
           print("CONNECT from ",addr)
           rlist.append(c)#增加新的IO事件
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove()
                r.close()
                continue
            print("Receive",data.decode())
            wlist.append(r)

    for w in ws:
       w.send(b'OK')
       wlist.remove(w) #使用后移除
    for x in xs:
        pass
