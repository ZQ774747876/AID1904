"""
基本排序算法训练

"""
def bubble(list_):
# 外层循环表达比较多少轮0--->5
    for i in range(len(list_)-1):
# 内层循环把控比较次数5 4
        for j in range(len(list_)-1-i):
            if list_[j]>list_[j+1]:
                list_[j],list_[j+1]=list_[j+1],list_[j]
def select(list_):
    for i in range(len(list_)-1):
        min=i
        for j in range(i+1,len(list_)):
           if list_[min]>list_[j]:
               min=j
        if min!=i:
            list_[i],list_[min]=list_[min],list_[i]
def insert(list_):
    for i in range(1,len(list_)):
       x=list_[i]
       j=i-1


def sub_sort(list_,low,high):
#基准数
     x=list_[low]
     while list_[high]>x and high>low:
      high -=1
      list_[low]=list_[high]
     while list_[low]<x and low<high:
         low +=1
         list_[high]=list_[low]
     list_[low]=x
     return low

# 快排，low 第一个数序列号，high最后一个数序列号
def quick(list_,low,high):
    if low<high:
        key=sub_sort(list_,low,high)
        quick(list_,low,key-1)
        quick(list_,key+1,high)

list01=[1,3,6,4,2,8]
quick(list01,0,5)
print(list01)

