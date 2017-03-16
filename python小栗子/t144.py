import easygui as g
msg = '请填写一下联系方式'
title='账号中心'
fileName = ['*UserName','*PassWord','PhoneNumber','*E-mail','QQ']
fileValue = []
fileValue = g.multenterbox(msg,title,fileName)
while True:
    if fileValue == '':
        break
    errmsg = ''
    for i in range(len(fileName)):
        ss = fileName[i].strip()
        if fileValue[i].strip()==''and ss[0]=='*':
            errmsg+=('[%s]为必填项\n\n'% str(fileName[i]))
    if errmsg=='':
        break
    fileValue = g.multenterbox(errmsg,title,fileName,fileValue)
    print('用户资料如下:%s'% str(fileValue))