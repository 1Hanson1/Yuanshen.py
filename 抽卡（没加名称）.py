# 原神抽卡模拟器
import random

a = '单抽'
b = '十连'
res4 = 0  # 4水位
res5 = 0  # 5水位
num4 = 0  # 4星个数
num5 = 0  # 5星个数
al = 0  # 总抽
wai4 = 0  # 4歪
wai5 = 0  # 5歪
half = [0, 1]  # 0歪1中
z5 = 0  # 5星中
z4 = 0  # 4星中
cz5 = ['']
up5 = ['']
cz4 = ['']
up4 = ['']
cz = ['']
zh = 0  # 整活
for i in range(100000):
    list1 = random.sample([i for i in range(1, 1001)], 1000)
    list2 = random.sample([i for i in range(1, 1001)], 100)
    list3 = random.sample([i for i in range(1, 1001)], 5)
    for j in range(1000):
        choice2 = str(input("单抽还是十连呢？\n作出你的选择："))
        if choice2 not in [a, b]:
            if zh <= 4:
                zh += 1
                print("请输入有效选择！！！再选错不让你玩了")
                continue
            else:
                print("你太调皮了！！！不给你玩了！！！哼！（气气）")
                exit(0)
        if choice2 in [a, b]:
            zh = 0
            if choice2 == a:
                one = [random.choice(list1) for i in range(1)]
                for x in one:
                    if (res4 // 9 == 1 and res5 // 89 == 1) or res5//89 == 1:
                        if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:
                            z5 += 1
                            wai5 = 0
                            al += 1
                            res5 = 0
                            num5 += 1
                            print("恭喜你中限定了！！！")
                        else:
                            al += 1
                            num5 += 1
                            res5 = 0
                            wai5 += 1
                            print("你五星歪了")
                    elif res4 // 9 == 1:
                        if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:
                            z4 += 1
                            al += 1
                            res4 = 0
                            res5 += 1
                            num4 += 1
                            wai4 = 0
                            print("up四星，不错诶～")
                        else:
                            al += 1
                            num4 += 1
                            res4 = 0
                            res5 += 1
                            wai4 += 1
                            print("你四星是歪的")
                    else:
                        if x in list3:
                            if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:
                                z5 += 1
                                wai5 = 0
                                al += 1
                                res5 = 0
                                num5 += 1
                                print("恭喜你中限定了！！！")
                            else:
                                al += 1
                                num5 += 1
                                res5 = 0
                                wai5 += 1
                                print("你五星歪了")
                        elif x in list2:
                            if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:
                                z4 += 1
                                al += 1
                                res4 = 0
                                res5 += 1
                                num4 += 1
                                wai4 = 0
                                print("up四星，不错诶～")
                            else:
                                al += 1
                                num4 += 1
                                res4 = 0
                                res5 += 1
                                wai4 += 1
                                print("你四星是歪的")
                        else:
                            al += 1
                            res4 += 1
                            res5 += 1
                            print("你只抽到了三星")
            if choice2 == b:
                ten = [random.choice(list1) for i in range(10)]
                for m in ten:
                    if (res4 // 9 == 1 and res5 // 89 == 1) or res5//89 == 1:
                        if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:
                            z5 += 1
                            wai5 = 0
                            al += 1
                            res5 = 0
                            num5 += 1
                            print("恭喜你中限定了！！！")
                        else:
                            al += 1
                            num5 += 1
                            res5 = 0
                            wai5 += 1
                            print("你五星歪了")
                    elif res4 // 9 == 1:
                        if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:
                            z4 += 1
                            al += 1
                            res4 = 0
                            res5 += 1
                            num4 += 1
                            wai4 = 0
                            print("up四星，不错诶～")
                        else:
                            al += 1
                            num4 += 1
                            res4 = 0
                            res5 += 1
                            wai4 += 1
                            print("你四星是歪的")
                    else:
                        if m in list3:
                            if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:
                                z5 += 1
                                wai5 = 0
                                al += 1
                                res5 = 0
                                num5 += 1
                                print("恭喜你中限定了！！！")
                            else:
                                al += 1
                                num5 += 1
                                res5 = 0
                                wai5 += 1
                                print("你五星歪了")
                        elif m in list2:
                            if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:
                                z4 += 1
                                al += 1
                                res4 = 0
                                res5 += 1
                                num4 += 1
                                wai4 = 0
                                print("up四星，不错诶～")
                            else:
                                al += 1
                                num4 += 1
                                res4 = 0
                                res5 += 1
                                wai4 += 1
                                print("你四星是歪的")
                        else:
                            al += 1
                            res4 += 1
                            res5 += 1
                            print("你只抽到了三星")
        print("总共抽了", al)
        print("出了", num4, "个四星", "中了", z4, "个")
        print("出了", num5, "个五星", "中了", z5, "个")
        print("四星水位计数板：", res4, "  是否保底状态(0否1是)", wai4)
        print("五星水位计数板：", res5, "  是否保底状态(0否1是)", wai5)
        if 1 in [1]:
            break
