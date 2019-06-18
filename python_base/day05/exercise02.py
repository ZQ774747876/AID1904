
list_name=[]
while True:
    name=str(input("请录入学生的姓名："))

    if name == "esc":
        break
    # 如果存在，则跳过本次循环
    if name in list_name:
        continue
    list_name.append(name)
 for i in range(len(name)):
     print(i)


