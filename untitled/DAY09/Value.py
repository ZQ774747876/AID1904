from multiprocessing import Value,Process
import time
from random import  randint
#创建共享内存
money=Value('i',5000)
#修改共享内存
def man():
    for i in  range(30):
        time.sleep(0.2)
        money.value += randint(1,1000)

def gril():
    for i in range(30):
        time.sleep(0.15)
        money.value -=randint(100,800)

m=Process(target=man)
g=Process(target=gril)
m.start()
g.start()
m.join()
g.join()
#获取共享内存值
print("一月余额",money.value)