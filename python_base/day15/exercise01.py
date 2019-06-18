"""
多继承
"""
class A:
    def fun01(self):
        print("fun01===")
class B(A):
    def fun01(self):
        print("fun02===")
class C(A):
  def fun01(self):
      print("dsf")
class D(B,C):
  def fun01(self):
      print("sdhf")

