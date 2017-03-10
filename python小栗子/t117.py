try:
    f = open('F://My_File.txt','w')
    print(f.write('dsfsd'))
    sum =1+'1'
    f.close()
except TypeError as reason:
    print('出错啦：' + str(reason))


