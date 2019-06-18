"""

seek,py文件偏移演示
"""
#文件偏移量在开头
import os
f=open('file01','wb+')
print(f.fileno())
f.write(b"world\n")
f.flush()
f.write(b'fdsfasds')
print(f.tell())
f.seek(-10,2)
print(f.read())
# print(os.path.getsize('file'))
# print(os.listdir('..'))
# print(os.path.exists('file'))
# print(os.path.isfile('dsfs'))
os.remove('file04')