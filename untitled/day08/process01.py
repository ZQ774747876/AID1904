"""

"""
import multiprocessing as mp
from time import  sleep
a=1
def fun():
    print("开始一个新的进程")
    sleep(3)
    global a
    print("a=",a)
    print("子进程结束了")
p=mp.Process(target=fun())
p.start()
sleep(2)
print("fujincheng")
p.join(1)
print("a=",a)