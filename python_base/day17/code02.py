# list01=[1,2,2,3,4,56,7,56]
# iteror=list01.__iter__()
# while True:
#     try:
#         item=iteror.__next__()
#         print(item)
#     except StopIteration:#迭代完成
#         break

# 练习1：（4,4,54,55,414,41,41）通过迭代器获取元组元素
# 练习2：{“张无忌”：3 ,"赵敏":2}通过迭代器，获取字典记录
# tuple01=(4,4,54,55,414,41,41)
# iteror01=tuple01.__iter__()
# while True:
#     try:
#         item=iteror01.__next__()
#         print(item)
#     except StopIteration:
#         break
dict01={"张无忌":3,
         "赵敏":2
        }
iteror02=dict01.__iter__()
while True:
        try:
            item01=iteror02.__next__()
            print(item01,dict01[item01])
        except StopIteration:
            break

