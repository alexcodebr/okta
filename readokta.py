import json

#Read file
with open('logs.json', 'r') as f:
  data = json.load(f)
  #print(list(data)) 
# Output: {'name': 'Bob', 'languages': ['English', 'French']}
#print(data)
#print(json.dumps(data,indent=4))


for i in data:
 #print (list(i))
 
 print(type(i))
 #print(i.values())
 print('Event Type: '+ i['eventType'])

  #print(list(i))
 #print(i['debugContext']['debugData'].keys())
 detalhe = i['debugContext']['debugData']


 print(type(i['debugContext']['debugData']))
 print(i['debugContext']['debugData'].keys())


 #print(type(detalhe))
 #for d in detalhe:
  # print(type(d))


 ##VERY COOL!!!
 #dictDebug vira lista
 #dictDebug = list(i['debugContext']['debugData'])
 #print(type(dictDebug))
 #print(dictDebug)
 ##VERY COOL!!!

 #debCon = i['debugContext']


##VERY COOL!!!
 #json_object = json.dumps(dictDebug, indent = 4) 
 #print(type(json_object))
 #print(json_object)
 
##VERY COOL!!!



 #jsonData = i.debugContext.debugData
 #print(jsonData.keys())
 #keys = i.keys()
#for x in jsonData:
            #print(x)
 #          keys = x.keys()
 #          print(keys)



#jsonData = data['debugContext']['debugData']
#for x in data:
            #print(x)
#            keys = x.keys()
#            print(keys)
#
#print(json.dumps(data['debugContext']['debugData'],indent=1))
