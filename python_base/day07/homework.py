day07作业
1. 三合一
2. 独立完成练习
3. 定义在控制台中打印矩形的函数
    for r in range(2):  # 0          1
      # 内层循环控制列
      for c in range(3):  # 012     012
        print("*", end=" ")
      print()  # 换行
4. 定义在控制台中打印二维列表的函数
二维列表：
[
    [2,4,0,8,"a"],
    [0,2,4],
    [4,0],
    [0,2,2,0],
]
打印结果：
2   4   0  8   a
0   2   4
4   0
0   2   2  0

5. (扩展)将2 -- 100之间的素数存入列表（不用做成函数）.
素数：　只能被１和自身整除的数字
算法：判断从2开始到当前数字之间，是否存在可以被整除的数．
　　　如果存在则不是素数，如果不存在是素数
例如：2  3   5    7  8  9
 　　　6　能被2  整除
 　　　8　能被2  整除
      9 能被3  整除
list_result=[]
for item in  range(2,101):
    for number in  range(2,item):
     if item%number ==0:
         break
    else:
        list_result.append(item)
print(list_result)

6. 阅读程序员的数学,第5章