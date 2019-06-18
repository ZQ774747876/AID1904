# 需求:老张开车去东北
"""
设计原则：
1.开闭原则
  扩展（增加新功能）开放（允许）
  修改（改变



"""

class Person:
  def __init__(self, name):
    self.name = name

  @property

  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  def to(self, type, str_pos):
    print(self.name)
    type.run(str_pos)


class Car:
  def run(self, str_pos):
    print("行驶到:", str_pos)
# 练习：手雷爆炸了，可能伤害敌人，玩家
#  还可能伤害未知的事物
#如果增加了新事物，不影响手雷的代码
class Grenade:
    def blast(self,target):
        """
        爆炸
        """
        # 调用目标的受伤方法
        if not isinstance(target,Damageable):
           raise TypeError
        target.damage(200)
class Damageable:
    def damage(self,value):
        raise NotImplemented

class Player(Damageable):
    def damage(self,value):
        print("玩家扣%d血，并且碎屏"%value)
class Enemy(Damageable):
    def damage(self,value):
        print("敌人扣%d血，并且冒字"%value)
g01=Grenade()
p01=Player()
e01=Enemy()
g01.blast(p01)
g01.blast(e01)

