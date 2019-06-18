def triangle(char):
 for r in  range(4):#0 1 2 3
        for c in range(r+1):#0 01 10 11 12 1123
          print(char,  end=" ")
        print()


triangle("*")
triangle("%")