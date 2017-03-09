import pickle
files = open('F://mypickle.pkl','rb')
mylist = pickle.load(files)
print(mylist)