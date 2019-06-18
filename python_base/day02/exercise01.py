number01 = input("请输入第一个变量：")
number02 = input("请输入第二个变量：")
# 借助第三个变量进行交换(跨语言的终端思想)
# temp = number01
# number01=number02
# number02 = temp

# 直接交换(python 独特的方式)
number01,number02 = number02, number01

print("第一个变量为"+number01)
print("第二个变量为"+number02)