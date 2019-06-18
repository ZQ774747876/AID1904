day10 作业
1.三合一
2.当天练习独立完成(2048除外)
3.定义学生类,具有(姓名,性别,成绩)数据,
           具有打印个人信息的行为.
class Student:
    def __init__(self,name,sex,grade):
        self.name=str(name)
        self.sex=str(sex)
        self.grade=int(grade)

    def input_student_info(self):
        print(self.name,self.sex,self.grade)
  定义函数,在学生列表中,查找姓名是"张无忌"的学生对象.
def find01(list_target):
     for item in list_target:
        if item.name=="张无忌":
            return item
  定义函数,在学生列表中,查找成绩大于60的所有女同学对象.
def find02(list_target):
    result=[]
    for item in list_target:
        if item.grade>=60 and item.sex=="女":
            result.append(item)
    return result
  定义函数,计算成绩大于等于60的所有同学数量.
def count_number(list_target):
    result=[]
    count=0
    for item in list_target:
        if item.grade>=60:
           count +=1
    return count
  定义函数,获取最高分的学生对象.
def get_most_grade(list_target):
    max_value=list_target[0]
    for i in range(1,len(list_target)):
      if max_value.grade <list_target[i].grade:
          max_value=list_target[i]
    return max_value
  定义函数,删除所有成绩低于60分的学生对象.
def del_list_student(list_target):
    count=0
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i].grade<60:
            del list_target[i]
            count +=1
    return count
4.(扩展)
    定义函数,获取二维列表,某个位置元素的某个方向,的指定个数的所有元素.
    例如:获取下列二维列表,21位置元素,向右,3
     结果: 22   23  24
    """
      00   01   02   03  04
      10   11   12   13  14
      20   21   22   23  24
    """
def get_elements(target,vect_pos,vect_dir,count):
    result=[]
    for i in range(count):
        # 改变位置:原位置+方向
        vect_pos.x +=vect_dir.x
        vect_pos.y +=vect_pos.y
        result.append(target[vect_pos.x][vect_pos.y])
    return result