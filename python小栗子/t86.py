import os
def searchfiles(start,target):
    os.chdir(start)
    for each in os.listdir(os.curdir):
        if each == target:
            print(os.getcwd()+os.sep+each)
        if os.path.isdir(each):
            searchfiles(each,target)
            os.chdir(os.pardir)
startdir = input('请输入要查找的初始目录：')
target = input('请输入要查找的文件:')
searchfiles(startdir,target)