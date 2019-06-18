"""
  练习1:
    将通用函数定义在list_helper.py模块中
    在当前模块中,测试find.

  练习2:
    功能1:定义函数,在列表中查找"如来神掌"技能.
    功能2:定义函数,在列表中查找攻击力大于50的单个技能.
    功能3:定义函数,在列表中查找cd大于0的单个技能.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示
"""
from day18.common.list_helper import ListHelper


class SkillData:
  def __init__(self, name, atk, cd, speed):
    self.name = name
    self.atk = atk
    self.cd = cd
    self.atk_speed = speed


list01 = [
  SkillData("降龙十八掌", 100, 60, 50),
  SkillData("如来神掌", 80, 50, 30),
  SkillData("一阳指", 20, 0, 80)
]

# result01=ListHelper.skill_number01(list01,lambda e:e.atk<1000)
# result02=ListHelper.skill_number01(list01,lambda e:e.cd==0)
#
#
#
# def get_atk_list(list_target):
#   list01=[]
#   for item in list_target:
#     list01.append(item.atk)
#   print(list01)
#
# get_atk_list(list01)
#
# [2,4,3,37]
#
#
# for item in map(lambda e:e.name,list01):
#   print(item)

# for item in filter(lambda e:50<=e.atk<=100,list01):

for item in map(lambda e:(e.atk,e.name,),list01):
 print(item)
result=sorted()
re02