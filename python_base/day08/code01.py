"""

  函数：


"""

def fun01():
    print("fun01执行咯")
    #返回数据
    #退出方法
    return 100
    print("函数有蜘蛛侠你看就是 ")


result=fun01()
print(result)
#-----------------定义函数，两个数值相加---------------------
#分而治之
# 函数职责单一
def add(number_one,number_two):
    #获取数据

    result=number_one+number_two
    return result


#获取
number_one=int(input("请输入第一个数字："))
number_two=int(input("请输入第二个数字："))
add(number_one,number_two)
#显示结果
print("结果是："+str(result))


def input_time(hour,minute,second):
   return hour*3600+minute*60+second



print("结果是"+str(input_time(3,4,5)))


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_days_for_month(month,year):

 if month < 1 or month > 12:
  return "输入错误"
 if month == 2:
    # if is_leap_year(year):
    #     return 29
    # return 28
    return 29 if is_leap_year(year) else 28
 if month in (4,6,9,11):
  return "30天"
 return"31天"

# -----------------
# 练习：定义函数，获取指定范围内的素数
def get_prime(begin,end):
    list_result=[]
    for item in range(begin,end):
        for number in range(2,item):
            if item % number ==0:
                break
            else:
              list_result.append(number)
              return
#函数内存
def fun01(a):
 a=2
num01=500
fun01(num01)
print(num01)

# 在内存的方法区存储函数的字节码（方法体不执行）
def fun01(a):
 a=2
num01=500
# 调用函数,会在内存中开辟空间(栈帧),存储函数内定义的变量
fun01(num01)
# 函数执行完毕后,栈帧立即释放
print(num01)


# 定义函数,按照从小到大的方式排序列表
def arrange_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
 # return list_target

list01=[3,4,45,5,7,9]
print(arrange_order(list01))
#作用域
#   局部
#   全局

g01=400
def fun01():
    #局部作用域
    g01 =600#没有修改全局变量g01,而是创建了局部变量g01
    print(g01)
    l01=100
def fun02():
    #局部作用域
    print(g01)
    l01=200
def fun03():
    # 通过global语句,定义g01为全局变量
    global g01
    g01 =300#修改的是全局变量
g01=500
fun03()
fun01()
fun02()

# 统计 一个函数的执行次数
count=0
def state_number():
    global count
    count +=1
    pass
state_number()
state_number()

print(count)
# 函数参数
# 实际参数
def fun01(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
fun01(1,2)



def fun01(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
# 位置传参:实参与形参的位置依次对应
fun01(1,2,3,4)
# 序列传参:*将序列拆分后与形参位置依次对应
list01=[1,2,8,7]
fun01(*list01)
#关键字传参:实参与形参根据名称进行对应
fun01(b=1,c=2,d=3,a=4)
fun01(1,2,d=3,c=4)
# --字典传参:**将字典拆分后的形参的名字进行对应
dict01={"d":4,"c":3,"a":1,"b":2}
fun01(**dict01)

#练习:随意传递参数
#根据小时/分钟/秒,计算总秒数
def input_time(hour=0,minute=0,second=0):
   return hour*3600+minute*60+second
print(input_time(1,2,3))


# 星号元组形参:*让实参个数无限
def fun02(*a):
     print(a)

# 可以不传递参数
fun02()
#也可以传递多个参数
fun02(1,2)
# 练习:定义函数,数值想加的函数
def add_num(*args):
    sum=0
    for item in args:
        sum +=item
    return sum

print(add_num(1,2))
print(add_num(2,24,34,34))

# 位置形参+星号元组形参
def fun03(a,b,*args):
    print(a)
    print(b)
    print(args)

fun03(1,2)
fun03(1,2,344,5)

# 双星号字典形参:实参可以传递多个关键字参数
def fun66(**kwargs):
    print(**kwargs)
fun66(a=1,b=5,c=1)
# 万能传参
def fun07(*args,**kwargs):
   pass
fun07()

