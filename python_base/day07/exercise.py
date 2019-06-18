import random
wins ={
    "石头":"箭头",
    "剪刀":"布",
    "布":"石头"
    }

dict_items=["剪刀","布","石头"]
random_number=random.randint(0,2)
str_sys_inpout=dict_items[random_number]
str_use_inpout=input("请输入：")
if str_sys_inpout==str_use_inpout:
    print("平局")
elif wins[str_use_inpout]==str_sys_inpout:
    print("胜利")
else:
    print("失败")