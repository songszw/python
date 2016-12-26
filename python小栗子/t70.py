def file_view(fileName,fileLine):
	print('\n文件%s的前%s内容如下：\n'%(fileName,fileLine))
	f = open('F:\\'+fileName+'.txt')
	for i in range(int(fileLine)):
		print(f.readline(),end = '')
	f.close()
fileName = input('请输入要查询的文本：')
fileLine = input('请输入要查询的行数：')
file_view(fileName,fileLine)