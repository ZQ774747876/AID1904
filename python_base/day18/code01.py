"""
生成器表达式
"""
list01=[4,4,5,67,5,78]
result01=[item for item in list01 if item>5]
for item in result01:
    print(item)

result01=(item for item in list01 if item>5)
for item in result01:
    print(item)