from socket import *
from select import *
#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)
#创建epoll对象关注s
p=epoll()
#建立查找字典，用于通过fileno查找IO对象
fdmap={s.fileno():s}
#关注s
p.register(s,EPOLLIN|EPOLLERR)
#循环监控
while True:
    events=p.poll()
    for  fd,events in events:
    #区分事件，进行处理
    if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("Connect from ",addr)
            #添加新的关注IO
            p.register(c.EPOLLIN|EPOLLERR)
            fdmap[c.fileno()]=c#维护字典
    #按位于判定是POLLIN就绪
    elif events & EPOLLIN:
        data=fdmap[fd].recv(1024)
        if not data:
            p.unregister(fd)
            fdmap[fd].close()
            del fdmap[fd]
            continue
        print("Receive",data.decode())
        fdmap[fd].send(b'OK')