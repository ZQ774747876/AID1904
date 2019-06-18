"""练习：提取一段文字中所有的日期（2019-05-23）
        将日期打印出来，打印格式为2019/05/23
"""
import  re
print(re.search(r'dog','cat is catch dog').group())
print(re.match(r'dog','cat is catch dog'))
list01=[1,2,3,4]
list01[1:2]=[1,]
print(list01)
for i in range(4,0,-1):
    print(i)
list02=[1,'dfs',3,'四']
list03=[1,'dfs',3,'四']
print('3' in list02)
print(id(list02))
print(id(list03))
list02[0:1]=['a','b']
print(list02)
print(id(list02))