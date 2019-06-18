day09 作业
1. 三合一
2. 当前练习独立完成
3. 2048核心算法
   -- 左移动/右移动 内存图
   -- (扩展)完成上移动/下移动.
4. 画出code01.py代码内存图
5. 创建狗类,具有姓名.体重等数据
   具有坐,吃,导盲等方法
   创建至少2对象.
   画出代码内存图.
class Dogs:
    def __init__(self,name,weight):
        self.name=str(name)
        self.weight=int(weight)
    def dog_sit(self):
        print(self.name+"坐下了")
    def dog_eat(self):
        print(self.name+"正在吃")
    def dog_navigation(self):
        print(self.name+"狗正在导航")
dog01=Dogs("小白",25)
dog02=Dogs("小新",15)
dog01.dog_sit()
dog01.dog_eat()
dog01.dog_navigation()
dog02.dog_eat()
dog02.dog_sit()
dog02.dog_navigation()
6. 以万物皆对象的思想,洞察身边存在客观事物.
   自行创建2个类,2个对象.
    核心:体会将现实事物抽象化的过程.
            从抽象到具体化的过程.
class Computer:
 def __init__(self,brand,production_date,inch):
        self.brand=str(brand)
        self.production_date=str(production_date)
        self.inch=int(inch)
 def computer_open(self):
         print(self.brand+"开机了")
         print("它的出产日期是"+self.production_date)
         print("它的尺寸是"+str(self.inch))
 def computer_close(self):
        print(self.brand+"关机了")

computer01=Computer("DELL","1994-01-05",13)
computer02=Computer("lenove","2001--02-10",15)
computer01.computer_open()
computer01.computer_close()
computer02.computer_open()
computer02.computer_close()