import easygui as g
import os
file_list = {}
source_list = {}
g.msgbox('请打开您存放所有代码的文件夹','统计代码量')
path = g.diropenbox('请选择您的代码库：')

def calc_code(file_name):
    lines = 0
    with open(file_name) as song:
        print('正在分析文件：%s'%file_name)
        try:
            for each_line in song:
                lines+=1
        except UnicodeDecodeError:
            pass
    return lines


def search_file(start_dir):
    os.chdir()
    for each_file in os.listdir():
        ext = os.path.splitext(each_file)[1]
        if ext == '.py':
            lines = calc_code(each_file)
            try:
                file_list[ext]+=1
            except KeyError:
                file_list[ext]=1

            try:
                source_list[ext]+=lines
            except KeyError:
                source_list[ext]=lines
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)




search_file(path)
