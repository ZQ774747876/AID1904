"""
基于fork的进程创建演示
"""
import sys
import os
print("============")
a=1
pid = os.fork()
if pid<0:
    print("error")
elif pid==0:
    print("child pid",os.getpid())
    print("get  parent PID:",os.getppid())
    sys.exit("退出进程")
else:
    print("get child PID:",pid)
    print("parent pid:",os.getpid())
print("ALL A=",a)
