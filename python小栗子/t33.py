def findstr(words,needfind):
    length = len(words)
    count = 0
    if needfind not in words:
        print('he\'s died, i can\'t find it')
    else:
        for each in range(length):
            if words[each]==needfind[0]:
                if words[each+1]==needfind[1]:
                    count+=1
        print('共有 %d 次'% count)
words=input('请输入要查询的大范围：')
needfind=input('请输入要查询的具体内容：')
findstr(words,needfind)
