# 原神抽卡模拟器
import random

a = '单抽'
b = '十连'
for i in range(100000):
    list1 = random.sample([i for i in range(1, 1001)], 1000)
    list2 = random.sample([i for i in range(1, 1001)], 100)
    list3 = random.sample([i for i in range(1, 1001)], 5)
    for i in range(1000):
        choice2 = str(input("单抽还是十连呢？\n作出你的选择："))
        if choice2 not in [a, b]:
            print("请输入有效选择！！！再选错不让你玩了")
            continue
        if choice2 in [a, b]:
            if choice2 == a:
                for i in range(1000):
                    x = int(input("请输入一个整数（1～1000）："))
                    if x not in list1:
                        print("你输入的数字不在范围内哟！！！")
                        continue
                    if x in list1:
                        break
                if x in list3:
                    print("恭喜你抽到了五星！！！")
                elif x in list2:
                    print("你抽到了四星呢，不错诶～")
                else:
                    print("你只抽到了三星，还好还好，下次再接再励吧！")
            if choice2 == b:
                ten = random.sample([i for i in range(1, 1001)], 10)
                print(ten)
                for l in ten:
                    if l in list3:
                        print("恭喜你抽到了五星！！！")
                    elif l in list2:
                        print("你抽到了四星呢，不错诶～")
                    else:
                        print("你只抽到了三星，还好还好，下次再接再励吧！")
        if 1 in [1]:
            break
