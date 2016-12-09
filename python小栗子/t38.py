def hlw(worlds):
    length = len(worlds)
    a=0
    b=length-1
    c=True
    while c:
        for each in worlds:
            if a<=(length/2):
                if worlds[a]==worlds[b]:
                    a+=1
                    b-=1
                    if a>=length/2:
                        print('是回连文')
                else:
                    print('不是回连文')
                    c=False
                    break
neirong = input('请输入呢容：')
hlw(neirong)
                
                    
            
