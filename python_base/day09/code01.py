"""
  类和对象
"""
class wife:
    "老婆"
    def __init__ (self,name,age):
     self.name=name
     self.age=age
    def play(self):
      print(self.name+"打游戏")

   # 对象
w01=wife("丽丽",23)
w02=wife("莹莹",25)
w01.play()
w02.play()
