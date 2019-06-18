import  time


def excution_time(func):
    def wrpper(*args, **kwargs):
        t01 = time.time()
        func(*args, **kwargs)
        t02 = time.time()
        t = t02 - t01
        print("执行了：", t)
        return func(*args, **kwargs)

    return wrpper

class Student:


    @excution_time

    def study(self):
        print("学习...")
        time.sleep(2)

    @excution_time

    def play(self):
        print("玩耍...")
        time.sleep(3)

s01=Student()
s01.study()






