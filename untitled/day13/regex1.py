"""
regex1 示例
"""
import  re
s="2019年，键国70年"
#完全匹配
m=re.fullmatch(r'\w+','jame1')
print(m)

#匹配开始位置
m=re.match(r"[A-Z]\w*",'Hello word')
print(m)

#匹配目标字符串第一处符合的内容
m1=re.search(r"[A-Z]\w*",'Hello word')
print(m)