"""
练习
"""
from threading import Thread
from time import  sleep,ctime
class MyThead(Thread):
        def __init__(self,target=None,args=(),kwargs={}):
            super().__init__()
            self.target=target
            self.args=args
            self.kwargs=kwargs
        def run(self):
            self.target(*self.args,**self.kwargs)
def player(sec,song):
    for i in range(3):
        print("playing %s:%s"%(song,ctime()))
        sleep(sec)
t=MyThead(target=player,args=(5,),kwargs={'song':'冰冰'})
t.start()
t.join()
