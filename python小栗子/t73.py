def checkfile(file1,file2):
	f1 = open('F:\\'+file1+'.txt')
	f2 = open('F:\\'+file2+'.txt')
	count = 0
	line = []
	for each1 in f1:
		each2 = f2.readline()
		count+=1
		if each1 != each2:
			line.append(count)
	f1.close()
	f2.close()
	return line
file1 = input('请输入第一个文件名：')
file2 = input('请输入第二个文件名：')
num = checkfile(file1,file2)
if len(num)==0:
	print('这两个文件完全相同')
else:
	print('这两个文件有%d处不同'% len(num))
	for each in num:
		print('第%d行不同'% each)
	