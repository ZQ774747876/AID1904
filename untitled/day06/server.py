

DICT
f=open('dict.txt','wb')
from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
server_addr=('127.0.0.1',8888)
sockfd.bind(server_addr)
while True:

    data, addr = sockfd.recvfrom(1024)
    if data==
    print()
    sockfd.sendto(b'receive', addr)
sockfd.close()