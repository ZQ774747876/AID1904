class Cars:
    def __init__(self,brand,model,price):
        self.brand=str(brand)
        self.model=str(model)
        self.price=int(price)
class ElectricCars(Cars):
    def __init__(self,battery_capacity,charge_power,brand,model,price):
        self.battery_capacity=int(battery_capacity)
        self.charge_power=int(charge_power)
        # 调用父类构造函数
        super().__init__(brand,model,price)
e01=ElectricCars(10,10,"比亚迪",'秦',200000)
print(e01.battery_capacity)
print(e01.price)
# 定义父类：动物（数据：姓名，年龄）
# 定义子类：狗（数据：爱称）
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Dogs(Animal):
    def __init__(self,pet_name,name,age):
        self.pet_name=pet_name
        super().__init__(name,age)

dog01=Dogs("小i","SHA",2)
print(dog01.pet_name)