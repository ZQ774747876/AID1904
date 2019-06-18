"""
lstack.py 栈的链式存储
重点代码
"""
# 异常类
class StackError(Exception):
    pass
#节点类
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


#栈操作类
class LStack:
    def __init__(self):
    # 定义栈顶位置属性
        self._top=None

    def is_empty(self):
        return self._top is None
    #

    def Push(self,elem):
        self._top=Node(elem,self._top)

    # 弹栈
    def Pop(self):
        if self._top is None:
            raise StackError("Stack is empty")
        val=self._top.data
        self._top=self._top.next
        return val
    # 查看栈顶值
    def top(self):
        if self._top is  None:
            raise StackError("stack is  empty")
        return self._top.data

if __name__=="__main__":
    ls=LStack()
    ls.Push(10)
    ls.Push(20)
    ls.Push(30)
    print(ls.Pop())
    print(ls.Pop())
    print(ls.Pop())


