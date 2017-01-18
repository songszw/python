def read_text(filename,line):
	f = open('F:\\'+filename+'.txt')
	line = int(line)
	for each in range(line):
		print(f.readline(),end='')
	f.close()
filename = input('请输入要查询的文件名：')
line = input('请输入要查询的行数：')
read_text(filename,line)