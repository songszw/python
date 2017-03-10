def splitfiles(boy,girl,count):
    filesnameB = 'Boy_' + str(count) + '.txt'
    filesnameG = 'Girl_' + str(count) + '.txt'
    fb = open('F://' + filesnameB, 'w')
    fg = open('F://' + filesnameG, 'w')
    fb.writelines(boy)
    fg.writelines(girl)
    fb.close()
    fg.close()
def writefiles(filesname):
    count = 1
    boy = []
    girl = []
    f = open(filesname)
    for eachline in f:
        if eachline[:6] != '======':
            (person, say) = eachline.split(':', 1)
            if person == '小甲鱼':
                boy.append(say)
            if person == '小客服':
                girl.append(say)
        else:
            splitfiles(boy,girl,count)
            boy = []
            girl = []
            count += 1
    splitfiles(boy, girl, count)
    f.close()
writefiles('F://record.txt')