num = 3
pwd='song0315'
while num:

    text = input('请输入密码：')

    if text==pwd :
        print('登陆成功')
        break
    elif '*' in text:
        print('含有非法字符*，请重新输入，您还有',num,'次机会')
        continue
    else:
        print('密码输入错误，您还有',num-1,'次机会',end=' ')
   
    num-=1
