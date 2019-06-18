# day13
# 1. 三合一
# 2. 独立完成练习
# 3. 开放性作业:洞察客观世界的事物,自行定义子类(2个)与父类(1个).
# 4. (扩展)有若干个图形(圆形/矩形....)
#    定义图形管理器
#       -- 记录所有图形(多个圆形对象,多个矩形对象),
#       -- 提供计算总面积的方法.
# *5. 穷尽一切手段,在互联网上搜集继承,与多态相关的资料.
#    并结合课堂所讲,写成自述文档.为答辩准备.
#    关键词:继承,多态,面向对象,三大特征.开闭原则,依赖倒置,
#--------------------------调用者-----------------
class GraphicManager:
    """
    图形管理起
    """
    def __init__(self,):
        self.__graphics=[]
    def add_graphic(self,graphic):
        self.__graphics.append(graphic)
    def get_total_area(self):
        total_area=0
        for item in self.__graphics:

            total_area += item.calulate_area()
        return total_area
class Grapphic:
    def calulate_area(self):
        pass
#------------------------------------------
class Circle(Grapphic):
    def __init__(self,r):
        self.ridius=r
    def calculate_area(self):
         return 3.14*self.ridius**2

class Rectangle(Grapphic):
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def calculate_area(self):
        return self.length*self.width
manager=GraphicManager()
g01=Circle(10)
manager.add_graphic(g01)
manager.add_graphic(Rectangle(10,20))
result=manager.get_total_area()
print(result)