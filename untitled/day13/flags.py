"""
flags扩展功能展示
"""
import re
s="""Hello 
北京
"""
#regex=re.compile(r'\w+',flags=re.ASCII)


#
#regex=re.compile(r'[a-z]+',flags=re.I)

#regex=re.compile(r'.+',flags=re.S)
regex=re.compile(r'^北京',flags=re.M)
l=regex.findall(s)
print(l)