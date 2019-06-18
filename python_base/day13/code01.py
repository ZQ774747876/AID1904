"""
继承
财产：钱不用孩子挣，但是可以花
皇位：江山不用孩子打，但是可以坐
精神：
....
代码;子类不用写，但是可以用
练习：定义子类：狗（行为：看守）
             鸟（行为：飞）
         父类：动物（行为：叫）

"""
class Animal:
    def __int__(self,name):
     self.name=name
    def cry(self):
        pass
class Dogs(Animal):
    def __init__(self,name,score):
        super().__init__(name)
        self.score=score
    def watch(self):
        print("kanshou")

class Birds(Animal):
    def fly(self):
        pass
d01=Dogs()
b01=Birds()
a01=Animal()
d01.watch()
print(isinstance(d01,Birds))
