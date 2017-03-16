import  easygui as g
import os
#要选择的文件
file_path = g.fileopenbox(default='*.txt')
with open(file_path) as old_file:
    #获取文件名称，os.path.basename,去除文件路径，单独返回文件名
    title = os.path.basename(file_path)
    msg = '文件【%s】的内容如下：'% title
    text = old_file.read()
    text_after = g.textbox(msg,title,text)
if text != text_after[:-1]:
    choice = g.buttonbox(
        '检测到文件内容发生改变，请选择一下操作：',
        '警告',
        ('覆盖保存','放弃保存','另存为')
    )
    if choice == '覆盖保存':
        with open(file_path,'w') as old_file:
            old_file.write(text_after[:-1])
    if choice == '放弃保存':
        pass
    if choice == '另存为':
        another_path = g.filesavebox(default='.txt')
        if os.path.splitext(another_path)[1] != '.txt':
            another_path+='.txt'
        with open(another_path,'w') as new_file:
            new_file.write(text_after[:-1])
