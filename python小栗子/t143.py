import easygui as g
msg = '请填写一下联系方式'
title = '账号中心'
fileName = ['*usernaem','*password','phonenumber','QQ','*E-mail']
fileValue = []
fileValue = g.multenterbox(msg,title,fileName)

while 1:
    if fileValue == None:
        break
    errmsg = ''
    for i in range(len(fileName)):
        option = fileName[i].strip()
        if fileValue[i].strip()=='' and option[0]=='*':
            errmsg+=('[%s]为必填项：\n\n'% str(fileName[i]))
    if errmsg=='':
        break
    fileValue = g.multenterbox(errmsg,title,fileName,fileValue)
print('用户资料如下:%s'%str(fileValue))