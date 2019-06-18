"""
ftp文件服务器
多线程并发/线程练习
"""
from socket import  *
from  threading import  Thread
import  os
import time
import sys
#全局变量

# HOST = '0.0.0.0'

HOST ='0.0.0.0'
PORT =8080
ADDR=(HOST,PORT)
FTP='/home/tarena/1904/untitled/day10/FTP/' #文件库位置

#创建文件服务器端功能类
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd=connfd
        super().__init__()
    def do_list(self):
    #获取文件列表
        files=os.listdir(FTP)
        if not files:
            self.connfd.send("该文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()

    def do_get(self,filename):
        try:
            fd=open(FTP+filename,'rb')
        except Exception:
            self.connfd.send("文jian ".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        # 拼接文件列表
        files = ''
        for file in  files:
             if file[0] !='.' and os.path.isfile(FTP+file):
                 files +=file +"\n"
        self.connfd.send(files.encode())

    #循环接受客户端请求
    def run(self):
        while True:
            data=self.connfd.revc(1024).decode()
            if data=="Q" or not data:
                return  
            elif data =="L":
                self.do_list()
            elif data[0]=='G':
                filename=data.split(' ')[-1]
                self.do_get(filename)




#网络搭建
def main():
    # 创建套接字
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(3)
    print("listen the part %d... "% PORT)
    while True:
        try:
          connfd,addr=sockfd.accept()
        except KeyboardInterrupt:
            print("服务器程序退出")
            return
        except Exception as e:
            print(e)
            continue
        #创建新的线程处理客户端
        client= FTPServer(connfd)
        client.setDaemon(True)
        client.start()#运行run方法

if __name__=="__main__":
 main()