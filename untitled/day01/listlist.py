"""
linklist.py 链表程序实现
重点代码
思路分析
1.创建节点类，生成节点对象
包含数据和下一个节点的引用
2.链表类，生成链表对象，可以对链表进行数据操作
"""
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Linklist:
    def __init__(self):
        self.head=Node(None)

    def init_list(self,list_):
        p=self.head  #p为移动变量
        for i in  list_:
            p.next=Node(i)
            p=p.next   #向后移动一个节点
     # 遍历链表
    def show(self):
         p=self.head.next#第一个有效节点
         while p is not None:
             print(p.data,end='')
             p=p.next
         print()#换行
    def get_length(self):
         n=0
         p=self.head
         while p.next is not None:
             n +=1
             p=p.next
         return n



      #判断链表是否为空
    def is_empty(self):
         if self.get_length()==0:
             return True
         else:
              return  False

    def clear(self):
         self.head.next=None
    def append(self,data):
         node=Node(data)#生成新节点
         p=self.head
         while p.next is not None:
             p=p.next
         p.next=node
    #x选择位置插入节点
    def insert(self,index,data):
        if index<0 or index>self.get_length():
           raise IndexError("INDEX OUT OF RANGE")
        #定义p移动到插入位置的前一个
        p=self.head
        for i in range(index):
            p=p.next
            node=Node(data)
            #插入
            node.next=p.next
            p.next=node
    # 删除节点
    def delete(self,data):
        p=self.head
        while p.next and p.next.data !=data:
            p=p.next
        if p.next is None:
            raise ("value is error")
        else:
            p.next=p.next.next


    #获取节点值
    def get_item(self,index):
         if index <0 or index>=self.get_length():
             raise IndexError("index out of range")
         p =self.head.next
         for i in range(index):
              p=p.next
         return p.data


#     获取链表长度
#  判断链表是否为空def
# 清空链表




link_=Linklist()
l=[1,2,3,4,5]
link_.init_list(l)
link_.show()
print(link_.get_length())
print(link_.is_empty())
link_.delete(3)
link_.show()
link_.insert(2,10)
link_.show()
print(link_.get_item(3))
print(link_.get_item(100))
