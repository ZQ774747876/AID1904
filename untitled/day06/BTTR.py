"""
套接字属性
"""
from socket import *
s=socket()
#设置套接字端口，立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",6666))
s.listen(3)
c,addr=s.accept()
print('地址类型:',s.family)
print("套接字类型",s.type)
print("获取绑定的地址：",s.getsockname())
print("获取文件描述符：",s.fileno())
print("获取链接的客户端地址：",s.getpeername())
print("获取选项值：",s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
