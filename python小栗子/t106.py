count =1
boyValue = []
girlValue = []
f = open('F://record.txt')
for each in f:
    if each[:6] != '======':
        (people,world) = each.split(':',1)
        if people == '小甲鱼':
            boyValue.append(world)
        if people == '小客服':
            girlValue.append(world)
    else:
        fileNameB = 'F://boy_'+str(count)+'.txt'
        fileNameG = 'F://girl_'+str(count)+'.txt'
        boyFile = open(fileNameB,'w')
        girlFile = open(fileNameG,'w')
        boyFile.writelines(boyValue)
        girlFile.writelines(girlValue)
        boyValue=[]
        girlValue=[]
        count+=1
fileNameB = 'F://boy_'+str(count)+'.txt'
fileNameG = 'F://girl_'+str(count)+'.txt'
boyFile = open(fileNameB,'w')
girlFile = open(fileNameG,'w')
boyFile.writelines(boyValue)
girlFile.writelines(girlValue)
boyFile.close()
girlFile.close()
f.close()