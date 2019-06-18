day04作业
1.三合一
2.独立完成当天练习
3.在控制台获取一个整数作为边长
根据边长打印矩形
列如4
****
****
****
****
number=int(input("请输入整数："))
print("*"*number)
for i in range(number-2):
    print("*"+' '*(number-2)+"*")
print("*"*number)

4.在控制台上录入一个字符串，判断是否为回文
判断规则：正向和反向相同
上海自来水来自海上
str01=str(input("请输入字符串："))
if(str01[:]==str01[::-1]):
    print("是回文")
else:
    print("不是回文")
5.一个小球从100m高度落下
每次弹回源高度的一半
计算：总共弹起多少次（最小弹起高度为0.01m）
    总共走了多少米
count=0
height=100
sum=100
while (height/2 > 0.01):
    count +=1
    sum += height
    height /= 2

print(count)
print(sum)
6.阅读：python入门到实践第5章与第7章
