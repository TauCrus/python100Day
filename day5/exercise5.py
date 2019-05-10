'''
craps赌博游戏
规则：玩家掷两个骰子，每个骰子点数为1-6，
如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，
玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；
若掷出的点数和为7则庄家胜。
'''

from random import randint

money = 1000
result = '你破产了，游戏结束！'

while money > 0:
    print('你的总资产为：', money)
    needs_go_on = False

    '''
    while True:
        debt = int(input('请下注：'))
        if debt > 0 and debt <= money:
            break
    '''
    debt = money

    first = randint(1, 6) + randint(1, 6)
    print('玩家(first)摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    # print("needs_go_on:", needs_go_on)

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家(current)摇出了%d点' % current)
        if current == 7:
            print('庄家胜！')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜！')
            money += debt
        needs_go_on = False

    if money >= 1000000:
        result = '恭喜你成为百万富翁'
        break

print(result)

