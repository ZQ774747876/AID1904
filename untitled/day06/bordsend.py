"""
http请求响应实列
"""
from socket import *
s=socket()
s.bind(("127.0.0.1",6666))
s.listen(3)
c,addr=s.accept()
print("connect from ",addr)
data=c.recv(4026)
print(data)
data="""HTTP/1.1 200 OK
CONTENT-TYPE:TEXT/233565646461221544



"""
c.send(b'ok')
s.close()
