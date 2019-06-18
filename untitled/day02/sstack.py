"""
sstack.py栈模型顺序存储
重点代码
"""
# 思路分析：
# 1.列表即顺序存储，但是功能太多，不符合站模型
# 2.利用列表，封装类，提供栈的接口方法
#自定义异常类




# 顺序栈类封装
class SStack:
   def __init__(self):
       # 列表最后一个元素为栈顶元素
       self._elems=[]
    #判断栈是否为空
   def is_empty(self):
       return  self._elems==[]
    #入栈
   def Push(self,elem):
       self._elems.append(elem)
   #出栈
   def Pop(self):
       if not self._elems:
             raise StackError("stack is empty")
       return self._elems.pop()

   #查看栈顶元素
   def Top(self):
       if not self._elems:
           raise StackError("stack is empty")
       return self._elems[-1]



if __name__=="__main__":
    st=SStack()#初始化栈
    st.Push(10)
    st.Push(20)
    st.Push(30)
    print(st.Top())