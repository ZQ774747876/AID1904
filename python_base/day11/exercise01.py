class Enemy:
    def __init__(self, atk, hp):
        # 由于公开了实际存储数据的变量
        #  所以类定义者失去了对变量的保护力度。
        self.atk=atk
        self.hp=hp
    @property #目的：拦取读取操作，本质:创建property对象，注册读取对象
    def atk(self):
        return self.__atk
    @atk.setter#目的：拦截写入操作，
    def atk(self, value):
        if 10 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击力不在范围")
    @property#免费
    def hp(self):
        return self.__hp
    @hp.setter
    def set_hp(self, hp):
        if 0 <= hp <= 100:
            self.__hp = hp
        else:
            raise Exception("血量有误")