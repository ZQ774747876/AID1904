from socket import *
import struct
ADDR=('127.0.0.1',8888)
st=struct.Struct('i32sif')
s=socket(AF_INET,SOCK_DGRAM)
while True:
    id = int(input("编号："))
    name = str(input("姓名:")).encode()
    age = int(input("年龄:"))
    score = float(input("分数:"))
    data=st.pack(id,name,age,score)
    s.sendto(data,ADDR)

sockfd.close()