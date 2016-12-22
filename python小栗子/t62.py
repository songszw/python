user_data = {}
def new_user():
	text = '请输入用户名:'
	while True:
		username = input(text)
		if username in user_data:
			print('该用户名已存在')
			continue
		else:
			break
	passworld = input('请输入密码：')
	user_data[username]=passworld

def old_user():
	text = '请输入用户名：'
	while True:
		username = input(text)
		if username in user_data:
			break
		else:
			print('查无此人')
			continue
	passworld = input('请输入密码：')		
	if passworld==user_data[username]:
		print('登陆成功，点击右上角按钮关闭程序')
	else:
		print('密码错误')

def showmenu():
	text = '''
|===新建用户：N/n===|
|===登陆账号：E/e===|
|===退出登陆：Q/q===|
|===请输入指令代码：'''
	while  True:
		onoff = False
		while not onoff:
			code = input(text)
			if code not in 'QNEqne':
				print('您输入的指令有误，请重新输入')
			else:
				onoff = True
		if code=='q' or code =='Q':
			break
		if code=='n' or code =='N':
			new_user()
		if code=='e' or code =='E':
			old_user()
showmenu()
		

