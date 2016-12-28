def createTxt(boy,girl,count):
	boy_file = 'boy_'+str(count)+'.txt'
	gitl_file = 'girl_'+str(count)+'.txt'

	boyFile = open('F:\\'+boy_file,'w')
	girlFile = open('F:\\'+gitl_file,'w')

	boyFile.writelines(boy)
	girlFile.writelines(girl)

	

	boyFile.close()
	girlFile.close()

def splitFile(filenaem):
	f = open(filenaem)
	boy = []
	girl = []
	count = 1
	for each in f:
		if each[:6] != "======":
			a = each.split(":",1)
			if a[0] =='小甲鱼':
				boy.append(a[1])
			if a[0] == '小客服':
				girl.append(a[1])
		else:
			createTxt(boy,girl,count)
			boy=[]
			girl=[]
			count+=1

	createTxt(boy,girl,count)
	boy=[]
	girl=[]
	f.close()

splitFile('F:\\record.txt')
