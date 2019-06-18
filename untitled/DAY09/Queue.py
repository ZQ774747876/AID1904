#创建消息队列
from multiprocessing import Queue,Process
from  random import  randint
from time import sleep
q=Queue(3)
def request():
    for i in range(19):
        x=randint(0,100)
        y=randint(0,100)
        print("=======")
        q.put((x,y))

def handle():
    while True:
        sleep(1)
        try:
            x,y=q.get(timeout=5)
        except:
            break
        else:
            print("%d + %d=%d"%(x,y,x+y))
p1=Process(target=request)
p2=Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()