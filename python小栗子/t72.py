def filecheck(file1,file2):
	f1 = open('F:\\'+file1+'.txt')
	f2 = open("F:\\"+file2+'.txt')
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
file1 = input('请输入第一个文件名称：')
file2 = input('请输入第二个文件名称：')

wahahah = filecheck(file1,file2)
print(wahahah)
if len(wahahah)==0:
	print('两个文件完全一样')
else:
	print('两个文件共有%d处不同'% len(wahahah))
	for each in wahahah:
		print('第%d行不一样'%each)



