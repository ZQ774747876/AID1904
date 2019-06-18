"""
迭代器
"""
class EmployeeIterator:
    def __int__(self,target):
      self.__target=target
      self.__index=0
    def __next__(self):
        if self.__index>len(self.__target)-1:
         raise StopIteration
        result=self.__target[self.__index]
        self.__index +=1
        return result

class employee:
    pass


class EmployeeManager:
    def __int__(self):
        self.__list_emp = []

    def add_employee(self,emp):
        self.__list_emp.append(emp)

    def __iter__(self):
        return EmployeeIterator(self.__list_emp)

manager=EmployeeManager()
manager.add_employee(employee())


iterator=manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
