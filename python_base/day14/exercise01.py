class StaffManager:
    def __init__(self):
        self.__staffs=[]
    def add_staff(self,staff):
        self.__staffs.append(staff)
    def calculate_total_sarally(self):
        total_sarally=0
        for item in self.__staffs:
            total_sarally += item.calculate_sarally()
        return total_sarally
class Staffs():
    def __init__(self,basic_salarry):
        self.basic_salarry=basic_salarry
    def calculate_sarally(self):
        return self.basic_salarry

class GeneralStaff(Staffs):
    def __int__(self,basic_salarry):
        self.basic_salarry=int(basic_salarry)
    def calculate_sarally(self):
        return self.basic_salarry
class Programmer(Staffs):

    def __init__(self,bonus,basic_salarry):
        self.bonus=bonus
        super().__init__(basic_salarry)
    def calculate_sarally(self):
       return self.basic_salarry+self.bonus
class  Saleman(Staffs):
    def __init__(self,basic_salarry,sales):
        self.sales=sales
        super().__init__(basic_salarry)
    def calculate_sarally(self):
       return self.basic_salarry+self.sales

s01=StaffManager()
s01.add_staff(Programmer(8000,1000))
s01.add_staff(Saleman(1800,2000))
s01.add_staff(GeneralStaff(5000))
result=s01.calculate_total_sarally()
print(result)