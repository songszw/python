import easygui as g
import sys
while 1:
    g.msgbox('(｡･∀･)ﾉﾞ嗨，欢迎使用easygui界面')
    msg = '请问有什么可以帮到您？'
    title= 'easygui界面'
    choices = ['谈恋爱','钓鱼','把妹','琴棋书画']
    choice = g.choicebox(msg,title,choices)
    g.msgbox('your choice is:'+str(choice),'结果')
    msg = '你希望重新开始小游戏吗？'
    title = '请选择'
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit()