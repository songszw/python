def filechange(filename,old,new):
	fileread = open('F:\\'+filename+'.txt')
	content = []
	count = 0

	for eachline in fileread:
		if old in eachline:
			count+=eachline.count(old)
			eachline = eachline.replace(old,new)
		content.append(eachline)
	decide = input('%s中共有%s个【%s】，\n您是否要讲所有的%s全部替换为%s\n【YSE|NO】：'%(filename,count,old,old,new))
	if decide in ['yes','YES','Yes']:
		f = open('F:\\'+filename+'.txt','w')
		f.writelines(content)
		f.close()
	
	fileread.close()
filename = input('请输入要更改的文件：')
old = input('请输入要查询的内容：')
new=  input('请输入要替换成的内容：')
filechange(filename,old,new)