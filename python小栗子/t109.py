import pickle
my_list = [123,'what the fuck',['this is another list',123]]
pick_file = open('F://mypickle.pkl','wb')
pickle.dump(my_list,pick_file)
pick_file.close()
