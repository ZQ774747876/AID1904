



# for 变量 in 可迭代对象
#  语句

for item in "我爱python":
    print(item)


# while 循环对折5次
thickness = 0.0001
count = 0
while count<5:
    thickness *= 2
    count += 1
print(thickness)

# for 循环对折5次
thickness =0.0001
for count in range(5);
    thickness += 2
print(thickness)


# 练习1: 累加1--100之间整数
sum = 0
for item in range(1,101):
    print(item)
    sum += item
print(sum)
# 练习2: 累加5--58之间的整数
sum = 0
for item in  range(5,59):
    sum += item;
print(sum)
# 练习3: 累加6--20之间偶数
sum =0
for item in range(6,21,2):
    sum +=item
print(sum)
# 练习4: 累加10--50之间个位是2 5 9 的整数
sum = 0
for item in range(10,51):
    unit = item % 10
    if unit ==2 or unit ==5 or unit ==9:
        sum+=item
    sum += item
print(sum)

# 练习:随机加法考试
# 随机产生两个数字,在控制台中获取两个数字想家的结果
#
import random
score = 0
for item in range(3):
    random_number01=random.randint(1,10)
    random_number02=random.randint(1,10)
    result_input = int(input("请计算"+str(random_number01)+"+"+str(random_number02)+"="))
    if result_input == random_number01 + random_number02:
        score += 10
    else:
        score -= 5


print(score)

# 练习1 :在控制台上.获取一个字符串
#  打印每个字符的编码值
string=str(input("请输入一个字符串："))
for item in  string:
    print(ord(item))

#  练习2:在控制台中，重复录入一个编码值，打印字符
# 如果没有输入编码值，而直接回车，则退出循环
while True:
    str_code =input("请输入编码值：")
    if str_code =="":
       break
    print(chr(int(str_code))),

# str 字面值
#  双引号
name01 = "苏大强"
#  单引号
name02 ='苏大强'
#  三引号:可见即所得
name03 ='''苏大强'''
name03 ="""苏大强"""

# 练习1：格式化字符串
# 在控制台中按照如下格式输出：图形的面积是52.5，周长是35.25.
# 其中图形是变量，面积与周长的值是变量
graph="图形"
area =52.5
length = 35.25
msg = "%s的面积是%.1f，周长是%.2f"%(graph,area,length)
print(msg)

# 练习：在控制台中显示120秒的倒计时。02:00 --> 01:59-->....-->00:00
for second in range(120,-1,-1):
    print("%02d:%02d" % (second/60,second%60))

# 索引
str02 ="我叫苏大强"
print(str02[1])#叫
print(str02[-1])#强

# 切片
print(str02[0:3])
#
print(str02[2:5])
print(str02[:3])
print(str02[2:])
print(str02[:])

# 练习：在控制台中获取一个字符串
# 打印第一个字符
#  打印最后一个字符
#  如果长度是技术，打印中间的字符
#  打印倒数3个字符
#  倒叙打印字符串


