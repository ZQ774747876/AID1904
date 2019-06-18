#  day06复习
#  容器：存储一系列数据
#    字符串：存储字符，不可变
#  列表：存储变量，可变(预留空间)，序列（有序），灵活（索引，切片）
#  元组：存储变量，不可变(按需分配)
#  字典：存储键值对，可变，散列(无序)，读取速度快（利用空间换取时间），相比列表，可读性高

# -------------合并多个容器------------------
list01=[1,2]
print(id(list01))
list01 += [3,4]
print(id(list01))
print(list01)


tuple01=(1,2)
print(id(tuple01))
tuple01 +=(3,4)#创建新元素，替换tuple01地址
print(id(tuple01))#
print(tuple01)

dict01={"qtx":99}
dict02={"mz":23}
dict03={**dict01,**dict02}
print(dict03)