day11作业
1. 三合一
2. 当天练习独立完成
3. 使用面向对象,描述下列情景.
   玩家(具有攻击力)攻击敌人,敌人(具有血量)受伤后掉血,还可能死亡(掉装备).
   敌人(具有攻击力)攻击玩家,玩家(具有血量)受伤后掉血并且碎屏,还可能死亡(游戏结束).


class Player:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def atk_enemy(self, atk, Enemy):
        Enemy.hp -= atk
        if Enemy.hp <= 0:
            Enemy.equip = 0
            del Enemy

        else:
            return Enemy.hp


class Enemy:
    def __init__(self, atk, hp,):
        self.atk = atk
        self.hp = hp


    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def atk_player(self, atk, Player):
        Player.hp -= atk
        if Player.hp <= 0:
            print("Game over")
            del Player
        else:
            print("碎屏")
            return Player.hp





4. 使用面向对象,描述下列情景.
   张无忌 教 赵敏 打篮球
   赵敏 教 张无忌 画眉
   张无忌 上班赚了10000元
   赵敏  上班赚了5000元.

   要求:遇到数据,使用属性进行封装.
class Person:
    def __init__(self,name):
        self.name=name
    @property
    def name(self):
        return  self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    def teach(self,person_other,str_skill):
#      类内部，可以私有变量，也可以使用属性
#      类外部，只能使用属性
        print("%s教%s%s技能"%(self.name,person_other.name,str_skill))
    def work(self,money):
        print("%上班赚了%d钱"%(self.name,money))
zwj=Person("张无忌")
zm=Person("赵敏")
zwj.teach(zm,"打篮球")
zm.teach(zwj,"画眉")
5. 倾尽一切手段,在互联网中搜集封装的知识,并结合课堂所讲.
   总结为自己的话术,为"全国面向对象课程答辩峰会"做准备.day11作业
