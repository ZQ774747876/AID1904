"""
wait 处理僵尸
"""
import os
pid=os.fork()
if pid<0:
    print("error")
elif pid==0:
    print("chuld process",os.getpid())
    os._exit(3)
else:
    p,status=os.wait()#阻塞等待子进程退出
    print("p:",p)
    #还原退出状态
    print("status",os.WEXITSTATUS(status))
    while True:
        pass
