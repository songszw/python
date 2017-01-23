def filechange(filename,oldworld,newworld):
	f_read = open('F:\\'+filename+".txt")
	content = []
	count = 0
	for eachline in f_read:
		if oldworld in eachline:
			count += eachline.count(oldworld)
			
			eachline = eachline.replace(oldworld,newworld)
		content.append(eachline)
	decide = input('%s 中共有 %s 个[%s]\n您确定要把所有的%s 替换成%s吗？\n【YES|NO】：'% (filename,count,oldworld,oldworld,newworld))
	if decide in ['yes','Yes','YES']:
		f_write = open('F:\\'+filename+'.txt','w')
		f_write.writelines(content)
		f_write.close()
	f_read.close()
filename = input('请输入文件名：')
oldworld = input('请输入要替换的话：')
newworld = input('请输入新的内容：')
filechange(filename,oldworld,newworld)
