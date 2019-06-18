class Person:
  def __init__(self,name):
   self.name=name

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self,value):
    self.__name=value
  def teach(self,):




p01=Person("张无忌")
p02=Person("赵敏")





