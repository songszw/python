def file_compare(file1,file2):
	f1 = open('F:\\'+file1+'.txt')
	f2 = open('F:\\'+file2+'.txt')
	count = 0
	differ = []
	for line1 in f1:
		line2 = f2.readline()
		count+=1
		if line1 != line2:
			differ.append(count)
	f1.close()
	f2.close()
	return differ
file1 = input('请输入第一个文件名：')
file2 = input('请输入第二个文件名：')
differ = file_compare(file1,file2)
if len(differ)==0:
	print('这两个文件完全相同')
else:
	print('这两个文件共有 %d 处不同'% len(differ))
	for length in differ:
		print('分别是第 %d 行不同' % length)
