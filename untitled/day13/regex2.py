"""
match对象使用示例

"""
import  re
pattern=r"(ab)cd(?P<pig>ef)"
regex=re.compile(pattern)
obj = regex.search('abcdefghi')#match对象
#属性变量

print(obj.endpos)#目标字符串结尾位置
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)
#属性方法
print(obj.span())
print(obj.start())
print(obj.end())
print(obj.groupdict())#
print(obj.groups())#子组内容
print(obj.group('pig'))