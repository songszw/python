def writeText(value):
	f = open('F:\\'+value+'.txt','w')
	print('请输入要打印的内容，输入:w退出程序：')
	while True:
		valueText = input()
		if valueText != ':w':
			f.write('%s\n' % valueText)
		else:
			break
	f.close()
wahaha = input('请输入文件名：')
writeText(wahaha)
