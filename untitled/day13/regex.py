"""
regex
"""
import re
s='Alex:1994,Sunny:1993,fdsf:555'
pattern=r'\w+:\d+'
#re模块调用findall
l=re.findall(pattern,s)

print(l)

#按照匹配内容切割字符串
l=re.split(r'[:,]',s)
print(l)

#替换匹配到的内容
s=re.subn(r'\s+','#',"This is a test",1)
print(s)

#使用compile对象调用
regex=re.compile(pattern)
l=regex.findall(s,0,10)
print(l)