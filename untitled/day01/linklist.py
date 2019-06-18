"""
linklist链表程序实现
重点代码
思路分析：
1.创建节点类，生成节点对象，包含数据和下一个节点的引用
2.链表类，可以生成链表对象，可以对脸表进行数据操作
"""
#节点类
class Node():
    def __init__(self,data,next):
        self.data=data
        self.next=next
class Linklist():
    """
    建立链表模型
    进行链表操作
    """
    def __init__(self):
#初始化一个链表，生成一个头结点，表示链表开始节点
     self.head=Node(None)
#初始添加一组链表节点
    def list_list(self,list_):
        p=self.head#p为移动变量
        for i in list_:
            p.next=Node(i)
            p=p.next
#遍历链表
    def show(self,):
       p=self.head.next  #第一个有效节点
       while p is not None:
           print(p.data,end=' ')
           p=p.next
    print()
#获取链表长度
    def get_length(self):
        n=0
        p=self.head
        while p.next is not None:
            n +=1
            p=p.next
        return  n
#判断链表是否为空
    def is_empty(self):
        if self.get_length()==0:
            return True
        else:
            return False
#清空链表
    def clear(self):
        self.head.next=None

    def append(self,data):
        node=Node(data)
        p









