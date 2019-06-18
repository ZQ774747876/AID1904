"""

内置可重写函数
"""
class Student:
    def __init__(self,name,score,age):
        self.name=name
        self.score=score
        self.age=age
    def __str__(self):
        return "姓名为%s，成绩为…%d，年龄为%d"%(self.name,self.score,self.age)
    def __repr__(self):
        return 'Student('zs',100,25)'
s01=Student("zs",100,25)
print(s01)
re=eval(s01.__repr__())
print(re)