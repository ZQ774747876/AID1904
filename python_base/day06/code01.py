# 1.创建元组
# --空元祖
t01=()
t01=tuple()
# --具有默认值的元素
t01=(1,"a")
# 列表：预留空间
# 元祖：按需分配
t01=tuple([1,2,3,4,5])
# t02=(1) 此时为整数1,，并非元素1
t02=(1,)
t03=1,2,3,4 #创建元祖时，可以省略小括号
list01 =list(t01)
print(list01)

# 2.获取切片/索引获取元素
print(t03[:2])
print(t03[2])

# 3.获取所有元素
for index in :
    print(t03[index])

# 在控制台中录入月。日，计算这是这一年的第几天。
# 例如：3月6日 1月天数+2月天数+6
# 方法1
day_of_month=(31,28,31,30,31,30,31,31,30,31,30,31)
month=int(input("请输入月："))
date=int(input("请输入日："))
sum1=date
for item in day_of_month[:month-1]:
    sum += item
print("总计有%d天"%sum1)

# 方法2
day_of_month=(31,28,31,30,31,30,31,31,30,31,30,31)
month=int(input("请输入月："))
date=int(input("请输入日："))
sum1=date
sum1+=sum(day_of_month[:month-1])
print("总计有%d天"%sum1)

# 字典
# 空字典
dict01={}
dict01=dict()
# 具有默认值的字典
dict={"ze":65,"yl":80,"mz":80}
print(dict)
# 添加
dict01["qtx"]=100
print(dict01)
# 获取
# 如果查找不存在的key，列异常
if "xx" in dict01：
    print(dict01[["xx"]])
#4.修改(存在key)
dict01["zc"]=90
print(dict01)
#5.删除
if "xx" in dict01:
 del dict01["zc"]
 print(dict01)
# 6.遍历
# 得到的是键值中的元组
for key,value in dict01:
    print(key)
    print(value)

# 练习 输入季度，在控制台输出月份
dict01={"春":(1,2,3),
        "夏":(4,5,6),
        "秋":(7,8,9),
        "冬":(10,11,12)
        }
season=str(input("请输入季度："))
if season in dict01:
 print(dict01[season])
else:
    print('输入错误')

# 在控制台中录入多个学生信息（姓名，性别，成绩，年龄）
# 如果姓名输入esc，则停止录入
# 运行打印所有学生信息
dict_student_info={}
while True:
   name=input("请输入姓名：")
   if name =="esc":
       break
   else:
      sex=input("请输入性别：")
      score=float(input("请输入成绩："))
      age=int(input("请输入年龄："))
      dict_student_info[name]=[sex,score,age]
for key,value in dict_student_info.items():
       print("%s的性别是%s，成绩是%d，年龄是%d"%(key,value[0],value[1],value[2]))
# 序列：有序 灵活（索引/切片）
# 散列：无序 速度快，可读性更高

# 创建调查问卷：
# 请输入姓名：（esc结束）
# 请输入您的喜好：（esc结束）
# 调查结束后，运行显示所有信息