class People:
    def __init__(self,name,attack,attack_distance,life_value):
        self.name=str(name)
        self.attack=int(attack)
        self.attack_distance=int(attack_distance)
        self.life_value=int(life_value)

    def print_self(self):
         print(self.name,self.attack,self.attack_distance,self.life_value)

# people01=People("小王",25,15,14)
# people01.print_self()
# list_all_people=[]
# for i in range(3):
#     name=input("请输入姓名:")
#     attack = input("请输入攻击力:")
#     attack_distance=input("请输入攻击距离:")
#     life_value=input("请输入生命值:")
#     p01=People(name,attack,attack_distance,life_value)
#     list_all_people.append(p01)
#     p01.print_self()
# print(list_all_people)

def find01(list_target):
    for item in list_target:
       if item.name=="灭霸":
           return item
list01=[
      People("灭霸",9999,99999,9999),
      People("師右",9000,100,9999),
      People("钢铁侠",4000,100,9999),


]
# re=find01(list01)
# re.print_self()
# 练习2:定义函数,在敌人列表中,查找攻击力大于等于5000的所有敌人
def find02(list_target):
    result=[]
    for item in list_target:
        if item.attack>=5000:
            result.append(item)
    return result

re01=find02(list01)
for item in re01:
    item.print_self()



# 练习:统计一个类,
#     创建了多少对象(记录init调用次数).画内存图
class Enemy:
  count = 0

  @classmethod
  def print_count(cls):
    print("总共创建了%d个对象" % cls.count)

  def __init__(self):
    Enemy.count += 1


e01 = Enemy()
e02 = Enemy()
Enemy.print_count()
"""
静态方法:
 将函数放到类中
"""
class vector2:
    #向量
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @staticmethod
    def get_right():
        return vector2(0,1)

    @staticmethod
    def get_up():
        return  vector2(-1,0)
    @staticmethod
    def get_left():
        return  vector2(0,-1)
    @staticmethod
    def get_down():
        return  vector2(1,0)
pos01=vector2(1,2)
right=vector2.get_right()
#定义类方法,获取向左边的方向
#定义类方法.获取向下的方向
#表示02点,向左的点
pos03=vector2(0,2)
left=pos03.get_left()
pos04=vector2(pos03.x+left.x,pos03.y+left.y)

    # 表示向右01
    # 表示向上01

#点
pos01=vector2(1,2)
#表示 pos01 点向右:点+方向
pos02=vector2(pos01.x+right.x,pos01.y+right.y)
print(pos02.x,pos02.y)
"""
00 01 02 03 04
10 11 12 13 14
20  21 22 23 24

"""

