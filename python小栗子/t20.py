pwd= input('请输入需要检查的密码组合')
length = len(pwd)
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
qdc=0
qdq = 0
while(pwd.isspace()or length==0):
    pwd = input('您输入的密码为空（或空格）,请重新输入')
    length = len(pwd)
 
if length<=8:
    qdc = 1
elif 8<length<=16:
    qdc=2
elif 16<length:
    qdc=3
    
for each in pwd:
    if each in symbols:
        qdq+=1
    
    if each in chars:
        qdq+=1
        
    if each in nums:
        qdq+=1
        

while 1:
    print('您的密码安全级别为： ',end='')
    if qdc==1 or qdq==1:
        print('低')
    elif qdc==2 or qdq==2:
        print('中')
    elif qdc==3 or qdq==3:
        print('高')
    break
            
