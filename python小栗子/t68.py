def file_compare(file1,file2):
	f1 = open('F:\\'+file1+'.txt')
	f2 = open('F:\\'+file2+'.txt')
	count = 0
	differ = []
	for line1 in f1:
		line2 = f2.readline()
		count+=1
		if line1!= line2:
			differ.append(count)
	f1.close()
	f2.close()
	return differ
file1 = input('请输入一个要比较的文件名：')
file2 = input('请输入另一个要比较的文件名：')
differ=  file_compare(file1,file2)
print(differ)

if len(differ) == 0:
	print('两个文件完全一样')
else:
	print('两个文件共有 %d 处不同：' % len(differ))
	for each in differ:
		print('第 %d 行不一样'% each)
		
