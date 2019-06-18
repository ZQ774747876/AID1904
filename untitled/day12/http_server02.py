"""
http_server 2.0
IO多路复用 http练习
思路分析：
1，使用类进行封装
2.从用户使用角度决定类的编写
"""
#具体HTTP server功能
from  socket import  *
from select import *
class HTTPserver:
    def __init__(self,host,port,dir):
        #添加属性
      self.address=(host,port)
      self.host=host
      self.port=port
      self.dir=dir
      self.creat_socket()
      self.bind()
      self.rlist=[]
      self.wlist=[]
      self.xlist=[]
#创建套接字
    def create_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    def bind(self):
        self.sockfd.bind(self.address)
    def handle(self,connfd):
        request=connfd.recv(1024)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        #提取请求内容
        request_line=request.splitlines()[0]
        info=request_line.decode().spilit(' ')[1]
        print(connfd.getpeername(),":",info)
        #info分为访问网页或者其他内容
        if info=='/' or info[-5:]==".html":
            self.get_html(connfd.info)
        else:
            pass

    def get_html(self,connfd,info):
           if info=="/":
               filename=self.dir+"/index.html"
           else:
               filename=self.dir+info
           try:
               fd=open(filename)
           except Exception:
               responsHeaders="HTTP/1.1 404 NOT FOUND"
               responsHeaders+='\r\n'
               responsBody="Sorry,Not FOUND The Page"
           else:
               #存在网页
                responsHeaders="HTTP/1.1  200 OK\r\n"
                responsHeaders+="\r\n"
                responsBody=fd.read()
           finally:
               response=

    #启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("LISTEN THE PORT %d"%self.port)
        self.rlist.append(self.sockfd)
        while True:
         rs,ws,xs=select(self.rlist,self.wlist,self.xlist)
         for r in rs:
            if r is self.sockfd:
             c,addr=r.accept()
             print("Connect from ",addr)
             self.rlist.append(c)
         else:
             #处理请求
             self.handle(r)



    HOST='0.0.0.0'
    POST=8000
    DIR="./static"#网页存储位置

    httpd=HTTPserver(HOST)

if __name__=="__main__":
    #希望通过HTTPserver快速的搭建http服务，用于展示自己的网页
