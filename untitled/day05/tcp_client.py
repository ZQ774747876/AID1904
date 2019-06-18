"""
tcp_client.py tcp客户端重点代码
"""
from socket import *
#创建TCP套接字
sockfd=socket()#参数默认即tcp套接字
#连接服务端程序
#server_addr=()
sockfd.connect(("127.0.0.1",6666))
#sockfd.connect(server_addr)
while True:
#消息发送接受
    data=input('Msg>>')
    if not data:
        break
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    print("server",data.decode())

sockfd.close()
