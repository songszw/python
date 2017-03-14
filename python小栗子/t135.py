import random
import easygui as g
g.msgbox(msg='(｡･∀･)ﾉﾞ嗨，欢迎进入第一个游戏界面')
secert = random.randint(1,10)
msg = '你猜我现在想的是那个数字啊'
title = '小游戏'
guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
while True:
    if guess == secert:
        g.msgbox(
            msg='卧槽，你是我心中的蛔虫么'
        )
        g.msgbox(
            msg='哼，猜中也没有奖励'
        )
        break
    else:
        if guess>secert:
            g.msgbox(
                msg='大了'
            )
        else:
            g.msgbox(msg='小了')
        guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
g.msgbox('Game Over')
