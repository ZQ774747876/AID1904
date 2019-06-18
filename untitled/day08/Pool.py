"""
进程池使用演示
"""
from multiprocessing import Pool
from time import  sleep,ctime
#进程池时间
def worker(msg):
    sleep(2)
    print(msg)
    return  ctime()
#创建进程池
pool=Pool(10)
#向进程池添加执行事件
for i in range(20):
    msg="HELLO %d"%i
    #r代表func事件的一个对象
    r=pool.apply_async(func=worker,args=(msg,))
#关闭进程池
pool.close()
#回收进程池
pool.join()
print(r.get())