def seaveFile(boy,girl,count):
    fileNameB = 'F://boy_'+str(count)+'.txt'
    fileNameG = 'F://girl_'+str(count)+'.txt'
    boyfile = open(fileNameB,'w')
    girlfile = open(fileNameG,'w')
    boyfile.writelines(boy)
    girlfile.writelines(girl)
    boyfile.close()
    girlfile.close()
def splitFile(fileName):
    count =1
    boy = []
    girl = []
    f = open(fileName)
    for each in f:
        if each[:6]!='======':
            (people,world)=each.split(':',1)
            if people == "小甲鱼":
                boy.append(world)
            elif people == "小客服":
                girl.append(world)
        else:
            seaveFile(boy, girl, count)
            boy=[]
            girl=[]
            count+=1
    seaveFile(boy, girl, count)
    f.close()
splitFile('F://record.txt')