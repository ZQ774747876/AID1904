  # 1.创建空列表
   ，
  .list01 = []
  list01 = list()
00

  # --创建具有默认元素的列表
list01 = [2,大强，True]


#练习：在控制台中录入学生中的学生成绩
#  “请输入学生总数：”
#  “请录入第1个学生成绩
# 获取总分 获取最高分 获取最低分
/
075                               0
number01=int(input("请输入学生总数："))
list_student_score=[]
for i in range(number01):
    score=float(input("请输入第%d个学生的成绩"%(i+1)))
    list_student_score.append(score)
print("总分是:%.1f"%sum(list_student_score))
print("最高分是:%.1f"%max(list_student_score))
print("最低分是:%.1f"%min(list_student_score))

# 内存图
# list01 是变量，存储列表对象的地址
# 列表引用
list01 = ["张无忌","赵敏","周知诺"]
# list02 得到的是列表对象地址
list02 = list01
# 修改的是列表第一个元素存储的对象地址
list01[0]="老张"
print(list02[0])



list01=["张无忌","赵敏","周芷若"]
list02=list01
# 修改的是变量存储的对象地址
list01="老张"
print(list02[0])

list01=["张无忌","赵敏","周芷若"]
# 通过切片复制列表（拷贝了列表中的变量，而没有变量
list02=list01[:]
list01[0]="老张"
print(list02[0])

list01=["张无忌",["赵敏","周芷若"]]
list02=list01
# 修改列表第二个元素的第二个元素
list01[1][1]="止若"
print(list02[1][1])

list01=["张无忌",["赵敏","周芷若"]]
list02=list01.copy() #浅拷贝
list01[1][1]="止若"
print(list02[1][1]) #止若

import copy
list01=["张无忌",["赵敏","周芷若"]]
list02=copy.deepcopy(list01)#深拷贝
list01[1][1]="止若"
print(list02[1][1])

# 练习：在控制台中录入多个学生的姓名
#  如果有重复的姓名，不存入列表
# 如果输入esc，则停止录入，在每行打印学生姓名


# 练习1：将list_score列表中大于60的元素存入list01中
list_score =[60,85,35,26,20,90]
list01=[]
for i in range(len(list_score)):
    if (list_score[i]>60):
         list01.append(list_score[i])
print(list01)

# 练习2：获取list_score列表中最大值（不使用max）
list_score =[60,85,35,26,20,90]
max_value=list_score[0]
for i in range(1,len(list_score)):
    if max_value<list_score[i]:
        max_value=list_score[i]
print(max_value)
list_score =[60,85,35,26,20,90]

# 需求：大量某些逻辑，拼接字符串
# 0123456789
str_result =""
for item in range(9):
    # 缺点：每次+都会产生新的字符串对象
   # 替换str_result变量存储的地址，行之间

    list_result = []
    for item in range(10):
        # 向列表追加字符（不会每次产生新对象，造成垃圾）
        list_result.append(str(item))
    # list --> str
    str_result = "".join(list_result)
    print(str_result)
    list_result=[]for item in range(10):    # 向列表追加字符（不会每次产生新对象，造成垃圾）    list_result.append(str(item))# list --> strstr_result="".join(list_result)print(str_result)/


# 练习：在控制台中重复录入字符串，知道输入esc为止
# 最后打印拼接后的字符串
  str_result = []
  while True:
      str_input = input("请录入字符串：")
      if str_input == "esc":
          break
      str_result.append(str_input)
  str_result01 = "".join(str_result)
  print(str_result01)

  # 字符串 --> 列表
str01= "张无忌.赵敏周.芷若"
list_result =str01.split(".")
print(list_result)

# 英文单词反转
# "How are you" -->"you are How"
str01="How are you"
list_result01 =str01.split(" ")
list_result02=list_result01[::-1]
str02=" ".join(list_result02)
print(str02)


# 传统写法
list01 =[4,5,66,7,8,9]
list02=[]
for item in list01:
    if item<10:
        list02.append(item**2)
print(list02)

# 推导式写法
list03 =[item** 2 for item in list01 if item<10]
print(list03)


# 练习:将list01中的所有元素的个位存入list02中
list01 =[56,36,69,44,868]
# 传统写法
list01 =[56,36,69,44,868]
list02=[]
for item in list01:
    list02.append(item % 10)
print(list02)
# 推导式写法
list03=[item%10 for item in list01]
print(list03)
