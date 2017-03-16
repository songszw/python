import random
import easygui as g
g.msgbox(msg='你好，欢迎进入我的游戏世界')
secret = random.randint(1,10)
msg = '你猜，我现在在想哪一个数字？'
title = '第一个小游戏'
guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
while True:
    if guess==secret:
        g.msgbox(msg='wohoo,bingo')
        break
    else:
        if guess>secret:
            g.msgbox(msg='大啦')
        else:
            g.msgbox(msg='小啦')
    guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
g.msgbox(msg='Game Over')