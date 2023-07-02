import csv
import json 

file = open("et.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

#print(data)

#create Pyhton dictionary
etype = {"eventType": data[0][0]}
#print(type(etype))

#add element
var3=  data[0][1],data[0][2]
etype.update({"outcome.result": data[0][0]})
etype.update(dict(debugData=var3))
print(type(etype))


#print json
js= json.dumps(etype,indent=4)
print(js)
