"""
装饰器
"""
def print_fun_name(func):
    print(say_hello.__name__)
def say_hello():
    print_fun_name(say_hello)
    print("hello")

def say_goodbey():
    print_fun_name(say_goodbey)
    print("goodbye")

# 需求：在两个方法实现的功能基础上，增加一种新功能（打印方法名称）
say_hello()
say_goodbey()