import random
random_number = random.randint(1, 100)
count = 0
while count < 7:
  count += 1
  input_number = int(input("请输入整数:"))
  if input_number > random_number:
    print("大了")
  elif input_number < random_number:
    print("小了")
  else:
    print("猜对了,总共猜了" + str(count) + "次")
    break
else:
  print("游戏失败")