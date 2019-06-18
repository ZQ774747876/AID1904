"""
进程属性基本示例
"""
from multiprocessing import Process
from time import sleep,ctime
def tm():
    for i in range(3):
        sleep(2)
        print(ctime())
p=Process(target=tm)
p.daemon=False #子进程会随父进程一起退出
p.start()
print("name",p.name)
print("PID",p.pid)
print('IS alive ',p.is_alive())
