"""
poll_server
思路分析：
创建套接字作为监控IO
将套接字register
创建查找字典，并维护(要时刻与注册IO保持一致）
循环监控I0发生
处理发生的IO
"""
from socket import *
from select import *
#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)
#创建poll对象关注s
p=poll()
#建立查找字典，用于通过fileno查找IO对象
fdmap={s.fileno():s}
#关注s
p.register(s,POLLIN|POLLERR)
#循环监控
while True:
    events=p.poll()
    for  fd,events in events:
    #区分事件，进行处理
    if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("Connect from ",addr)
            #添加新的关注IO
            p.register(c.POLLIN|POLLERR)
            fdmap[c.fileno()]=c#维护字典
    #按位于判定是POLLIN就绪
    elif events & POLLIN:
        data=fdmap[fd].recv(1024)
        if not data:
            p.unregister(fd)
            fdmap[fd].close()
            del fdmap[fd]
            continue
        print("Receive",data.decode())
        fdmap[fd].send(b'OK')
