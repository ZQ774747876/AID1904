"""
练习1：
"""


def check_limit(func):
   def wrapper(*args,**kwargs):
     print("验证您的身份")
     return  func(*args,**kwargs)
   return wrapper()

@check_limit
def enter_background():
    print("进入后台系统")

@check_limit
def delete_order():
    print("删除订单")

