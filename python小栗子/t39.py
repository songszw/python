def huilianwen(worlds):
    length = len(worlds)
    last = length-1
    length //= 2
    flag=1
    for each in range(length):
        if worlds[each]!=worlds[last]:
            flag=0
        last-=1

    if flag==1:
        return 1
    else:
        return 0

worlds = input('请输入要查询的内容：')
if huilianwen(worlds)==1:
    print('是回连文')
else:
    print('不是回连文')
    
