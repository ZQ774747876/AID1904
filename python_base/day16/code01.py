"""
  标准库模块
       ---时间
"""
# import time
# # 1558401660.9481585
# # 1558401685.9869597
# # 时间戳：从1970年后经过的秒数
# print(time.time())
# # 时间戳--->时间元组
# # 年/月/日 小时：分钟：秒
# tuple_time=time.localtime(1558401685.9869597)
# print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))
# # str-->时间元组
# print(time.strptime("2019/05/21 09:21:25","%Y/%m/%d %H:%M:%S"))
# # 时间元组-->时间戳
# print(time.mktime(tuple_time))

# 练习1：定义函数，根据年月日，返回星期数
# 星期一 星期二 ....星期日
# import time
# def return_week(year,month,day):
#      tupel01=time.strptime("%d-%d-%d","%y/%M/%d"%(year,month,day))
#      # return  tupel01[6]
#      dict_weeks={
#          0:"星期一",
#          1: "星期二",
#          2:"星期三",
#          3:"星期四",
#          4:"星期五",
#          5:"星期六",
#          6: "星期天",
#                }
#      return dict_weeks[tupel01[6]]
# print(return_week(2019,5,21))


import  time
def life_days(year,month,day):
    tuple_time=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    life_second=time.mktime(tuple_time)-time.time()
    return  life_second/60/60/24

print(life_days(1994,11,5))