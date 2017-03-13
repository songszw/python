import easygui as g
import sys
while True:
    g.msgbox('(｡･∀･)ﾉﾞ嗨，欢迎进入第一个界面小游戏(*^_^*)')
    msg = '请问你希望在这里学习什么知识呢？'
    title = '小游戏互动'
    choices = ['Doat','编程','泡妞','钓鱼']
    choice = g.choicebox(msg,title,choices)
    g.msgbox('你的选择是：'+str(choice),'结果')
    msg = '你希望重新开始游戏吗？'
    title = '请选择'
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)