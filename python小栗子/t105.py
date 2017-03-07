count = 1
boy = []
girl = []
f = open('f://record.txt')
for each in f:
    if each[:6] in f != "======":
        (a,b) = each.split(':',1)
        if a == '小甲鱼' :
            boy.append(b)
            print(boy)
        if a == '小客服' :
            girl.append(b)
            print(girl)
    else:
        fileName_boy = 'boy_'+str(count)+'.txt'
        fileName_girl = 'girl_'+str(count)+'.txt'
        boy_file = open('f://'+fileName_boy,'w')
        girl_file = open('f://'+fileName_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy = []
        girl = []
        count+=1
fileName_boy = 'boy_' + str(count) + '.txt'
fileName_girl = 'girl_' + str(count) + '.txt'
boy_file = open('f://' + fileName_boy, 'w')
girl_file = open('f://' + fileName_girl, 'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
f.close()
