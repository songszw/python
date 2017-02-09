import os
allfiles = os.listdir(os.curdir)
typedict = dict()
for each in allfiles:
	if os.path.isdir(each):
		typedict.setdefault(each,0)
		typedict[each]+=1
	else:
		ext = os.path.splitext(each)[1]
		typedict.setdefault(ext,0)
		typedict[ext]+=1
for each in typedict:
	print('该文件夹下面共有类型为【%s】的文件 %d 个'% (each,typedict[each]))