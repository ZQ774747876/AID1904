import os
f=open("file01","w+")
def top():
    fr=open(filename,'rb')
    fw=open()
s01=os.path.getsize("file01")
pid=os.fork()
if pid<0:
       print("error")
elif pid==0:
     top()#复制上半
else:
     bot()