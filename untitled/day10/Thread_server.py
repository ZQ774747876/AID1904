"""
思路分析：
1.基本与进程相符，只是换线程
"""
from socket import *
from  threading import Thread
import sys
#创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
#处理客户端请求
def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


S=socket()
S.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
S.bind(ADDR)
S.listen(100)
#循环等待客户端链接
while True:
    try:
        c,addr=S.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    #创建线程处理客户端请求
    t=Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()
