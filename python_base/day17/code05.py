# 练习2: 改写MyRnage类



def MyRange(stop_value):
    start_value = 0
    while start_value < stop_value:
      yield start_value
      start_value += 1


# 循环一次  计算一次  返回一个
result=MyRange(5)
# 函数体包含yield语句，
# print(type(result))
# for i in result:
#   print(i)
# 练习1：  使用生成器函数，获取列表中所有偶数
# 将[34,4,5,34,37,52,65,32]
def get_even_number(list_target):
    for item in list_target:
        if item%2==0:
            # 返回一个数据，退出方法
            # return item
            yield item #返回多个数据，暂时离开方法
list01=[34,4,5,34,37,52,65,32]
re=get_even_number(list01)
for item in re:
    print(item)

for item in enumerate(list01):
    print(item)


def my_enumerate(list_taeget):
    for i in range(len(list_taeget)):
        yield (i,list_taeget[i])

re1=my_enumerate(list01)
for item in re1:
    print(item)



