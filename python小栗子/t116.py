try:
    sum = 1+"1"
    f = open('F://wahahah.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件名不存在'+str(reason))
except TypeError as reason:
    print('类型错误'+str(reason))