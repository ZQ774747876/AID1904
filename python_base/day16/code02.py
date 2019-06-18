"""
异常处理
"""
def get_score():
    while True:

        try:
         score = int(input("请输入成绩:"))
        except ValueError:
            continue
        if 0<=score<=100:
            return  score



print(get_score())




