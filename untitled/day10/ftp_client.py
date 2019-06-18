"""
ftp客户端
"""
#创建客户端网络

from  socket import *
ADDR=('127.0.0.1',8080)#服务器地址

#客户端功能处理类
class FTPClient():
    def __init__(self,sockfd):
      self.sockfd=sockfd
    def do_list(self):
        self.sockfd.send(b'L')#发送请求
        data=self.sockfd.recv(128).decode()
        if data=='OK':
            # 一次性接受文件列表字符串
             data=self.sockfd.recv(4096)
             print(data.decode())
        else:
            print(data)
    def do_get(self,filename):
        #发送请球
       self.connfd.send(('6'+filename).encode())
        #等待回复
       data=self.connfd.recv(128).decode()
       if data=='OK':
           fd=open(filename,'wb')
           #接受文件
           while True:
               data=self.sockfd.recv(1024)
               if data==b'##':
                   break
               fd.write(data)
           fd.close()
       else:
           print(data)






#创建客户端网络
def main():
    sockfd=socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp=FTPClient(sockfd)#实例化对象


    #循环发送请求
    while True:
        print("****************命令选项******************")
        print("****************list******************")
        print("****************get file******************")
        print("****************put file******************")
        print("****************quit******************")

        cmd=input("输入命令：")

        if cmd.strip()=='list':
            ftp.do_list()
        elif cmd[:3]=="get":
            filename=cmd.strip().split(" ")[-1]
            ftp.do_get(filename)
        else cmd.strip()=="quit":

        sockfd.send(cmd.encode())

if __name__=="__main__":
    main()