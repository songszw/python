def file_view(filename,linenum):
	if linenum.strip() ==':':
		begin = '1'
		end = '-1'
	(begin,end) = linenum.split(':')
	if begin == '':
		begin = '1'
	if end == '':
		end = '-1'
	if begin == '1' and end == '-1':
		text = '的全文'
	elif begin == '1':
		text = '从开始到%s' % end
	elif end =='-1':
		text = '从%s到结束' % begin
	else:
		text = '从%s行到第%s行'%(begin,end)
	print('文件%s%s的内容如下：/n'%(filename,text))
	begin = int(begin)-1
	end = int(end)
	linnes = end-begin
	f = open('F:\\'+filename+'.txt')
	for i in range(begin):
		f.readline()
	if linnes<0:
		print(f.read())
	else:
		for j in range(linnes):
			print(f.readline(),end='')
	f.close()

filename = input('请输入要打开的文件：')
linenum = input('请输入要显示的行数：')
file_view(filename,linenum)
