"""
buffer.py
"""
f=open('file','w')
while True:
 s=input("qingshurudanci:")
 f.write(s)
 f.flush()#经缓冲内容写入磁盘

close()
