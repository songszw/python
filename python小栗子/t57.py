print('|--- 欢迎进入宋氏通讯录 ---|')
print('|--- 1：查询联系人资料 ---|')
print('|--- 2：插入新的联系人 ---|')
print('|--- 3：删除已有联系人 ---|')
print('|--- 4：退出通讯录程序 ---|')

contacts = dict()
while 1:
    num = int(input('please enter the number you want to do: '))

    if num==1:
        name = input('please enter the name you waht to check: ')
        if name in contacts:
            print(name+':'+contacts[name])
        else:
            print('sorry,the man who wasn\'t here')
    if num==2:
        name = input('please enter your name:')
        if name in contacts:
            print('sorry, the man is already in the contacts -->>',end=' ')
            print(name+":"+contacts[name])
            if input('do you want to change the name ?[YES/NO]:')=='YES':
                contacts[name]=input('please enter the phone number:')
            else:
                contacts[name] =input('please enter the phone number:')
        else:
            contacts[name]=input('please enter the phone number:')
    if num==3:
        name = input('please enter the name who you want to delete:')
        if name in contacts:
            contacts.pop(name)
        else:
            print('sorry, the man who wasn\'t here')
    if num==4:
         break
print('|--- 感谢使用通讯录程序 ---|')
