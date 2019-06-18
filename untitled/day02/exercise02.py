# 基于链式栈，完成一个逆波兰表达式的接口程序，只完成加法减法即可
from day02.lstack import *
s01=LStack()
while True:
    exp = input()
    tmp=exp.split(' ')
    for i in tmp:
        if  i not in ['+','-','p']:
            ls.push(float(i))
        elif i=='+':
          x=ls.pop()
          y=ls.pop()
          ls.
