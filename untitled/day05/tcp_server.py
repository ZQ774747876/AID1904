"""
tcp_server.py tcp套接字
"""
#创建流式套接字
import socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
socket.bind(('127.0.0.1',6666))
#设置socket为监听套接字
socket.listen(100)
#等待处理客户端连接
while True:
    print("waiting form connect...")
    try:
        connfd,addr=socket.accept()
        print("connect from",addr)
    except KeyboardInterrupt:
        print("server exit")#收发消息
        break
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print("message:",data.decode())
        n=connfd.send(b"hello word")
        print("send %d bytes"%n)
    #关闭套接字
    connfd.close()#断开连接
socket.close()