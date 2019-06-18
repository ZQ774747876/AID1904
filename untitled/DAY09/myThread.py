"""
thread_class
自定义线程类演示
"""
from  threading import Thread
"""
1.继承Thread
2.重写_init__和run
"""
class Threadclass(Thread):
    def __init__(self,attr):
        self.attr=attr
        super().__init__()

    #很多方法配合完成任务
    def f1(self):
        print("buzou1")
    def f2(self):
        print("buzou2")

    def run(self):
        self.f1()
        self.f2()
t=Threadclass("xxxx")
t.start()
t.join()