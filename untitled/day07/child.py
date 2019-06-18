import os
from time import sleep
def f1():
    for i in range (5):
        sleep(2)
        print("写代码")
def f2():
    for i  in range(5):
        sleep(1)
        print("侧代码")
pid=os.fork()
if pid<0:
    print("error")
elif pid==0:
    p=os.fork()
    if p==0:
        f2()
    else:
        os._exit(0)#一级子进程退出
else:
    os.wait()#等待二级子进程退出
    f1()
