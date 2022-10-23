# 原神抽卡模拟器
import random

a = '单抽'
b = '十连'
c = '结束'
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
cz5 = ['提纳里', '刻晴   ', '迪卢克  ', '七七   ', '莫娜   ', '琴    ']
up5 = ['妮露   ']
cz4w = ['弓藏   ', '祭礼弓  ', '绝弦   ', '西风猎弓 ', '昭心   ', '祭礼残章 ', '流浪乐章 ', '西风秘典 ', '西风长枪 ', '匣里灭辰 ',
        '雨裁   ', '祭礼大剑 ', '钟剑   ', '西风大剑 ', '匣里龙吟 ', '祭礼剑  ', '笛剑   ', '西风剑  ']
cz4j = ['多莉   ', '柯莱   ', '久岐忍   ', '云堇   ', '鹿野院平藏', '九条挲罗 ', '五郎   ', '早柚   ', '托马   ', '烟绯   ', '罗莎莉亚 ', '辛焱   ',
        '砂糖   ', '迪奥娜  ', '重云   ', '诺艾尔  ', '班尼特  ', '菲谢尔  ', '凝光   ', '行秋   ', '雷泽   ']
cz4 = cz4j + cz4w
up4 = ['香菱   ', '北斗   ', '芭芭拉  ']
cz3 = ['弹弓   ', '神射手之誓', '鸦羽弓  ', '翡玉法球 ', '讨伐英杰谭', '魔导绪论 ', '黑缨枪  ', '以理服人 ', '沐浴龙血的剑',
       '铁影阔剑 ', '飞天御剑 ', '黎明神剑 ', '冷刃 ']
zh = 0  # 整活
for i in range(100000):
    list1 = random.sample([i for i in range(1, 10001)], 10000)  # 总列表
    list2 = random.sample([i for i in range(1, 10001)], 1300)  # 4星
    list3 = random.sample([i for i in range(1, 10001)], 160)  # 3星
    for j in range(100000):
        choice2 = str(input("单抽,十连,还是结束呢？\n作出你的选择："))  # 选择抽卡方式
        if choice2 not in [a, b, c]:  # 如果不在选的范围
            if zh <= 4:  # 拿来纠正输入内容，计数连续输错5次，直接结束程序
                zh += 1
                print("请输入有效选择！！！再选错不让你玩了")
                continue
            else:
                print("你太调皮了！！！不给你玩了！！！哼！（气气）")
                exit(0)
        if choice2 in [a, b, c]:  # 输入合理开始判定
            if choice2 == a:  # 选择单抽
                one = [random.choice(list1) for i in range(1)]  # list1内抽取一个整数
                for x in one:
                    if (res4 // 9 == 1 and res5 // 89 == 1) or res5 // 89 == 1:  # 四五星同时保底
                        if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:  # 大小保底判定（wai5）
                            z5 += 1
                            wai5 = 0
                            al += 1
                            res5 = 0
                            num5 += 1
                            print("\033[1;33;40m", random.choice(up5), "\033[0m")
                        else:
                            al += 1
                            num5 += 1
                            res5 = 0
                            wai5 += 1
                            print("\033[1;33;40m", random.choice(cz5), "\033[0m")
                    elif res4 // 9 == 1:  # 四星保底
                        if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:  # 四星保底判断（wai4）
                            z4 += 1
                            al += 1
                            res4 = 0
                            res5 += 1
                            num4 += 1
                            wai4 = 0
                            print("\033[1;35;40m", random.choice(up4), "\033[0m")
                        else:
                            al += 1
                            num4 += 1
                            res4 = 0
                            res5 += 1
                            wai4 += 1
                            print("\033[1;35;40m", random.choice(cz4), "\033[0m")
                    else:  # 不含特殊情况判定
                        if x in list3:  # 三星
                            if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:  # 歪判定以及保底
                                z5 += 1
                                wai5 = 0
                                al += 1
                                res5 = 0
                                num5 += 1
                                print("\033[1;33;40m", random.choice(up5), "\033[0m")
                            else:
                                al += 1
                                num5 += 1
                                res5 = 0
                                wai5 += 1
                                print("\033[1;33;40m", random.choice(cz5), "\033[0m")
                        elif x in list2:  # 四星
                            if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:  # 歪判定以及保底
                                z4 += 1
                                al += 1
                                res4 = 0
                                res5 += 1
                                num4 += 1
                                wai4 = 0
                                print("\033[1;35;40m", random.choice(up4), "\033[0m")
                            else:
                                al += 1
                                num4 += 1
                                res4 = 0
                                res5 += 1
                                wai4 += 1
                                print("\033[1;35;40m", random.choice(cz4), "\033[0m")
                        else:
                            al += 1
                            res4 += 1
                            res5 += 1
                            print("\033[1;34;40m", random.choice(cz3), "\033[0m")
            if choice2 == b:
                ten = [random.choice(list1) for i in range(10)]  # list1里抽10个数
                for m in ten:  # 进行十次单抽
                    if (res4 // 9 == 1 and res5 // 89 == 1) or res5 // 89 == 1:
                        if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:
                            z5 += 1
                            wai5 = 0
                            al += 1
                            res5 = 0
                            num5 += 1
                            print("\033[1;33;40m", random.choice(up5), "\033[0m")
                        else:
                            al += 1
                            num5 += 1
                            res5 = 0
                            wai5 += 1
                            print("\033[1;33;40m", random.choice(cz5), "\033[0m")
                    elif res4 // 9 == 1:
                        if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:
                            z4 += 1
                            al += 1
                            res4 = 0
                            res5 += 1
                            num4 += 1
                            wai4 = 0
                            print("\033[1;35;40m", random.choice(up4), "\033[0m")
                        else:
                            al += 1
                            num4 += 1
                            res4 = 0
                            res5 += 1
                            wai4 += 1
                            print("\033[1;35;40m", random.choice(cz4), "\033[0m")
                    else:
                        if m in list3:
                            if [random.choice(half) for i in range(1)] == [1] or wai5 == 1:
                                z5 += 1
                                wai5 = 0
                                al += 1
                                res5 = 0
                                num5 += 1
                                print("\033[1;33;40m", random.choice(up5), "\033[0m")
                            else:
                                al += 1
                                num5 += 1
                                res5 = 0
                                wai5 += 1
                                print("\033[1;33;40m", random.choice(cz5), "\033[0m")
                        elif m in list2:
                            if [random.choice(half) for i in range(1)] == [1] or wai4 == 1:
                                z4 += 1
                                al += 1
                                res4 = 0
                                res5 += 1
                                num4 += 1
                                wai4 = 0
                                print("\033[1;35;40m", random.choice(up4), "\033[0m")
                            else:
                                al += 1
                                num4 += 1
                                res4 = 0
                                res5 += 1
                                wai4 += 1
                                print("\033[1;35;40m", random.choice(cz4), "\033[0m")
                        else:
                            al += 1
                            res4 += 1
                            res5 += 1
                            print("\033[1;34;40m", random.choice(cz3), "\033[0m")
            if choice2 == c:  # 结束进程
                print("总共抽了", al)
                print("出了", num4, "个四星", "中了", z4, "个")
                print("出了", num5, "个五星", "中了", z5, "个")
                print("四星水位计数板：", res4, "  是否保底状态(0否1是)", wai4)
                print("五星水位计数板：", res5, "  是否保底状态(0否1是)", wai5)
                exit(0)
        print("总共抽了", al)
        print("出了", num4, "个四星", "中了", z4, "个")
        print("出了", num5, "个五星", "中了", z5, "个")
        print("四星水位计数板：", res4, "  是否保底状态(0否1是)", wai4)
        print("五星水位计数板：", res5, "  是否保底状态(0否1是)", wai5)
        if 1 in [1]:
            break
