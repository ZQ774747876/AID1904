list02=["张无忌","赵敏","周知诺"]
list03=[101,102,103]
# for  item in zip(list02,list03):
#     print(item)


def my_zip(list_target01,list_target_02):
    for i  in range(len(list_target01)):
      yield (list_target01[i],list_target_02[i])


for item in my_zip(list02,list03):
    print(item)

zip()