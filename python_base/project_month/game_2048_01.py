"""
  2048 游戏核心算法

"""
# 定义函数,将列表中的0元素移至末尾
# [2,0,2,0]-->[2,2,0,0]
# [2,0,0,2]-->[2,2,0,0]
# [2,4,0,2]-->[2,4,2,0]
def move_end(list01):
    # 除掉0元素,再末尾增加
    for i in range(len(list01)-1,-1,-1):
       if list01[i]==0:
        del list01[i]
        list01.append(0)
# _-------测试--------------------
# list01=[2,0,2,0]
# move_end(list01)
# print(list01)
# 2.定义函数,合并列表中的相同元素
def merge(list01):
    # x
 move_end(list01)
#     如果相邻且相同
 for i in range(len(list01)-1):
     if list01[i]== list01[i+1]:
         list01[i]+=list01[i+1]
         del list01[i+1]
         list01.append(0)

"""
3.定义函数,向左移动二维列表
[ 
  [2,2,0,2]
  [0,2,0,4]
  [2,0,4,2]
  [0,4,2,2]
]

"""
def move_left(map):
#  将每行(二位列表的每个元素)传递给合并函数
  for row in  map:
    merge(row)
double_list=[
  [2,2,0,2],
  [0,2,0,4],
  [2,0,4,2],
  [0,4,2,2],

]

def move_right(map):
    # 将每行(从右向左获取行数据)传递给合并函数
    for row in map:
        list_marge=map[row][::-1]
        # map[0][::-1]从右向左获取行数据(新列表)
        merge(list_marge)
        # 将合并后的结果,从右向左获还给二维列表
        map[row][::-1]=list_marge
double_list=[
  [2,2,0,2],
  [0,2,0,4],
  [2,0,4,2],
  [0,4,2,2],

]
# move_right(double_list)
# print(double_list)

#    -- 左移动/右移动 内存图
def move_up(map):
#     00 10 20 30
 list_merge=[]
 for r in  range(4):
    list.merge.append(map[r][0])
 merge(list_merge)
 for c in range(4):
     map[r][c]=list_merge[r]
move_up(double_list)
print(double_list)
#    -- (扩展)完成上移动/下移动.
def move_down(map):
# 30 20 10 00

 for c in range(4):
  list_merge = []
  for r in range(3,-1,-1):
   list_merge.append(map[r][0])
   merge(list_merge)
 # 从左到右赋值给二维列表(从下到上)
  for r in range(3,-1,-1):
     map[r][c]=list_merge[3-r]
