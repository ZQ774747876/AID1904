"""
UDP 客户端流程
"""
ADDR=('127.0.0.1',9999)
#创建套接字
from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
#循环发送消息
while True:
    data=input("Msg>>")
    if not data:
        break

    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print('from server:',msg.decode())
sockfd.close()