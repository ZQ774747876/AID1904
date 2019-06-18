from multiprocessing import Process
from time import sleep
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("i am %s"%name)

# p=Process(target=worker,args=(2,'brafee'))
p=Process(target=worker,kwargs={"name":'baer',"sec":5})
p.start()
p.join()