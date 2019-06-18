"""
event线程互斥方法演示
"""
from threading import Event,Thread
from time import  sleep

s=None
e=Event()
def 扬子龙():
    print("样子荣前来拜山头")
    global s
    s="天王盖地虎"
    e.set()#对e设置
t=Thread(target=扬子龙())
t.start()

print("说对口令就是自己人")
e.wait()#阻塞等待口令
if s=="天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是自己人")
else:
    print("打死他。。。")
t.join()
