import pickle
filesname = open('F://myfiles.pkl','rb')
mytest = pickle.load(filesname)
print(mytest)