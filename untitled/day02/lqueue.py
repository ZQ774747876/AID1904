"""
链式队列
重点代码
思路分析：
1.基于链表模型完成储存结构
2.链表开端作为队头，尾端作为队尾
"""
class QueueError(Exception):
    pass
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Lqueue:
    def __init__(self):
        self.front=self.rear=Node(None)
    def is_empty(self):
        return self.front==self.rear
    def enqueue(self,elem):
        self.rear.next=Node(elem)
        self.rear=self.rear.next
    def dequeue(self):
        if self.front==self.rear:
            raise QueueError("QUEUE IS EMPTY")
        self.front=self.front.next
        return self.front.data
if __name__=="__main__":
    lq=Lqueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())
    print(lq.dequeue())