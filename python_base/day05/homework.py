day05 作业：
1. 三合一
2. 当前练习独立完成.
3. 计算列表中最小值(不使用min)．

list01 = [3,45,56,6,7,2,8,9]
min_value =list01[0]
for index in range(1,len(list01)):
    if   min_value>list01[index]:
         min_value=list01[index]
print(min_value)
4. 彩票　双色球：
红球:7个，1 -- 33 之间的整数   不能重复
蓝球:１个，1 -- 17 之间的整数
(1) 随机产生一注彩票[7个红球１个蓝球].
import random

list_ticket=[]
# 7个不重复的红球
while len(list_ticket)<7:
 number=random.randint(1,33)
 if number not in list_ticket:
  list_ticket.append(number)
# 1个蓝球
list_ticket.append(random.randint(1,17))
print(list_ticket)
(2) 在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码："list_ticket =[]
list_ticket =[]

# 7个红球
while len(list_ticket)<7:
    number=int(input("请输入第%d个红球号码"%(len(list_ticket)+1)))
    if number <1 or number>33:
      print("号码不在范围")
    elif number in list_ticket:
      print("号码已经重复")
    else:
      list_ticket.append(number)
while True:
 number=int(input("请输入蓝球号码："))
 if 1<= number <= 17:
     list_ticket.append(number)
     break
 else:
     print("号码不在范围")
print(list_ticket)
# 7个红球
while len(list_ticket)<7:
    number=int(input("请输入第%个红球号码"%(len(list_ticket))))
    if number <1 or number>33:
      print("号码不在范围")
    elif number in list_ticket:
      print("号码已经重复")
    else:
      list_ticket.append(number)
while True:
 number=int(input("请输入蓝球号码："))
 if 1<= number <= 17:
     list_ticket.append(number)
     break
 else:
     print("号码不在范围")

5. 阅读python入门到实践第３章和第４章
