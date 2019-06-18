def fun03():
    print("exercise03")

from  package01.module01 import fun02
fun02()
import sys
sys.path.append("/home/tarena/1904/python_base/day16/project")
print(sys.path)