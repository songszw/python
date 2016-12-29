def createFile(boy,girl,count):
	boyFileName = 'boy_'+str(count)+'.txt'
	girlsFileName = 'girl_'+str(count)+'.txt'
	boyFile = open('F:\\'+boyFileName,'w')
	girlsFile = open('F:\\'+girlsFileName,'w')
	boyFile.writelines(boy)
	girlsFile.writelines(girl)
	boyFile.close()
	girlsFile.close()
	
def restart(filename):
	boy = []
	girl=[]
	count = 1
	a = open('F:\\'+filename)
	for each in a:
		if each[:6]!='======':
			(people,worlds) = each.split(':',1)
			if people == '小甲鱼':
				boy.append(worlds)
			else:
				girl.append(worlds)
		else:
			createFile(boy,girl,count)
			boy = []
			girl= []
			count+=1
	createFile(boy,girl,count)
	a.close()

restart('record.txt')


