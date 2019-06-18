"""
思路分析：
1.每当一个客户端被创建一个新的进程作为客户需处理进程
2.客户端如果结束，对应进程应该销毁
"""
from socket import *
import  os
import signal
#创建监听套接字
HOST='0,0,0,0'
PORT=8888
ADDR=(HOST,PORT)

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
#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
while True:
    try:
        c,addr=S.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

  #创建子进程，处理这个客户端
    pid=os.fork()
    if pid==0:
        S.close()
        handle(c)
        os._exit(0)#handle处理完客户端请求子进程也退出
    #无论出错或者父进程都要循环回去接受请求
    #c对于父进程没用
    c.close()
