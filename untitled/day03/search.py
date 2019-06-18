"""
search.py 基本查找方法训练
"""
# def search(list_,key):
#     low=0
#     high=len(list_)-1
#     while low<=high:
#         mid = (low + high) // 2
#         if list_[mid]>key:
#             high=mid-1
#         elif list_[mid]<key:
#             low=mid+1
#         else:
#             return mid
def buble(list_):
    for i in range(len(list_)-1):
        for j in range(len(list_)-1-i):
            if list_[j]>list_[j+1]:
                list_[j],list_[j+1]=list_[j+1],list_[j]


def select(list_):

    for i in range(len(list_)-1):
        for j in range(i+1,len(list_)):
            if list_[i]>list_[j]:
                list_[i],list_[j]=list_[j],list_[i]


list01=[4,3,5,6,2,1]
select(list01)
print(list01)



