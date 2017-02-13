import os
allfiles = os.listdir(os.curdir)
typedict = dict()
for each in allfiles:
	if os.path.isdir(each):
		continue
	else:
		typedict.setdefault(each,os.path.getsize(each))
		print('%s, [%sBytes]'%(each,typedict[each]))

