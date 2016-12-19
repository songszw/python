user_data = {}
def new_user():
    pormpt = '请输入用户名：'
    while True:
        name = input(pormpt)
        if name in user_data:
            pormpt = '此用户名已经被使用，请重新输入'
            continue
        else:
            break

    password = input('请输入密码：')
    user_data[name]=password
    print('注册成功，请登陆')

def old_user():
    pormpt = '请输入用户名：'
    while True:
        name = input(pormpt)
        if name in user_data:
            break
        else:
            print('您输入的用户名不存在，请重新输入：')
            continue

    passworld = input('请输入密码：')
    if passworld==user_data[name]:
        print('欢迎进入本系统，请点击右上角x结束程序！')
    else:
        print('密码错误！')
def showmenu():
    pormpt= '''
|=== 新建用户：N/n ===|
|=== 登陆账号：E/e ===|
|=== 退出程序：Q/q ===|
|=== 请输入指令代码：'''
    while True:
        chose = False
        while not chose:
            choice = input(pormpt)
            if choice not in 'NnEeQq':
                print('您输入的指令代码有误，请重新输入：')
            else:
                chose = True
        if choice == 'q' or choice == 'Q':
            break
        if choice == 'n' or choice == 'N':
            new_user()
        if choice == 'e' or choice == 'E':
            old_user()

showmenu()
