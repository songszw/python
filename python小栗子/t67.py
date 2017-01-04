def createText(fileName):
	f = open('F:\\'+fileName+'.txt','w')
	print('请输入内容，\':w\'退出：')
	while True:
		textValue = input()
		if textValue!=':w':
			f.write('%s\n' % textValue)
		else:
			break
	f.close()
fileName = input('请输入文件名:')
createText(fileName)


		
