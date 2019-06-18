"""
管道通信示例
"""
from multiprocessing import  Pipe,Process
import os,time
#创建管道对象
fd1,fd2=Pipe()
def read():
    while True:
     data=fd1.recv()#从管道获取消息
     print(data)
def write():
    while True:
      time.sleep(2)
      data=fd2.send({'name':1,'age':2})#向管道发送内容
r=Process(target=read)
w=Process(target=write)
r.start()
w.start()
r.join()
w.join()
