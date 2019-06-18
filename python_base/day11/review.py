
"""
面向对象
类
---概念:抽象的
--语法
 class 类名:
       成员...
       def _init_(self,参数):
        self.变量名=参数
对象
  --概念:具体的
  --语法:
    变量名=构造函数(参数列表)
    从设计角度讲:先有对象,再有类--->抽象化的过程
    从编码角度讲:先有类,再有对象--->实列化(具体化)的过程
类中成员
 --实例成员
       变量
           概念:表示对象的数据,(每个对象的数据都可以不一样)[杯子]
           语法:对象.名称=?
           备注:通常在_init_方法中定义
        方法
           概念:表示对象的行为,常用于操作实列变量
           语法:
             @classmethod
             def 方法名称(cls):
                     方法体
            备注:@classmethod的作用是,调用方法自动传递类名,
                 只能访问类变量,不能访问实列成员(因为没有self)

 --类成员:
       概念:表示类的数据,(所有对象共享的数据)[饮水机]
       语法:在类中,方法外定义变量
 --静态方法
       概念:将函数放到类中.
       语法:
         @staticmethod
         def 方法名称():
             方法体
         备注:@staticmethod的作用是, 调用方法是不自动传递参数
  总结:实例方法操作实例变量
      类方法操作类变量
      静态方法,什么都不操作
"""
class A:
    def __init__(self,a):
        self.a=a
    def fun02(self):