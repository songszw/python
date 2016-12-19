data = '1000,littleFish,man'
mydict = {}
(mydict['id'],mydict['name'],mydict['sex'])=data.split(',')
print('ID:'+mydict['id'])
print('Name:'+mydict['name'])
print('Sex:'+mydict['sex'])
print(mydict)

