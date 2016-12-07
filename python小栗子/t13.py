num=3
pwd = 'song0315'

while num:
    text = input('请输入密码： ')
    if text == pwd:
        print('登陆成功')
        break
    elif '*' in text:
        print('密码中不允许出现*，您还有',num,'次机会')
        continue
    else:
        print('密码错误，您还有',num-1,'机会')
    num-=1
