import os
all_files = os.listdir(os.curdir)
type_dict = dict()
for each in all_files:
	if os.path.isdir(each):
		type_dict.setdefault('文件夹',0)
		type_dict['文件夹']+=1
	else:
		ext = os.path.splitext(each)[1]
		type_dict.setdefault(ext,0)
		type_dict[ext]+=1
for each in type_dict.keys():
	print('该文件夹下面共有类型为【%s】的文件%d 个'%(each,type_dict[each]))
	