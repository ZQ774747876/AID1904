# 字典推导式

# 1 2 3 4 5 6 7 8 9 10--》 数：平方
dict={}
for item in range(1,10):
    dict[item]=item**2
print(dict)

dict02={item:item**2 for  item in range(1,10)}
print(dict02)

# 练习1.["张无忌",”赵敏“,”周芷若“]...字符串的长度
list01=["张无忌","赵敏周","芷若"]
dict01={key:len(key)  for key in list01}

print(dict01)

# ["张无忌",”赵敏“,”周芷若“]
#[101,102,103]
# 将人与房间号合并为字典
list01= ["张无忌","赵敏","周芷若"]
list02=[101,102,103]
dict01={}
for index in range(len(list01)):
    dict01[list01[index]]=list02[index]
dict02={list01[i]:list02[i] for i in range(len(list01))}
print(dict01)
print(dict02)

# 需求：根据值找键
# 解决：交换键盘：键-->值 值-->键
dict03={value:key for key,value in dict02.items()}
print(dict03)
# 缺点：容易丢失数据（值如相同，反过来作为键你会丢失


# 集合
# 作用：不重复 数学运算
# 空
s01=set()
# 具有默认值
s01={"a","b"}
s01=set("abcdefg")
# 添加
s01.add("A")
print(s01)
# 删除
print(s01)
s01.remove("b")
print(s01)
# 定位元素
lsit01=list(s01)
# 遍历
# 数字运算
s02={1,2,3}
s03={2,3,4}
# 交集
print(s02 & s03)# {2,3}
# 并集
print(s02|s03)#{1,2,3,4}
# 补集
print(s02^s03)
print(s02-s03)#{1}
print(s03-s02)#{4}

# 子集   超集
s04={1,2}
print(s04<s02)
print(s02>s04)

#固定集合
f01=frozenset("dsjf")
print(f01)

# 练习1：
# 在控制台中随意输入字符串
# 按下esc则停止，然后打印所有不重复字符串
s01=set()
while True:
 str_input=str(input('请输入字符串：'))
 if str_input=="esc":
     break
 else:
   s01.add(str_input)
print(s01)


# 练习2：
# 经理：曹操，刘备，孙权
# 技术员：曹操，刘备，张飞，关羽
# 1.是经理也是技术员的有谁
# 2.是经理，不是技术员的有谁
# 3.是技术员，不是经理的有谁
# 4.张飞是经理吗？
# 5.身兼一致的都有谁？
# 6.经理和技术员共有多少人
s01={"曹操","刘备","孙权"}
s02={"曹操","刘备","张飞","关羽"}
print("是经理也是技术员的有：%s"%(s01&s02))
print("技术员，不是经理的有:%s"%(s02-s01))
print("是经理,不是技术员的有：%s"%(s01-s02))

print("张飞" in s01)
print(s01^s02)
print(len(s01|s02))

# for for
# 外层循环控制行
for r in range(3):
 #内层循环控制列
 for c in range(5):#012
   if c==0 or c==2 or c==4:
    print("*",end="")
   else:
    print("#",end="")
 print()#换行

# [3,4,45,5,7,9]
# 从小到大排序
# 重点：列表中的元素两两比较
# 思想吧：
# 拿第一个元素，与后面元素进行比较
# 那第二个元素，与后面元素进行比较
# 拿第三个元素，与后面元素进行比较
# ’‘’‘
# 拿（倒数第二个元素）
# 发现后面的元素更小
# 交换两个元素（拿的 更小）
list01=[3,4,45,5,7,9]
#外层循环：拿出数据
for r in range(len(list01)-1):
#内层循环： 与后面作比较
   for c in range(r+1,len(list01)):#1-->5 2-->6
       if list01[r]>list01[c]:
           list01[r],list01[c]=list01[c],list01[r]
print(list01)


#练习：判断列表中 是否具有相同元素
# 思路：列表中所有元素两两比较，发现相同元素，记得到结论
#       所有元素比较后，。没有发现元素记得到结论
# [3,4,45,5,7,5]
list01=[3,4,45,5,7,5]
# 假设没有相同元素
result=False
for r in range(len(list01)-1):
 for c in  range(r+1,len(list01)):
   if list01[r] == list01[c]:
           print("you ")
           result=True
   #  后续循环不在执行
          break    #跳出内层循环
 if result:
  break

if not result:
    print("没有相同元素")


# 函数
# 做功能
def attack():

 print("百拳")
 print("勾拳")
 print("侧踹")

# 用功能
attack()
# 用功能
attack()
# 用功能
attack()

# 练习：将下列代码，定义在函数中，并调用函数，绘制三角形

