class Student:
   def __init__(self,name="",sex="",grade=0):
        self.name=name
        self.sex=sex
        self.grade=int(grade)
   def input_student_info(self):
        print(
            self.name,self.sex,self.grade)

# list_student=[]
# for i in range(3):
#     name=str(input("请输入名字:"))
#     sex=str(input('请输入性别:'))
#     grade=int(input("请输入成绩:"))
#     stu01=Student(name,sex,grade)
#     list_student.append(stu01)
#     stu01.input_student_info()
def find01(list_target):
    for item in list_target:
        if item.name=="张无忌":
            return item

def find02(list_target):
    result=[]
    for item in list_target:
        if item.grade>=60 and item.sex=="女":
            result.append(item)
    return result
def count_number(list_target):
    count=0
    for item in list_target:
        if item.grade>=60:
           count +=1
    return count

def get_most_grade(list_target):
    max_value=list_target[0]
    for i in range(1,len(list_target)):
      if max_value.grade <list_target[i].grade:
          max_value=list_target[i]
    return max_value

def del_list_student(list_target):
    count=0
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i].grade<60:
            del list_target[i]
            count +=1
    return count





list_student = [

    Student("赵敏", "女", 90),
    Student("周止诺", "女", 95),
    Student("张无忌", "男", 50),
    Student("小龙女", "女", 55),
    Student("杨过", "男", 85),

]
# re=find01(list_student)
# re.input_student_info()
# list01=find02(list_student)
# for i in list01:
#   i.input_student_info()

# print(count_number(list_student))
# stu02=get_most_grade(list_student)
# stu02.input_student_info()
