"""

# """
# word=input("请输入单词：")
# f=open('dict.txt','r')
# for line in f:
#     tmp=line.split(' ')[0]
#     if tmp>word:
#         print("没有找到该单词")
#         break
#     elif tmp==word:
#         print(line)
#         break
# else:
#     print("没有找到")

# f=open('file','w')
# # f.write("hello word\n".encode())
# # f.write('nihao sdifdks\n'.encode())
# # f.write("sdjkfjo.".encode())
# f.writelines(['abv','dsf'])
with open('file','r+') as  f:
     f.write("dsjfhsdj\n" )
     f.write("hello\n" )
     f.write("I am so suprised\n" )
     f.
     while True:
       DATA=f.readline()
       print(DATA)
       if not DATA:
           break

