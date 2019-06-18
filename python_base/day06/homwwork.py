day06 作业
1. 三合一
2. 当天练习独立完成
3. 将1970年到2050年中的闰年，存入列表．
lsit_result =[]
for item in range(1970,2051):
    if item%4==0 and item%100 !=0 or item%400==0:
         print("")
4. (1)存储多个商品信息,在控制台中显示出来.
   屠龙刀,10000元
   倚天剑,10000元
   打狗棒,5000元
   ...
# 可以最为快速的定位某一个商品
dict01={"屠龙刀":10000,
        "倚天剑":10000,
        "打狗棒":5000
        }
for key,value in dict01.items():
    print("商品名称是%s，单价为：%d" %(key,value) )

   (2)存储全国各个城市的景区与美食,在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头.
dict03={
    "北京":{
{"景区":["故宫","天安门","天坛"]},
{"美食": ["烤鸭","炸酱面","豆汁","卤煮."]}
    },
    "四川":{
        "景区":["九寨沟","峨眉山","春熙路．"],
        "美食":["火锅","串串香","兔头"]
            }
}
# 获取北京的美食
print(dict03[["北京"]["美食"]])
for city,info in dict03.items()
    print(city)


5. 计算一个字符串中的字符以及出现的次数.
abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
# 逐一判断字符出现的次数
# 将每个字符以及出现的次数存入一个容器（字符：出现次数。。。）

str_input=str(input("请输入字符串："))
dict_result={}
for item in str_input:
    if item not in dict_result:
      dict_result[item]=1
    else:
      dict_result[item] +=1
print(dict_result)


6.(扩展)猜拳游戏:石头剪刀布
系统随机选择一个
用户输入一个
判断输赢

提示：将胜利策略存入容器
石头 战胜　剪刀
剪刀　　　　布
布        石头
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
    print("pingju")
elif wins[str_use_inpout]==str_sys_inpout:
    print("shuengli")
else:
    print("shibai")


7.阅读python入门到实践第６章