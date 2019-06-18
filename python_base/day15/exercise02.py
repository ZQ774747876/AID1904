"""
练习：创建模块exercise02.py
     将double_list_helper.py粘贴到day15目录下
     在exercise02模块中，调用double_list_helper模块
     实现一下功能：
      1.获取00位置向右3个元素
      2.获取13位置想做2个元素
      3.获取22位置向上2个元素
      要求：分别使用是那种倒入方式实现
"""

# import double_list_helper
list01 = [
  ["00", "01", "02", "03"],
  ["10", "11", "12", "13"],
  ["20", "21", "22", "23"],
]
#
# pos=double_list_helper.Vector2(0,0)
# dir=double_list_helper.Vector2.get_right()
# target01=double_list_helper.get_elements(list01,pos,dir,3)
# print(target01)

from double_list_helper import *
pos=Vector2(0,0)
dir=Vector2.get_right()


re=get_elements(list01,pos,dir,3)
print(re)

# 练习2：
print(__name__)

