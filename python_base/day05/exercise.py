# import random
# list1=[]
# for red in range(1,8):
#     red=random.randint(1,33)
#     list1.append(red)
# blue=random.randint(1,17)
# list1.append(blue)


list01=[]
count = 1
i=0
while count<7:

       num01=int(input("请输入第%d个红球号码"%(count)))
       count +=1

       if num01>33 or num01<1:
           print("不在范围")
       else:
          list01.append(num01)


num02=input("请输入蓝球号码：")
list01.append(num02)
print(list01)
