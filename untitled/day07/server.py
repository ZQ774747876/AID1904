from  socket import  *
import  struct
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('127.0.0.1',9999))
st=struct.Struct('i32sif')
f=open("file01","a")
while True:
    data,addr=sockfd.recvfrom(1024)
    data=struct.unpack(data)
    info="%d   %-10s   %d    %.1f"%(data[0],data[1],data[2],data[3])
    
sockfd.close()