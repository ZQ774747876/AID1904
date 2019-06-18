"""
封装
   数据角度
   行为角度
   设计角度
"""
class A:
   b=50
   def __init__(self,a):
       self.a=a
   def fun01(self):
       print("fun01")
obj01=A(10)
print(obj01.a)
obj01.fun01()#自动传递对象地址

# 通过类访问实例方法,但必须手动传递对象地址
obj02=A(20)
A.fun01(obj02)
print(A.b)
print(obj01.b)