
#形参
#默认参数:如果不传递参数,可以使用默认值代替


def fun02(a=0,b=0,c=0,d=0):
    print(a)
    print(b)
    print(c)
    print(d)

#关键字传参b
#可以选择性的为形参赋值
fun02(b=2)#给参数b赋值
fun02(5)#给参数a赋值

def input_time(hour,minute,second):
   return hour*3600+minute*60+second