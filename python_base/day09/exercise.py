"""
练习:
定义类:具体事物,抽象化的过程
创建对象:抽象事物,具体化的过程
定义汽车类,数据(品牌,型号,价格),行为(启动,行驶)
    创建至少2个对象
"""
class Car:
    # 两个下划线开头,两个下划线结尾
    def __init__(self,brand,model,price=1000000):
        # self 是调用当前方法的对象地址
        self.brand=brand
        self.model=model
        self.price=price
    def action01(self):
        print(self.brand+"启动")
    def action02(self):
        print(self.brand+"行驶")
# 创建对象,调用_
car01=Car("奔驰","S300",)
# 自动传递对象地址到start方法,作为第一个参数
car01.action01()
car01.action02()
# 所有的方法被对象共享
car02=Car("BMW","X6",)
car02.action01()
car02.action02()
