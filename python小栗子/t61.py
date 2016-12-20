user_data={}
def showmenu():
	text = '''
	|===新建用户：N/n===|
	|===登陆账号：E/e===|
	|===退出登陆：Q/q===|
	|===请输入指令代码：'''

	while True:
		choses = False
		while not choses :
			choice = input(text)
			if choice not in 'eEnNqQ':
				print('您输入的指令有误，请重新输入: ')
			else:
				choses = True
		if choice =='q' or choice =='Q':
			break
		if choice =='e' or choice =='E':
			old_user()
		if choice =='n' or choice =='N':
			new_user()
def old_user():
	text = '请输入用户名：'
	while True:
		username = input(text)
		if username not in user_data:
			print('您输入的代码有误，请重新输入')
			continue
		else:
			break
	passworld = input('请输入密码：')
	if passworld==user_data[username]:
		print('欢迎登陆本系统，点击右上角可结束程序')
	else:
		print('密码错误')
def new_user():
	text = '请输入用户名:'
	while True:
		username = input(text)
		if username in user_data:
			print('用户名已存在，请重新输入')
			continue
		else:
			break
	passworld = input('请输入密码:')
	user_data[username]=passworld
	print('注册成功，请登陆')
showmenu()

