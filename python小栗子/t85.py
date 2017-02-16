import os
allfiles = os.listdir(os.curdir)
filedict = dict()
for each in allfiles:
    if os.path.isfile(each):
        filesize = os.path.getsize(each)
        filedict[each] = filesize
for each in filedict.items():
    print('%s【%dBytes】'%(each[0],each[1]))
    