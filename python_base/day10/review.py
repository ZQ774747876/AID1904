"""
面向对象
 面向过程:考虑细节,涿步实现  "干活的人"
 面向对象:识别对象/分配职责/建立交互 "雇人干活"
 类和对象
  --语法:
     创建类
     class 类名:
       def_init_(self):
       self.数据=值
       行为
     创建对象
     构造函数指的是类中的_init_方法
     变量名=构造函数(参数)
  --类:类别
  --对象:个体
  问题:先有对象还是先有类
  --设计角度:先有对象,再有类,抽象化过程
  --编码角度:先有类,再有对象,具体化的过程

  类和对象的区别:抽象与具体的区别
  类和类的区别:行为的不同
  对象与对象的区别:数据的不同
"""
# 定义:做人类,具有数据(姓名,攻击力,攻击距离,生命值)
# 行为:(在控制台输出对象数据)
# 练习2:在控制台中录入3个敌人,存入列表中
# 并在控制台中循环调用print_self方法

class Enemy:
  def __init__(self, name, atk, distance, hp):
    self.name = name
    self.atk = atk
    self.atk_distance = distance
    self.hp = hp

  def print_self(self):
    print(self.name, self.atk, self.atk_distance, self.hp)

def find01(list_target):
  for item in list_target:
    if item.name == "灭霸":
      return item
list01 = [
  Enemy("灭霸", 9999, 999999, 99999),
  Enemy("蚩尤", 4000, 10, 500),
  Enemy("钢铁侠", 5000, 30, 6000),
]
re = find01(list01)
re.print_self()