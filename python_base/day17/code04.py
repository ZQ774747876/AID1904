# for i in range(5):
#     print(i)


class MyRangeiterator:
    def __init__(self,target):
        self.target=target
        self.index=0
    def __next__(self):
       if self.index>=self.target:
           raise StopIteration
       result=self.index
       self.index +=1
       return result




class MyRange:
    def __init__(self,num):
        self.num=num

    def __iter__(self):
         return MyRangeiterator(self.num)

for i in MyRange(99999999999):
    print(i)