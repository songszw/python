list1 = ['1.just do it','2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothong']
list2 = ['4.阿迪达斯','2.李宁','3.鱼c工作室','1.耐克']
list3=[]
list4 = list2.sort()
print(list4)
for a in list1:
    for b in list4:
        if a[0]==b[0]:
            list3.append(a,':',b[2:])
