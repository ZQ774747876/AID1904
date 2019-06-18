dict01={}
while True:

   name=input("请输入您的姓名：")
   if name=="esc":
     break
   list01 = []
   dict01[name] = list01
   while True:
        hobby=input("请输入您的喜好(esc结束)：")
        if hobby=="esc":
            break
        list01.append(hobby)


for key,value in dict01.items():
    print("%s的兴趣爱好是%s"%(key,value))
