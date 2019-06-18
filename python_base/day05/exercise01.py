list01 = []
print(list01)
list01 = list(range(5))
print(list01)
list01.append("niam")
list01.append("nihao0")
print(list01)
list01.insert(1,"dksj")
print(list01)
list01.remove("niam")
print(list01)
del list01[1]
print(list01)
list01[3]="afhsjfsdh"
print(list01)
list02 = list01[:3]
print(list02)
list01[:3] = []
print(list01[:3])
for index in range(len(list01)):
    print(index)