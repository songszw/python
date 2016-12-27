f=open('F:\\record.txt')
boy=[]
girl=[]
count = 1
for each in f:
	if each[:6]!= '======':
		(role,line_spoken) = each.split(":",1)
		if role == '小甲鱼':
			boy.append(line_spoken)
		if role == '小客服':
			girl.append(line_spoken)

	else:
		fileNameBoy = 'box-'+str(count)+'.txt'
		fileNameGirl = 'girl'+str(count)+'.txt'

		boyFile = open('F:\\'+fileNameBoy,'w')
		girlFile = open('F:\\'+fileNameGirl,'w')

		boyFile.writelines(boy)
		girlFile.writelines(girl)

		boyFile.close()
		girlFile.close()

		boy=[]
		girl=[]
		count+=1
fileNameBoy = 'box-'+str(count)+'.txt'
fileNameGirl = 'girl'+str(count)+'.txt'

boyFile = open('F:\\'+fileNameBoy,'w')
girlFile = open('F:\\'+fileNameGirl,'w')

boyFile.writelines(boy)
girlFile.writelines(girl)

boyFile.close()
girlFile.close()

boy=[]
girl=[]		
f.close()
