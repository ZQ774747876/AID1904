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
        print("玩家攻击")
        Enemy.damage(self, atk)

    def damage(self, value):
        self.hp -= value
        print("玩家受伤了,还剩%d血量" % self.hp)
        print("屏幕岁啦")
        if self.hp <= 0:
            self.death()
    def __death(self):
        print("玩家死啦,GAME OVER")


class Enemy:
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

    def damage(self,value):
        self.hp -=value
        print("敌人受伤了,还剩%d血量"%self.hp)
        if self.hp<=0:
           self.death()
    def __death(self):
        print("敌人死啦,掉下了?装备")
p01=Player(50,100)
e01=Enemy(100,100)

