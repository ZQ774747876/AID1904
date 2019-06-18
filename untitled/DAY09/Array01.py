from multiprocessing import Process,Array
#创建共享内存
shm=Array('c',b"dskf")#表示开辟是3个空间的列表
def fun():
    for i in shm:
        print(i)
    shm[1]=b"H"
p=Process(target=fun)
p.start()
p.join()


for i in shm:
    print(i)
print(shm.value)#打印字节串，只针对于字节串有效