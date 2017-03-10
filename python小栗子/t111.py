import pickle
files = ['sdafsdf','sdfasdf',1234,['sdafasdf',4234]]
picklefiles = open('F://myfiles.pkl','wb')
pickle.dump(files,picklefiles)
picklefiles.close()