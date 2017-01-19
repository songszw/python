def file_view(filename, linenum):
	if linenum.strip()==':':
		begin = '1'
		end = '-1'
	(begin,end) = linenum.split(':')

	if begin=='':
		begin = '1'
	if end == '':
		end = '-1'
	if begin == '1' and end == '-1':
		prompt = '的全文'
	elif begin =='1':
		prompt = '从开始到%s' % end
	elif end == '-1':
		prompt = '从%s到结束'% begin
	else:
		prompt = '从第%s行到第%s行'%(begin,end)
	print('\n文件%s%s的内同是：\n' % (filename,prompt))
	begin = int(begin)-1
	end =int(end)
	lines = end-begin
	f = open('F:\\'+filename+'.txt')
	for i in range(begin):
		f.readline()
	if lines < 0:
		print(f.read())
	else:
		for j in range(lines):
			print(f.readline(),end='')
	f.close()
filename = input('请输入要打开的文件：')
linenum = input('请输入要显示的行数:')
file_view(filename,linenum)
