"""
队列的顺序存储
思路分析：
1.基于列表完成存储结构
2.通过封装规定队头和队尾
"""
#队列操作类
class QueueError(Exception):
    pass
class SQueue:
    def __init__(self):
        self._elems=[]
    def is_empty(self):
        if len(self._elems)==0:
            return True
        else:
            return False
    def enqueue(self,elem):
      return self._elems.append(elem)

    def dequeue(self):
        if not self._elems :
            raise QueueError("queue is empty")
        return self._elems.pop(0)

if __name__=="__main__":
    sq=SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())