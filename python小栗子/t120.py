def int_input(num = ''):
    while True:
        try:
            int(input(num))
            break
        except ValueError:
            print('输入证书啦，损塞')
int_input('请输入一个整数：')


