class Vector:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return (self.x+other)
    def __sub__(self, other):
        return (self.x-other)
    def __mul__(self, other):
        return (self.x*other)
    def __truediv__(self, other):
        return (self.x/other)
    def __str__(self):
        return "zhishi%d"%(self.x)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    def __iadd__(self, other):
        self.x +=other
        return self
v1=Vector(1)

# r01=v1+2
# r02=v1+1
# # r03=v1*3
# re1=1-v1
# re3=3/v1
# print(r03)
print(id(v1))
print(v1.x)

